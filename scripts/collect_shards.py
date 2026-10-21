#!/usr/bin/env python3
"""Сборка отчётов 30 полос в один итог (только stdlib)."""
import json
import os
import sys


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "artifacts"
    rows = []
    for dirpath, _dirs, files in os.walk(root):
        for name in files:
            if not name.endswith(".json"):
                continue
            try:
                with open(os.path.join(dirpath, name), encoding="utf-8") as f:
                    rows.append(json.load(f))
            except (OSError, ValueError):
                continue
    rows.sort(key=lambda r: r.get("shard", 0))
    bad = [b for r in rows for b in r.get("bad", [])]
    summary = {
        "shards_expected": 30,
        "shards_returned": len(rows),
        "files_checked": sum(r.get("files_in_shard", 0) for r in rows),
        "items_total": sum(r.get("items_total", 0) for r in rows),
        "links_total": sum(r.get("links_total", 0) for r in rows),
        "bad_files": len(bad),
        "bad_examples": bad[:15],
        "per_shard": [
            {
                "shard": r.get("shard"),
                "files": r.get("files_in_shard"),
                "items": r.get("items_total"),
                "links": r.get("links_total"),
                "bad": r.get("bad_count"),
            }
            for r in rows
        ],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    with open("executors-run.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
