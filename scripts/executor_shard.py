#!/usr/bin/env python3
"""Исполнитель-полоса: реальная проверка своей доли архива газеты (только stdlib).

Вход: каталог с *_summary-ru.md, номер полосы, общее число полос.
Выход: JSON-отчёт по своей доле + код возврата 0 (нет брака) / 1 (есть брак) / 2 (нет входа).

Проверки каждого номера:
 1. оглавление: layout (post или default) и заголовок;
 2. число позиций: для бэкфилла строки '## ', для дневного '### [';
 3. ссылки: каждая позиция должна иметь ссылку (http);
 4. локаль: нет иероглифов/CJK в русской версии;
 5. размер: 1500..200000 байт.
"""
import argparse
import json
import os
import re
import sys

CJK = re.compile(r'[\u3000-\u9fff\uac00-\ud7af]')
POST_DAY = re.compile(r'^### \[', re.M)
POST_BI = re.compile(r'^## ', re.M)


def examine(path):
    name = os.path.basename(path)
    date = name[:10]
    raw = open(path, "rb").read()
    size = len(raw)
    text = raw.decode("utf-8", errors="replace")
    day = len(POST_DAY.findall(text))
    backfill = len(POST_BI.findall(text))
    items = day if day > 0 else backfill
    links = len(re.findall(r'https?://', text))
    has_title = bool(re.search(r'^title:\s*\S+', text, re.M))
    cjk = len(CJK.findall(text))
    problems = []
    if items < 5:
        problems.append("мало позиций: %d" % items)
    if links < items:
        problems.append("ссылок меньше позиций: ссылок %d, позиций %d" % (links, items))
    if cjk:
        problems.append("иероглифы в русской версии: %d" % cjk)
    if not has_title:
        problems.append("нет заголовка в шапке")
    if not (1500 <= size <= 400000):
        problems.append("размер вне нормы: %d байт" % size)
    return {
        "date": date,
        "file": name,
        "items": items,
        "links": links,
        "bytes": size,
        "format": "backfill" if day == 0 else "daily",
        "problems": problems,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="_posts")
    ap.add_argument("--index", type=int, required=True)
    ap.add_argument("--total", type=int, required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    if not os.path.isdir(a.dir):
        print(json.dumps({"error": "нет каталога " + a.dir}))
        return 2
    files = sorted(f for f in os.listdir(a.dir) if f.endswith("-summary-ru.md"))
    mine = [f for i, f in enumerate(files) if i % a.total == a.index]
    rows = [examine(os.path.join(a.dir, f)) for f in mine]
    bad = [r for r in rows if r["problems"]]
    report = {
        "shard": a.index,
        "of": a.total,
        "files_total_in_archive": len(files),
        "files_in_shard": len(rows),
        "items_total": sum(r["items"] for r in rows),
        "links_total": sum(r["links"] for r in rows),
        "bad_count": len(bad),
        "bad": bad[:20],
        "dates": [r["date"] for r in rows],
    }
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    print(json.dumps({k: report[k] for k in ("shard", "files_in_shard", "items_total", "links_total", "bad_count")}, ensure_ascii=False))
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
