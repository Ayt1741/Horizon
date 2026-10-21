#!/usr/bin/env python3
"""Сборка отчётов 10 руководителей в один свод (только stdlib)."""
import json
import os
import sys


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "artifacts"
    out = sys.argv[2] if len(sys.argv) > 2 else "docs/council-10.json"
    leaders = {}
    for dirpath, _d, files in os.walk(root):
        for name in files:
            if name.endswith(".json") and name.startswith("result-"):
                try:
                    with open(os.path.join(dirpath, name), encoding="utf-8") as f:
                        data = json.load(f)
                except (OSError, ValueError):
                    continue
                key = data.get("leader") or name.replace("result-", "").replace(".json", "")
                leaders[key] = data
    summary = {
        "leaders_returned": len(leaders),
        "leaders_expected": 10,
        "missing": [f"L{i}" for i in range(1, 11) if f"L{i}" not in leaders],
        "results": {k: leaders[k] for k in sorted(leaders)},
    }
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=1)
    print(json.dumps({"leaders_returned": summary["leaders_returned"], "missing": summary["missing"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
