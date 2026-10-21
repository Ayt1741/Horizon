#!/usr/bin/env python3
"""pipeline.py — разбор RSS, архивные API, скоринг, LLM-обогащение с fuse."""
import re
import json
import time
import hashlib
import calendar
import html as htmlmod
import urllib.parse
import datetime
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

import requests
import feedparser

BROWSER_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
TRACKING_PARAMS = {"utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "fbclid", "gclid", "yclid", "mc_cid", "mc_eid"}

class DailyLimitExceeded(Exception):
    pass

def stage_log(stage, in_n, out_n, extra=""):
    msg = f"STAGE={stage} IN={in_n} OUT={out_n}"
    if extra:
        msg += f" {extra}"
    print(msg, flush=True)

def sha256_hex(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def normalize_url(url):
    url = (url or "").strip()
    if not url:
        return ""
    try:
        p = urllib.parse.urlsplit(url)
        scheme = (p.scheme or "https").lower()
        netloc = p.netloc.lower()
        if netloc.startswith("www."):
            pass
        path = p.path or "/"
        if len(path) > 1 and path.endswith("/"):
            path = path[:-1]
        q = urllib.parse.parse_qsl(p.query, keep_blank_values=True)
        q2 = [(k, v) for k, v in q if k not in TRACKING_PARAMS and not k.startswith("utm_")]
        q2.sort()
        query = urllib.parse.urlencode(q2)
        rebuilt = urllib.parse.urlunsplit((scheme, netloc, path, query, ""))
        return rebuilt
    except Exception:
        return url.split("#")[0].strip()

def norm_title(t):
    t = (t or "").strip().lower()
    t = re.sub(r"\s+", " ", t)
    return t

def title_hash(title):
    return sha256_hex(norm_title(title))

def url_hash(nurl):
    return sha256_hex(nurl)

def strip_html(h):
    if not h:
        return ""
    h = re.sub(r"<script.*?</script>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<style.*?</style>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<[^>]+>", " ", h)
    h = htmlmod.unescape(h)
    h = re.sub(r"\s+", " ", h).strip()
    return h

def entry_pubdate_to_iso(entry):
    dt = None
    for k in ("published_parsed", "updated_parsed", "created_parsed"):
        v = entry.get(k)
        if v:
            try:
                ts = calendar.timegm(v)
                dt = datetime.datetime.fromtimestamp(ts, tz=datetime.timezone.utc)
                break
            except Exception:
                continue
    if dt is None:
        for k in ("published", "updated", "created"):
            v = entry.get(k)
            if v:
                try:
                    d2 = parsedate_to_datetime(v)
                    if d2.tzinfo is None:
                        d2 = d2.replace(tzinfo=datetime.timezone.utc)
                    dt = d2.astimezone(datetime.timezone.utc)
                    break
                except Exception:
                    continue
    if dt is None:
        return None
    return dt.isoformat().replace("+00:00", "Z")

def entry_to_item(entry, source):
    link = (entry.get("link") or "").strip()
    title = (entry.get("title") or "").strip()
    if not link or not title:
        return None
    iso = entry_pubdate_to_iso(entry)
    summary_html = entry.get("summary", "") or entry.get("description", "") or ""
    content_html = summary_html
    content_text = ""
    try:
        if "content" in entry and entry["content"]:
            c0 = entry["content"][0]
            if isinstance(c0, dict):
                content_html = c0.get("value", "") or summary_html
    except Exception:
        pass
    summary_text = strip_html(summary_html)[:4000]
    content_text = strip_html(content_html)[:8000]
    nurl = normalize_url(link)
    return {
        "url": link,
        "url_norm": nurl,
        "url_hash": url_hash(nurl) if nurl else "",
        "title": title,
        "title_hash": title_hash(title),
        "published": iso,
        "source_id": source.get("id", ""),
        "source_name": source.get("name", ""),
        "lang": source.get("lang", ""),
        "category": source.get("category", ""),
        "summary": summary_text,
        "content": content_text,
        "score": 0.0
    }

def make_session(user_agent, timeout_s=30):
    s = requests.Session()
    s.headers.update({"User-Agent": user_agent or BROWSER_UA, "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*"})
    return s

def http_get(session, url, timeout, max_retries=3, backoff=(2, 6, 18), extra_headers=None):
    last_err = None
    for attempt in range(max_retries + 1):
        try:
            r = session.get(url, timeout=timeout, headers=extra_headers or {})
            if r.status_code == 429 or 500 <= r.status_code <= 599:
                last_err = RuntimeError(f"HTTP {r.status_code} for {url}")
                if attempt < max_retries:
                    time.sleep(backoff[min(attempt, len(backoff) - 1)])
                    continue
                r.raise_for_status()
            return r
        except Exception as e:
            last_err = e
            if attempt < max_retries:
                time.sleep(backoff[min(attempt, len(backoff) - 1)])
                continue
            raise last_err

def fetch_feed_single(feed_url, session, timeout):
    r = http_get(session, feed_url, timeout)
    data = r.content
    parsed = feedparser.parse(data)
    entries = parsed.get("entries", []) if isinstance(parsed, dict) else getattr(parsed, "entries", [])
    info = {"status": r.status_code, "etag": r.headers.get("ETag"), "last_modified": r.headers.get("Last-Modified"), "bozo": bool(getattr(parsed, "bozo", False))}
    return entries, info

def wp_paged_url(base, n):
    sep = "&" if "?" in base else "?"
    return f"{base}{sep}paged={n}"

def fetch_wp_paginated(base_url, session, timeout, max_pages, delay_s):
    all_entries = []
    seen = set()
    for page in range(1, max_pages + 1):
        url = base_url if page == 1 else wp_paged_url(base_url, page)
        try:
            entries, _ = fetch_feed_single(url, session, timeout)
        except Exception:
            break
        if not entries:
            break
        new_count = 0
        for e in entries:
            link = normalize_url(e.get("link", ""))
            h = sha256_hex(link) if link else sha256_hex(e.get("title", "") + str(e.get("published", "")))
            if h not in seen:
                seen.add(h)
                all_entries.append(e)
                new_count += 1
        if new_count == 0:
            break
        if delay_s > 0:
            time.sleep(delay_s)
        if len(entries) < 3:
            # вероятно хвост архива
            pass
    return all_entries

def fetch_devto_paginated(session, timeout, max_pages, delay_s):
    out = []
    for page in range(1, max_pages + 1):
        url = f"https://dev.to/api/articles?page={page}&per_page=100"
        try:
            r = http_get(session, url, timeout)
            arr = r.json()
        except Exception:
            break
        if not isinstance(arr, list) or not arr:
            break
        for a in arr:
            try:
                link = a.get("url", "")
                title = a.get("title", "")
                if not link or not title:
                    continue
                iso = a.get("published_at", "")
                try:
                    dt = datetime.datetime.fromisoformat(iso.replace("Z", "+00:00"))
                    iso_z = dt.astimezone(datetime.timezone.utc).isoformat().replace("+00:00", "Z")
                except Exception:
                    iso_z = None
                nurl = normalize_url(link)
                out.append({
                    "url": link, "url_norm": nurl, "url_hash": url_hash(nurl),
                    "title": title, "title_hash": title_hash(title),
                    "published": iso_z, "source_id": "devto", "source_name": "DEV.to",
                    "lang": "en", "category": "dev",
                    "summary": strip_html(a.get("description", "") or "")[:4000],
                    "content": strip_html(a.get("description", "") or "")[:8000],
                    "score": 0.0
                })
            except Exception:
                continue
        if delay_s > 0:
            time.sleep(delay_s)
        if len(arr) < 100:
            break
    return out

def fetch_hn_algolia_day(day_iso, session, timeout):
    day = datetime.date.fromisoformat(day_iso)
    start = int(datetime.datetime(day.year, day.month, day.day, 0, 0, 0, tzinfo=datetime.timezone.utc).timestamp())
    end = int(datetime.datetime(day.year, day.month, day.day, 23, 59, 59, tzinfo=datetime.timezone.utc).timestamp())
    items = []
    for page in range(0, 10):
        url = f"https://hn.algolia.com/api/v1/search_by_date?tags=story&numericFilters=created_at_i%3E{start},created_at_i%3C{end}&hitsPerPage=100&page={page}"
        try:
            r = http_get(session, url, timeout)
            j = r.json()
        except Exception:
            break
        hits = j.get("hits", []) if isinstance(j, dict) else []
        if not hits:
            break
        for h in hits:
            try:
                oid = h.get("objectID", "")
                link = h.get("url") or f"https://news.ycombinator.com/item?id={oid}"
                title = h.get("title", "") or ""
                if not title:
                    continue
                created = h.get("created_at", "")
                try:
                    dt = datetime.datetime.fromisoformat(created.replace("Z", "+00:00"))
                    iso_z = dt.astimezone(datetime.timezone.utc).isoformat().replace("+00:00", "Z")
                except Exception:
                    iso_z = f"{day_iso}T12:00:00Z"
                nurl = normalize_url(link)
                pts = h.get("points", 0) or 0
                comments = h.get("num_comments", 0) or 0
                summ = f"HN points={pts} comments={comments} author={h.get('author','')}".strip()
                items.append({
                    "url": link, "url_norm": nurl, "url_hash": url_hash(nurl),
                    "title": title, "title_hash": title_hash(title),
                    "published": iso_z, "source_id": "hn_algolia", "source_name": "Hacker News",
                    "lang": "en", "category": "tech",
                    "summary": summ[:2000], "content": summ[:2000], "score": 0.0,
                    "hn_points": pts, "hn_comments": comments
                })
            except Exception:
                continue
        if len(hits) < 100:
            break
        time.sleep(0.6)
    return items

def fetch_arctic_shift(subreddit, after_iso, before_iso, session, timeout, limit=100):
    url = f"https://arctic-shift.photon-reddit.com/api/posts/search?subreddit={subreddit}&after={after_iso}&before={before_iso}&limit={limit}"
    try:
        r = http_get(session, url, timeout)
        j = r.json()
    except Exception:
        return []
    arr = []
    if isinstance(j, dict):
        arr = j.get("data", []) or j.get("posts", []) or []
    elif isinstance(j, list):
        arr = j
    items = []
    for p in arr:
        try:
            title = p.get("title", "") or ""
            permalink = p.get("permalink", "") or ""
            link = f"https://www.reddit.com{permalink}" if permalink else p.get("url", "")
            if not title or not link:
                continue
            created = p.get("created_utc") or p.get("created_at")
            iso_z = None
            try:
                if isinstance(created, (int, float)):
                    iso_z = datetime.datetime.fromtimestamp(int(created), tz=datetime.timezone.utc).isoformat().replace("+00:00", "Z")
                elif isinstance(created, str):
                    if "T" in created:
                        dt = datetime.datetime.fromisoformat(created.replace("Z", "+00:00"))
                        iso_z = dt.astimezone(datetime.timezone.utc).isoformat().replace("+00:00", "Z")
            except Exception:
                iso_z = None
            nurl = normalize_url(link)
            body = (p.get("selftext", "") or p.get("body", "") or "")[:3000]
            items.append({
                "url": link, "url_norm": nurl, "url_hash": url_hash(nurl),
                "title": f"[r/{subreddit}] {title}"[:300], "title_hash": title_hash(title + subreddit),
                "published": iso_z, "source_id": f"reddit_{subreddit.lower()}", "source_name": f"Reddit r/{subreddit}",
                "lang": "en", "category": "tech",
                "summary": strip_html(body)[:3000] if body else f"score={p.get('score',0)} comments={p.get('num_comments',0)}",
                "content": strip_html(body)[:6000], "score": 0.0
            })
        except Exception:
            continue
    return items

def fetch_arxiv_oai(from_ymd, until_ymd, session, timeout, max_iters=12):
    items = []
    base = "https://export.arxiv.org/oai2"
    params = f"?verb=ListRecords&metadataPrefix=arXiv&from={from_ymd}&until={until_ymd}"
    url = base + params
    it = 0
    while url and it < max_iters:
        it += 1
        try:
            r = http_get(session, url, timeout)
            root = ET.fromstring(r.content)
        except Exception:
            break
        ns = {"oai": "http://www.openarchives.org/OAI/2.0/", "ax": "http://arxiv.org/OAI/arXiv/"}
        for rec in root.findall(".//oai:record", ns):
            try:
                meta = rec.find("oai:metadata/ax:arXiv", ns)
                if meta is None:
                    continue
                aid = (meta.findtext("ax:id", default="", namespaces=ns) or "").strip()
                title = (meta.findtext("ax:title", default="", namespaces=ns) or "").strip()
                title = re.sub(r"\s+", " ", title)
                abst = (meta.findtext("ax:abstract", default="", namespaces=ns) or "").strip()
                abst = re.sub(r"\s+", " ", abst)
                created = (meta.findtext("ax:created", default="", namespaces=ns) or "").strip()
                iso_z = None
                try:
                    if created:
                        dt = datetime.datetime.strptime(created[:10], "%Y-%m-%d").replace(tzinfo=datetime.timezone.utc)
                        iso_z = dt.isoformat().replace("+00:00", "Z")
                except Exception:
                    iso_z = None
                if not aid or not title:
                    continue
                link = f"https://arxiv.org/abs/{aid}"
                nurl = normalize_url(link)
                items.append({
                    "url": link, "url_norm": nurl, "url_hash": url_hash(nurl),
                    "title": title[:300], "title_hash": title_hash(title),
                    "published": iso_z or f"{from_ymd}T12:00:00Z",
                    "source_id": "arxiv_oai", "source_name": "arXiv",
                    "lang": "en", "category": "science",
                    "summary": abst[:3500], "content": abst[:7000], "score": 0.0
                })
            except Exception:
                continue
        tok_el = root.find(".//oai:resumptionToken", ns)
        tok = (tok_el.text or "").strip() if tok_el is not None and tok_el.text else ""
        if tok:
            url = f"{base}?verb=ListRecords&resumptionToken={urllib.parse.quote(tok)}"
            time.sleep(1.0)
        else:
            break
    return items

KEYWORDS = ["ai", "llm", "gpt", "transformer", "diffusion", "agent", "copilot", "python", "rust", "kubernetes", "spacex", "nasa", "quantum", "fusion", "mrna", "vaccine", "chip", "gpu", "nvidia", "openai", "mistral", "bitcoin", "ethereum", "ии", "нейросеть", "космос", "ракета", "спутник", "вакцина", "климат", "ядерн", "солнечн", "батарея"]

def score_relevance(item):
    s = 0.45
    title = (item.get("title") or "").lower()
    summ = (item.get("summary") or "").lower()
    blob = f"{title} {summ}"
    text_len = len(item.get("content") or "") + len(item.get("summary") or "")
    if text_len > 800:
        s += 0.12
    elif text_len > 300:
        s += 0.07
    tlen = len(item.get("title") or "")
    if 25 <= tlen <= 140:
        s += 0.05
    cat = (item.get("category") or "").lower()
    if cat in ("ai", "tech", "science", "dev", "space"):
        s += 0.08
    hits = 0
    for kw in KEYWORDS:
        if kw in blob:
            hits += 1
            if hits >= 8:
                break
    s += min(0.20, hits * 0.025)
    if item.get("source_id") == "hn_algolia":
        try:
            pts = int(item.get("hn_points", 0) or 0)
            if pts >= 200:
                s += 0.10
            elif pts >= 50:
                s += 0.05
        except Exception:
            pass
    if s > 0.99:
        s = 0.99
    if s < 0.01:
        s = 0.01
    return round(float(s), 4)

def select_top(items, max_items):
    for it in items:
        try:
            it["score"] = score_relevance(it)
        except Exception:
            it["score"] = 0.5
    items_sorted = sorted(items, key=lambda x: (x.get("score", 0), x.get("published") or ""), reverse=True)
    return items_sorted[:max_items]

def estimate_tokens(text):
    if not text:
        return 8
    return max(8, len(text) // 4)

def extractive_fallback(item):
    title = item.get("title", "")
    summ = item.get("summary") or item.get("content") or title
    summ = strip_html(summ)
    parts = re.split(r"(?<=[.!?])\s+", summ)
    short = " ".join(parts[:2])[:700] if parts else summ[:700]
    if len(short) < 140:
        short = (summ[:600] + ("..." if len(summ) > 600 else ""))
    item["title_ru"] = title
    item["summary_ru"] = short
    item["bullets"] = []
    item["enriched"] = False
    item["tokens_used"] = 0
    return item

def call_mistral(prompt, config, session):
    provider = config.get("provider", {})
    base_url = provider.get("base_url", "https://api.mistral.ai/v1/chat/completions")
    model = provider.get("model", "mistral-small-latest")
    timeout_s = int(provider.get("timeout_s", 60))
    api_key = ""
    env_name = provider.get("api_key_env", "MISTRAL_API_KEY")
    import os as _os
    api_key = _os.environ.get(env_name, "") or _os.environ.get("MISTRAL_API_KEY", "")
    if not api_key:
        raise RuntimeError("missing_api_key")
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    body = {
        "model": model,
        "temperature": 0.2,
        "max_tokens": int(config.get("limits", {}).get("max_tokens_per_item", 800)),
        "messages": [
            {"role": "system", "content": "Ты редактор русской новостной газеты. Отвечай строго JSON без пояснений."},
            {"role": "user", "content": prompt}
        ]
    }
    r = session.post(base_url, headers=headers, json=body, timeout=timeout_s)
    return r

def enrich_with_llm(items, config, state, session):
    import state as state_mod
    limits = config.get("limits", {})
    daily_limit = int(limits.get("daily_token_limit", 30000))
    provider = config.get("provider", {})
    backoff = provider.get("backoff_s", [5, 20, 60])
    max_retries = int(provider.get("max_retries", 3))
    enriched = []
    for idx, it in enumerate(items):
        title = it.get("title", "")[:300]
        src = it.get("source_name", "")
        txt = (it.get("summary") or it.get("content") or "")[:2200]
        prompt = (
            f"Заголовок: {title}\nИсточник: {src}\nТекст: {txt}\n\n"
            "Сделай на русском JSON: {\"title_ru\": \"перевод/пересказ заголовка\", "
            "\"summary_ru\": \"2-3 предложения сути, 300-600 символов\", "
            "\"bullets\": [\"факт 1\", \"факт 2\", \"факт 3\"]}. "
            "Только JSON, без markdown."
        )
        need = estimate_tokens(prompt) + 500
        state_mod.budget_reset_if_new_day(state)
        used = state.get("budget", {}).get("tokens_used", 0)
        if used + need > daily_limit:
            stage_log("ENRICH", len(items), len(enriched), f"fuse_hit used={used} limit={daily_limit} remaining_fallback={len(items)-idx}")
            for rest in items[idx:]:
                enriched.append(extractive_fallback(rest))
            raise DailyLimitExceeded(f"daily fuse {used}/{daily_limit}")
        try:
            resp = None
            for attempt in range(max_retries + 1):
                try:
                    resp = call_mistral(prompt, config, session)
                except RuntimeError as e:
                    if str(e) == "missing_api_key":
                        resp = None
                        break
                    raise
                if resp is None:
                    break
                if resp.status_code == 200:
                    break
                body_txt = ""
                try:
                    body_txt = resp.text[:2000].lower()
                except Exception:
                    pass
                if resp.status_code == 429 and ("tokens per day" in body_txt or "daily" in body_txt or "quota" in body_txt):
                    raise DailyLimitExceeded(f"429 daily: {body_txt[:300]}")
                if resp.status_code == 429 or 500 <= resp.status_code <= 599:
                    if attempt < max_retries:
                        wait = backoff[min(attempt, len(backoff) - 1)]
                        try:
                            ra = resp.headers.get("Retry-After")
                            if ra and str(ra).isdigit():
                                wait = max(wait, int(ra))
                        except Exception:
                            pass
                        time.sleep(wait)
                        continue
                    else:
                        break
                else:
                    break
            if resp is None or resp.status_code != 200:
                enriched.append(extractive_fallback(it))
                stage_log("ENRICH", 1, 0, f"fallback status={resp.status_code if resp is not None else 'no_key'} title={(title[:60])}")
                continue
            try:
                j = resp.json()
                content = j["choices"][0]["message"]["content"]
            except Exception:
                enriched.append(extractive_fallback(it))
                continue
            parsed_ok = False
            try:
                m = re.search(r"\{.*\}", content, flags=re.S)
                js = json.loads(m.group(0) if m else content)
                it["title_ru"] = str(js.get("title_ru", title))[:300]
                it["summary_ru"] = str(js.get("summary_ru", ""))[:1200] or extractive_fallback(dict(it))["summary_ru"]
                b = js.get("bullets", [])
                if isinstance(b, list):
                    it["bullets"] = [str(x)[:300] for x in b[:5]]
                else:
                    it["bullets"] = []
                parsed_ok = True
            except Exception:
                it["title_ru"] = title
                it["summary_ru"] = strip_html(content)[:800]
                it["bullets"] = []
            it["enriched"] = parsed_ok
            tok = estimate_tokens(prompt) + estimate_tokens(content)
            it["tokens_used"] = tok
            state_mod.budget_add(state, tok)
            enriched.append(it)
            time.sleep(0.4)
        except DailyLimitExceeded:
            raise
        except Exception:
            enriched.append(extractive_fallback(it))
            continue
    return enriched