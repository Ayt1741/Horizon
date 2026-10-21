#!/usr/bin/env python3
"""backfill.py — бэкфилл истории за период окнами, идемпотентно."""
import argparse
import datetime
import json
import os
import re
import sys
import time

import state as state_mod
import pipeline as pipe

def parse_ymd(s):
    return datetime.date.fromisoformat(s)

def parse_window(s):
    s = s.strip().lower()
    m = re.match(r"^(\d+)\s*([dwm])$", s)
    if not m:
        raise ValueError(f"bad --window {s}, use e.g. 7d")
    n = int(m.group(1))
    u = m.group(2)
    if u == "d":
        days = n
    elif u == "w":
        days = n * 7
    else:
        days = n * 30
    if days < 1:
        days = 1
    return datetime.timedelta(days=days)

def split_range(dfrom, dto, delta):
    chunks = []
    cur = dfrom
    while cur <= dto:
        end = cur + delta - datetime.timedelta(days=1)
        if end > dto:
            end = dto
        chunks.append((cur, end))
        cur = end + datetime.timedelta(days=1)
    return chunks

def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def day_of_item(it, fallback_day_iso):
    p = it.get("published") or ""
    if len(p) >= 10 and re.match(r"^\d{4}-\d{2}-\d{2}", p):
        return p[:10]
    return fallback_day_iso

def in_chunk(iso_z, cfrom, cto):
    if not iso_z or len(iso_z) < 10:
        return False
    try:
        d = datetime.date.fromisoformat(iso_z[:10])
        return cfrom <= d <= cto
    except Exception:
        return False

def should_skip_incremental(source, chunk_to, today):
    if source.get("incremental_only") and source.get("enabled", True):
        try:
            if (today - chunk_to).days > 14:
                return True
        except Exception:
            return False
    return False

def read_existing_hashes(md_path):
    if not os.path.exists(md_path):
        return set()
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            txt = f.read()
    except Exception:
        return set()
    s = set(re.findall(r"url_hash:([a-f0-9]{64})", txt))
    return s

def render_day_file(day_iso, items_new, out_dir):
    path = os.path.join(out_dir, f"{day_iso}-summary-ru.md")
    existing_hashes = read_existing_hashes(path)
    fresh = [x for x in items_new if x.get("url_hash") not in existing_hashes]
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            old = f.read()
    else:
        old = f"---\nlayout: post\ntitle: \"Выпуск {day_iso} (RU)\"\ndate: {day_iso} 09:00:00 +0000\nlang: ru\n---\n\n# Выпуск {day_iso}\n\n"
    if not fresh:
        return path, 0, len(items_new)
    fresh_sorted = sorted(fresh, key=lambda x: x.get("score", 0), reverse=True)
    blocks = []
    for it in fresh_sorted:
        t_ru = it.get("title_ru") or it.get("title", "")
        summ = it.get("summary_ru") or it.get("summary", "")[:600]
        bullets = it.get("bullets", []) or []
        src = it.get("source_name", "")
        url = it.get("url", "")
        uh = it.get("url_hash", "")
        btxt = ""
        if bullets:
            btxt = "\n".join([f"- {b}" for b in bullets[:5]]) + "\n"
        blocks.append(f"\n## {t_ru}\n\n_{src} · {day_iso} · score {it.get('score',0)}_\n\n{summ}\n\n{btxt}\n[Источник]({url})\n\n<!-- url_hash:{uh} -->\n")
    addition = "\n".join(blocks)
    new_text = old.rstrip() + "\n\n" + addition
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(new_text)
        f.flush()
        try:
            os.fsync(f.fileno())
        except Exception:
            pass
    os.replace(tmp, path)
    return path, len(fresh), len(items_new)

def update_index(out_dir, state):
    idx_path = os.path.join(out_dir, "backfill-index.md")
    dc = state.get("daily_counts", {})
    days = sorted(dc.keys())
    total = sum(dc.values())
    lines = ["---", "layout: page", "title: \"Индекс бэкфилла\"", "---", "", "# Индекс бэкфилла", "", f"Всего дней: {len(days)} · Всего материалов: {total}", "", "| Дата | Материалов | Файл |", "|---|---|---|"]
    for d in days:
        lines.append(f"| {d} | {dc[d]} | [{d}-summary-ru.md](./{d}-summary-ru.md) |")
    txt = "\n".join(lines) + "\n"
    tmp = idx_path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(txt)
        f.flush()
        try:
            os.fsync(f.fileno())
        except Exception:
            pass
    os.replace(tmp, idx_path)

