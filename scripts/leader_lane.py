#!/usr/bin/env python3
"""Полоса руководителя: каждый из 10 делает свою настоящую проверку архива газеты.
Только stdlib. Код возврата: 0 — работа сделана, 2 — нет входа.
"""
import argparse
import hashlib
import json
import os
import re
import statistics
import sys

CJK = re.compile(r'[\u3000-\u9fff\uac00-\ud7af]')
DAY = re.compile(r'^### \[', re.M)
BI = re.compile(r'^## ', re.M)
LINK = re.compile(r'https?://')
TITLE = re.compile(r'^title:\s*(.+)$', re.M)


LANGS = ("ru", "en")


def load(folder):
    """Читает выпуски ОБОИХ языков: ru и en.

    Раньше здесь был только "-summary-ru.md", поэтому полоса руководителя физически
    не могла увидеть брак в английском выпуске (иероглифы в en-выпуске 21-22.10.2026
    прошли 10 проверок незамеченными). Теперь каждый файл несёт поле lang.
    """
    out = []
    for name in sorted(os.listdir(folder)):
        lang = next((l for l in LANGS if name.endswith("-summary-%s.md" % l)), None)
        if lang is None:
            continue
        raw = open(os.path.join(folder, name), "rb").read()
        text = raw.decode("utf-8", errors="replace")
        day = len(DAY.findall(text))
        back = len(BI.findall(text))
        m = TITLE.search(text)
        out.append({"date": name[:10], "file": name, "lang": lang, "bytes": len(raw),
                    "items": day if day else back, "links": len(LINK.findall(text)),
                    "cjk": len(CJK.findall(text)), "format": "daily" if day else "backfill",
                    "title": (m.group(1).strip() if m else "")})
    return out


def lane(lid, rows):
    by_year = {}
    for r in rows:
        by_year.setdefault(r["date"][:4], []).append(r)

    if lid == "L1":
        cov = {}
        for year, rs in sorted(by_year.items()):
            months = {}
            for r in rs:
                months[r["date"][:7]] = months.get(r["date"][:7], 0) + 1
            cov[year] = {"days": len(rs), "months": dict(sorted(months.items()))}
        return {"metric": "покрытие по годам и месяцам", "coverage": cov}
    if lid == "L2":
        bad = [r for r in by_year.get("2024", []) if r["items"] < 5]
        return {"metric": "качество 2024", "files": len(by_year.get("2024", [])),
                "thin": len(bad), "thin_dates": [r["date"] for r in bad]}
    if lid == "L3":
        bad = [r for r in by_year.get("2025", []) if r["items"] < 5]
        return {"metric": "качество 2025", "files": len(by_year.get("2025", [])),
                "thin": len(bad), "thin_dates": [r["date"] for r in bad]}
    if lid == "L4":
        bad = [r for r in by_year.get("2026", []) if r["items"] < 5]
        months = sorted({r["date"][:7] for r in by_year.get("2026", [])})
        allm = ["2026-%02d" % m for m in range(1, 11)]
        return {"metric": "качество 2026", "files": len(by_year.get("2026", [])),
                "thin": len(bad), "thin_dates": [r["date"] for r in bad],
                "months_present": months,
                "months_missing": [m for m in allm if m not in months]}
    if lid == "L5":
        bad = [r for r in rows if r["cjk"] > 0]
        return {"metric": "локаль: иероглифы в русской версии", "files": len(bad),
                "hits": [{"date": r["date"], "cjk": r["cjk"]} for r in bad]}
    if lid == "L6":
        seen = {}
        for r in rows:
            key = hashlib.sha256(re.sub(r'\W+', '', r["title"].lower()).encode()).hexdigest()[:12]
            seen.setdefault(key, []).append(r["date"])
        dups = {k: v for k, v in seen.items() if len(v) > 1}
        return {"metric": "дубли заголовков", "groups": len(dups), "examples": list(dups.values())[:15]}
    if lid == "L7":
        sizes = [r["bytes"] for r in rows]
        thin = [r for r in rows if r["bytes"] < 1500]
        return {"metric": "размеры номеров", "min": min(sizes), "max": max(sizes),
                "median": int(statistics.median(sizes)), "under_1500": len(thin),
                "under_1500_dates": [r["date"] for r in thin]}
    if lid == "L8":
        short = [r for r in rows if r["links"] < r["items"]]
        return {"metric": "ссылки: меньше, чем позиций", "files": len(short),
                "dates": [r["date"] for r in short]}
    if lid == "L9":
        daily = sum(1 for r in rows if r["format"] == "daily")
        back = sum(1 for r in rows if r["format"] == "backfill")
        return {"metric": "формат номеров", "daily": daily, "backfill": back,
                "backfill_dates_sample": [r["date"] for r in rows if r["format"] == "backfill"][:20]}
    if lid == "L10":
        return {"metric": "сводка журнала", "files": len(rows),
                "items_total": sum(r["items"] for r in rows),
                "links_total": sum(r["links"] for r in rows),
                "years": {y: len(rs) for y, rs in sorted(by_year.items())},
                "source": "https://github.com/Ayt1741/Horizon/tree/gh-pages/_posts",
                "date": "2026-10-21"}
    return {"error": "unknown leader"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True)
    ap.add_argument("--dir", default="_posts")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    if not os.path.isdir(a.dir):
        print(json.dumps({"error": "нет каталога " + a.dir}))
        return 2
    rows = load(a.dir)
    res = lane(a.id, rows)
    res["leader"] = a.id
    res["files_in_archive"] = len(rows)
    res["generated"] = "2026-10-21"
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    print(json.dumps({"leader": a.id, "metric": res.get("metric"), "files": len(rows)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
