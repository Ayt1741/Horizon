#!/usr/bin/env python3
"""state.py — атомарное состояние бэкфилла, миграции, дедуп, бюджет."""
import json
import os
import tempfile
import datetime

STATE_VERSION = 3

def utc_today_str():
    return datetime.datetime.now(datetime.timezone.utc).date().isoformat()

def default_state():
    return {
        "version": STATE_VERSION,
        "window": {"from": None, "to": None},
        "feeds": {},
        "archive_cursors": {
            "hn_algolia": {"last_day_done": None},
            "reddit_arctic": {"last_day_done": None},
            "arxiv_oai": {"last_day_done": None, "resumption": None}
        },
        "published_url_hash": {},
        "published_title_hash": {},
        "daily_counts": {},
        "budget": {"date": utc_today_str(), "tokens_used": 0},
        "counters": {
            "fetched_total": 0,
            "dedup_dropped_total": 0,
            "selected_total": 0,
            "enriched_total": 0,
            "published_total": 0,
            "windows_done": 0,
            "windows_empty": 0
        }
    }

def migrate_state(s):
    if not isinstance(s, dict):
        return default_state()
    if "version" not in s:
        s["version"] = 1
    if s["version"] == 1:
        s.setdefault("feeds", {})
        s.setdefault("published_url_hash", {})
        s.setdefault("published_title_hash", {})
        s.setdefault("daily_counts", {})
        s.setdefault("budget", {"date": utc_today_str(), "tokens_used": 0})
        s.setdefault("counters", {})
        s.setdefault("window", {"from": None, "to": None})
        s.setdefault("archive_cursors", {})
        s["version"] = 2
    if s["version"] == 2:
        s.setdefault("archive_cursors", {})
        for k in ("hn_algolia", "reddit_arctic", "arxiv_oai"):
            if k not in s["archive_cursors"]:
                s["archive_cursors"][k] = {"last_day_done": None}
        if "resumption" not in s["archive_cursors"].get("arxiv_oai", {}):
            s["archive_cursors"]["arxiv_oai"]["resumption"] = None
        c = s.get("counters", {})
        for kk, vv in default_state()["counters"].items():
            c.setdefault(kk, vv)
        s["counters"] = c
        s["version"] = 3
    # гарантия полей
    d = default_state()
    for k, v in d.items():
        if k not in s:
            s[k] = v
    if not isinstance(s.get("budget"), dict):
        s["budget"] = d["budget"]
    s["budget"].setdefault("date", utc_today_str())
    s["budget"].setdefault("tokens_used", 0)
    return s

def load_state(path):
    if not os.path.exists(path):
        return default_state()
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return migrate_state(data)

def save_state_atomic(path, state):
    state["version"] = STATE_VERSION
    directory = os.path.dirname(os.path.abspath(path)) or "."
    os.makedirs(directory, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=directory, prefix=".state.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2, sort_keys=True)
            f.write("\n")
            f.flush()
            try:
                os.fsync(f.fileno())
            except Exception:
                pass
        os.replace(tmp, path)
    except Exception:
        try:
            if os.path.exists(tmp):
                os.unlink(tmp)
        except Exception:
            pass
        raise

def ensure_feed(state, feed_id):
    feeds = state.setdefault("feeds", {})
    if feed_id not in feeds:
        feeds[feed_id] = {
            "cursor_paged": 0,
            "last_seen": None,
            "etag": None,
            "last_modified": None,
            "fetched_total": 0,
            "published_total": 0,
            "completed": False
        }
    return feeds[feed_id]

def is_duplicate(state, url_hash, title_hash):
    if not url_hash and not title_hash:
        return True
    puh = state.get("published_url_hash", {})
    pth = state.get("published_title_hash", {})
    if url_hash and url_hash in puh:
        return True
    if title_hash and title_hash in pth:
        return True
    return False

def mark_published(state, url_hash, title_hash, day_iso):
    if url_hash:
        state["published_url_hash"][url_hash] = day_iso
    if title_hash:
        state["published_title_hash"][title_hash] = day_iso
    dc = state.setdefault("daily_counts", {})
    dc[day_iso] = dc.get(day_iso, 0) + 1

def budget_reset_if_new_day(state):
    today = utc_today_str()
    b = state.setdefault("budget", {"date": today, "tokens_used": 0})
    if b.get("date") != today:
        b["date"] = today
        b["tokens_used"] = 0
    return b

def budget_can_spend(state, need_tokens, daily_limit):
    b = budget_reset_if_new_day(state)
    return (b.get("tokens_used", 0) + need_tokens) <= daily_limit

def budget_add(state, used_tokens):
    b = budget_reset_if_new_day(state)
    b["tokens_used"] = int(b.get("tokens_used", 0)) + int(used_tokens)
    return b["tokens_used"]

def bump_counter(state, key, delta=1):
    c = state.setdefault("counters", {})
    c[key] = int(c.get(key, 0)) + int(delta)