def fetch_rss_for_chunk(sources, cfrom, cto, today, config, session, full_cache):
    throttle = config.get("throttle", {})
    timeout = int(throttle.get("timeout_s", 30))
    delay_s = float(throttle.get("delay_between_feeds_ms", 1200)) / 1000.0
    max_pages_default = int(throttle.get("max_pages_per_feed", 80))
    collected = []
    per_feed = {}
    for src in sources:
        sid = src.get("id", "")
        if not src.get("enabled", True):
            continue
        if should_skip_incremental(src, cto, today):
            per_feed[sid] = 0
            continue
        pag = src.get("pagination", {}) or {}
        ptype = pag.get("type", "none")
        max_pages = int(pag.get("max_pages", max_pages_default))
        try:
            if ptype == "wp_paged":
                raw = pipe.fetch_wp_paginated(src["feed_url"], session, timeout, max_pages, delay_s)
                items = []
                for e in raw:
                    it = pipe.entry_to_item(e, src)
                    if it and it.get("published") and in_chunk(it["published"], cfrom, cto):
                        items.append(it)
                    elif it and not it.get("published"):
                        # без даты — относим к концу чанка только для свежих чанков
                        if (today - cto).days <= 14:
                            it["published"] = cto.isoformat() + "T12:00:00Z"
                            items.append(it)
                collected.extend(items)
                per_feed[sid] = len(items)
            elif ptype == "rest_devto":
                dev_items = pipe.fetch_devto_paginated(session, timeout, min(max_pages, 20), delay_s)
                items = [x for x in dev_items if x.get("published") and in_chunk(x["published"], cfrom, cto)]
                collected.extend(items)
                per_feed[sid] = len(items)
            else:
                # full или window: один запрос, для full — кэш на весь прогон
                if src.get("archive") == "full" and sid in full_cache:
                    raw = full_cache[sid]
                else:
                    raw, _ = pipe.fetch_feed_single(src["feed_url"], session, timeout)
                    if src.get("archive") == "full":
                        full_cache[sid] = raw
                    time.sleep(delay_s)
                items = []
                for e in raw:
                    it = pipe.entry_to_item(e, src)
                    if it and it.get("published") and in_chunk(it["published"], cfrom, cto):
                        items.append(it)
                collected.extend(items)
                per_feed[sid] = len(items)
        except Exception as e:
            print(f"WARN fetch {sid} failed: {e}", flush=True)
            per_feed[sid] = 0
            continue
    return collected, per_feed

def fetch_archive_for_chunk(cfrom, cto, config, session):
    throttle = config.get("throttle", {})
    timeout = int(throttle.get("timeout_s", 30))
    out = []
    arch_list = config.get("archive_sources", []) or []
    by_type = {a.get("type"): a for a in arch_list if a.get("enabled")}
    # HN Algolia по дням
    if "algolia" in by_type:
        cur = cfrom
        while cur <= cto:
            try:
                items = pipe.fetch_hn_algolia_day(cur.isoformat(), session, timeout)
                # фильтр точнее по чанку
                items = [x for x in items if x.get("published") and in_chunk(x["published"], cfrom, cto)]
                out.extend(items)
            except Exception as e:
                print(f"WARN hn_algolia {cur} failed: {e}", flush=True)
            cur += datetime.timedelta(days=1)
    # Reddit Arctic по сабам за чанк
    arc = None
    for a in arch_list:
        if a.get("type") == "arctic" and a.get("enabled"):
            arc = a
            break
    if arc:
        subs = arc.get("subs", []) or []
        after_iso = cfrom.isoformat()
        before_iso = (cto + datetime.timedelta(days=1)).isoformat()
        for sub in subs:
            try:
                items = pipe.fetch_arctic_shift(sub, after_iso, before_iso, session, timeout, limit=int(arc.get("limit", 100)))
                items = [x for x in items if (not x.get("published")) or in_chunk(x["published"], cfrom, cto)]
                # без даты — проставляем середину чанка
                for x in items:
                    if not x.get("published"):
                        x["published"] = cfrom.isoformat() + "T12:00:00Z"
                out.extend(items)
            except Exception as e:
                print(f"WARN arctic {sub} failed: {e}", flush=True)
            time.sleep(0.5)
    # arXiv OAI за чанк
    if "oai" in by_type:
        try:
            items = pipe.fetch_arxiv_oai(cfrom.isoformat(), cto.isoformat(), session, timeout)
            out.extend(items)
        except Exception as e:
            print(f"WARN arxiv_oai failed: {e}", flush=True)
    # producthunt rss как обычный rss, только свежие чанки
    for a in arch_list:
        if a.get("type") == "rss" and a.get("enabled") and a.get("feed_url"):
            today = datetime.date.today()
            if (today - cto).days > 45:
                continue
            try:
                raw, _ = pipe.fetch_feed_single(a["feed_url"], session, timeout)
                fake_src = {"id": a.get("id", "producthunt"), "name": a.get("name", "Product Hunt"), "lang": "en", "category": "tech"}
                for e in raw:
                    it = pipe.entry_to_item(e, fake_src)
                    if it and it.get("published") and in_chunk(it["published"], cfrom, cto):
                        out.append(it)
            except Exception as e:
                print(f"WARN {a.get('id')} rss failed: {e}", flush=True)
    return out

def main():
    ap = argparse.ArgumentParser(description="Backfill Horizon newspaper")
    ap.add_argument("--from", dest="date_from", required=True, help="YYYY-MM-DD")
    ap.add_argument("--to", dest="date_to", required=True, help="YYYY-MM-DD")
    ap.add_argument("--window", default="7d", help="e.g. 7d, 30d, 1w")
    ap.add_argument("--max-items", dest="max_items", type=int, default=200)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--config", default="config.json")
    ap.add_argument("--state", default="data/state.json")
    ap.add_argument("--out-dir", default="_posts")
    ap.add_argument("--sources", default="", help="comma-separated ids filter")
    ap.add_argument("--no-archive", action="store_true")
    args = ap.parse_args()

    dfrom = parse_ymd(args.date_from)
    dto = parse_ymd(args.date_to)
    if dto < dfrom:
        print("ERROR --to earlier than --from", flush=True)
        return 2
    delta = parse_window(args.window)
    chunks = split_range(dfrom, dto, delta)
    print(f"PARAM from={dfrom} to={dto} window={args.window} chunks={len(chunks)} max_items={args.max_items} dry_run={args.dry_run}", flush=True)

    config = load_config(args.config)
    state = state_mod.load_state(args.state)
    state["window"] = {"from": dfrom.isoformat(), "to": dto.isoformat()}

    ua = config.get("throttle", {}).get("user_agent") or pipe.BROWSER_UA
    session = pipe.make_session(ua)

    os.makedirs(args.out_dir, exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(args.state)) or ".", exist_ok=True)

    src_filter = set([s.strip() for s in args.sources.split(",") if s.strip()]) if args.sources else None
    sources = [s for s in config.get("sources", []) if (src_filter is None or s.get("id") in src_filter)]

    today = datetime.date.today()
    full_cache = {}
    total_new = 0
    total_dedup = 0

    for ci, (cfrom, cto) in enumerate(chunks, 1):
        print(f"CHUNK {ci}/{len(chunks)} {cfrom}..{cto}", flush=True)
        # FETCH RSS
        rss_items, per_feed = fetch_rss_for_chunk(sources, cfrom, cto, today, config, session, full_cache)
        pipe.stage_log("FETCH_RSS", len(sources), len(rss_items), f"chunk={cfrom}..{cto}")
        arch_items = []
        if not args.no_archive:
            arch_items = fetch_archive_for_chunk(cfrom, cto, config, session)
            pipe.stage_log("FETCH_ARCH", 3, len(arch_items), f"chunk={cfrom}..{cto}")
        all_fetched = rss_items + arch_items
        pipe.stage_log("FETCH", 0, len(all_fetched), f"rss={len(rss_items)} arch={len(arch_items)}")
        state_mod.bump_counter(state, "fetched_total", len(all_fetched))
        for sid, cnt in per_feed.items():
            fe = state_mod.ensure_feed(state, sid)
            fe["fetched_total"] = int(fe.get("fetched_total", 0)) + int(cnt)
            fe["cursor_paged"] = int(fe.get("cursor_paged", 0))
            if cnt > 0:
                fe["last_seen"] = cto.isoformat() + "T23:59:59Z"

        # DEDUP
        kept = []
        dropped = 0
        for it in all_fetched:
            if state_mod.is_duplicate(state, it.get("url_hash", ""), it.get("title_hash", "")):
                dropped += 1
            else:
                kept.append(it)
        # внутричанковый дедуп
        seen_u = set()
        seen_t = set()
        kept2 = []
        for it in kept:
            uh = it.get("url_hash", "")
            th = it.get("title_hash", "")
            if uh in seen_u or th in seen_t:
                dropped += 1
                continue
            seen_u.add(uh)
            seen_t.add(th)
            kept2.append(it)
        pipe.stage_log("DEDUP", len(all_fetched), len(kept2), f"dropped={dropped}")
        state_mod.bump_counter(state, "dedup_dropped_total", dropped)
        total_dedup += dropped

        # SELECT
        selected = pipe.select_top(kept2, args.max_items)
        pipe.stage_log("SELECT", len(kept2), len(selected), f"max={args.max_items}")
        state_mod.bump_counter(state, "selected_total", len(selected))

        if not selected:
            print(f"CHUNK {cfrom}..{cto} EMPTY selected=0", flush=True)
            state_mod.bump_counter(state, "windows_empty", 1)
            state_mod.save_state_atomic(args.state, state)
            continue

        # ENRICH
        if args.dry_run:
            for it in selected:
                pipe.extractive_fallback(it)
            pipe.stage_log("ENRICH", len(selected), 0, "dry_run=1 fallback_only")
            enriched = selected
        else:
            try:
                enriched = pipe.enrich_with_llm(selected, config, state, session)
                ok = sum(1 for x in enriched if x.get("enriched"))
                pipe.stage_log("ENRICH", len(selected), ok, f"tokens_used={state.get('budget',{}).get('tokens_used',0)}")
                state_mod.bump_counter(state, "enriched_total", ok)
            except pipe.DailyLimitExceeded as e:
                print(f"WARN DailyLimitExceeded: {e} — остаток fallback", flush=True)
                # enrich_with_llm уже добавил fallback для остатка перед raise, но для надёжности:
                enriched = []
                for it in selected:
                    if "title_ru" not in it:
                        pipe.extractive_fallback(it)
                    enriched.append(it)
                pipe.stage_log("ENRICH", len(selected), 0, "fuse_fallback")
            except Exception as e:
                print(f"WARN enrich failed: {e} — fallback", flush=True)
                enriched = [pipe.extractive_fallback(x) if "title_ru" not in x else x for x in selected]
                pipe.stage_log("ENRICH", len(selected), 0, "error_fallback")

        # PUBLISH по дням
        by_day = {}
        for it in enriched:
            d = day_of_item(it, cfrom.isoformat())
            # clamp к чанку
            try:
                dd = datetime.date.fromisoformat(d)
                if dd < cfrom or dd > cto:
                    d = cfrom.isoformat()
            except Exception:
                d = cfrom.isoformat()
            by_day.setdefault(d, []).append(it)
        chunk_new = 0
        for day_iso in sorted(by_day.keys()):
            path, fresh_cnt, _ = render_day_file(day_iso, by_day[day_iso], args.out_dir)
            chunk_new += fresh_cnt
            # маркируем только реально свежие (по хэшам файла)
            for it in by_day[day_iso]:
                # проверяем что хэш теперь в файле (fresh) — маркируем все selected во избежание вечных повторов
                state_mod.mark_published(state, it.get("url_hash", ""), it.get("title_hash", ""), day_iso)
                fe = state_mod.ensure_feed(state, it.get("source_id", "unknown"))
                fe["published_total"] = int(fe.get("published_total", 0)) + (1 if fresh_cnt > 0 else 0)
            print(f"PUBLISH day={day_iso} file={path} fresh={fresh_cnt} tried={len(by_day[day_iso])}", flush=True)
        pipe.stage_log("PUBLISH", len(enriched), chunk_new, f"days={len(by_day)}")
        state_mod.bump_counter(state, "published_total", chunk_new)
        state_mod.bump_counter(state, "windows_done", 1)
        # archive курсоры
        try:
            state["archive_cursors"]["hn_algolia"]["last_day_done"] = cto.isoformat()
            state["archive_cursors"]["reddit_arctic"]["last_day_done"] = cto.isoformat()
            state["archive_cursors"]["arxiv_oai"]["last_day_done"] = cto.isoformat()
        except Exception:
            pass
        update_index(args.out_dir, state)
        state_mod.save_state_atomic(args.state, state)
        total_new += chunk_new
        # троттлинг между чанками
        time.sleep(1.0)

    pipe.stage_log("RESULT", len(chunks), total_new, f"dedup_dropped={total_dedup}")
    print(f"DONE total_new={total_new} dedup_dropped={total_dedup} dry_run={args.dry_run}", flush=True)
    if total_new == 0:
        print("EXIT 1: за окно 0 материалов (все дубли или пусто)", flush=True)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())