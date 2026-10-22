#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""qc_digest.py — языковой и структурный контроль выпуска Horizon (ЗАКОН 34).

Проблема, которую лечит: модель-обогатитель (ministral-8b) на части материалов
игнорирует «пиши по-русски» и отдаёт блок целиком на языке источника (китайский).
В выпуск попадало 633 иероглифа.

Что делает:
  1) находит все фрагменты чужой письменности для целевого языка (ru → всё, кроме кириллицы/латиницы/цифр);
  2) переводит их на целевой язык через бесплатную LLM (Groq → Mistral → OpenRouter, с перебором);
  3) если перевести не удалось — вырезает битый блок целиком (лучше меньше, чем брак) и чинит нумерацию;
  4) проверяет структуру: front matter, ≥10 материалов, ≥1 ссылка, отсутствие мусора;
  5) пишет отчёт state/qc-digest-<дата>.json и возвращает код 1, если брак остался.

Использование:
  python3 scripts/qc_digest.py report  _posts/2026-10-22-summary-ru.md --lang ru
  python3 scripts/qc_digest.py fix     _posts/2026-10-22-summary-ru.md --lang ru --write
  python3 scripts/qc_digest.py verify  _posts/2026-10-22-summary-ru.md --lang ru

Только stdlib (urllib). Ключи: GROQ_API_KEY / MISTRAL_API_KEY / OPENROUTER_API_KEY из env
или из my-api-keys.md рядом с репозиторием.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.request

# --- письменности -----------------------------------------------------------
CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\u3040-\u30ff\uac00-\ud7af]")
CYR = re.compile(r"[\u0400-\u04ff]")
LAT = re.compile(r"[A-Za-z]")
CYR_OR_LAT = re.compile(r"[\u0400-\u04ffA-Za-z]")
# CJK-пунктуация: для русского выпуска это тоже брак («『』【】、。！？：・　» и т.п.)
CJK_PUNCT = re.compile(r"[\u3000-\u303f\uff01-\uff5e]")
PUNCT_MAP = {
    "\u300c": "«", "\u300d": "»", "\u300e": "«", "\u300f": "»",
    "\u3010": "«", "\u3011": "»", "\u3014": "(", "\u3015": ")",
    "\u3001": ",", "\u3002": ".", "\uff0c": ",", "\uff0e": ".",
    "\uff1a": ":", "\uff1b": ";", "\uff01": "!", "\uff1f": "?",
    "\uff08": "(", "\uff09": ")", "\u30fb": "·", "\u3000": " ",
    "\uff0d": "-", "\u2015": "—", "\uff5e": "~", "\uff05": "%",
    "\uff03": "#", "\uff0f": "/", "\u201c": "«", "\u201d": "»",
    "\u2018": "«", "\u2019": "»",
}

# порог: строка считается битой, если чужой письменности в ней >= 4 символов
MIN_FOREIGN = 4

HEADING = re.compile(r"^#{2,4}\s")
ITEM = re.compile(r"^#{3}\s")
TOC = re.compile(r"^\d+\.\s+\[")
FRONT = re.compile(r"^---\s*$")

PROVIDERS = [
    ("openrouter/gemma-4-31b", "https://openrouter.ai/api/v1/chat/completions",
     "OPENROUTER_API_KEY", "google/gemma-4-31b-it:free"),
    ("openrouter/minimax", "https://openrouter.ai/api/v1/chat/completions",
     "OPENROUTER_API_KEY", "minimax/minimax-m3.1-flash:free"),
    ("openrouter/gemma-4-26b", "https://openrouter.ai/api/v1/chat/completions",
     "OPENROUTER_API_KEY", "google/gemma-4-26b-a4b-it:free"),
    ("groq", "https://api.groq.com/openai/v1/chat/completions", "GROQ_API_KEY",
     "llama-3.3-70b-versatile"),
    ("mistral", "https://api.mistral.ai/v1/chat/completions", "MISTRAL_API_KEY",
     "ministral-8b-latest"),
]
LANG_NAME = {"ru": "русский", "en": "English", "zh": "简体中文"}


def load_keys() -> dict:
    keys = {p[2]: os.environ.get(p[2], "") for p in PROVIDERS}
    for path in ("my-api-keys.md", "../my-api-keys.md", os.path.expanduser("~/my-api-keys.md")):
        if not all(keys.values()) and os.path.exists(path):
            text = open(path, encoding="utf-8", errors="ignore").read()
            pats = {"GROQ_API_KEY": r"gsk_[A-Za-z0-9]{20,}",
                    "OPENROUTER_API_KEY": r"(?:sk-or-v1-)?[a-f0-9]{64}",
                    "MISTRAL_API_KEY": r"(?<![\w-])[A-Za-z0-9]{32}(?![\w-])"}
            for name, pat in pats.items():
                if not keys.get(name):
                    m = re.search(pat, text)
                    if m:
                        keys[name] = m.group(0)
    return keys


def stderr(msg: str) -> None:
    print(msg, file=sys.stderr)


def ask_llm(prompt: str, keys: dict, temperature: float = 0.2) -> str | None:
    """Спрашивает модели по очереди, пока какая-нибудь не ответит."""
    order = list(PROVIDERS)
    random.shuffle(order)  # распределяем нагрузку по бесплатным лимитам
    for name, url, env, model in order:
        key = keys.get(env)
        if not key:
            continue
        body = json.dumps({
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
            "max_tokens": 2000,
        }).encode()
        req = urllib.request.Request(url, data=body, method="POST", headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/Ayt1741/Horizon",
            "X-Title": "Horizon QC",
        })
        for attempt in (1, 2):
            try:
                with urllib.request.urlopen(req, timeout=90) as r:
                    data = json.loads(r.read())
                text = data["choices"][0]["message"]["content"].strip()
                if text:
                    stderr(f"  [{name}/{model}] ok")
                    return text
            except urllib.error.HTTPError as e:
                code = e.code
                stderr(f"  [{name}/{model}] HTTP {code}")
                if code in (401, 402, 403, 404):
                    break
                if code == 429:
                    time.sleep(3)
                    continue
            except Exception as e:  # noqa: BLE001
                stderr(f"  [{name}/{model}] {type(e).__name__}")
                break
        time.sleep(0.5)
    return None


# --- анализ -----------------------------------------------------------------
def normalize_punct(text: str) -> str:
    """Заменяет CJK-пунктуацию на русскую/ASCII (без изменения смысла)."""
    for src, dst in PUNCT_MAP.items():
        text = text.replace(src, dst)
    return re.sub(r"[ \t]{2,}", " ", text)


def strip_stray_cjk(text: str) -> str:
    """Убирает одиночные иероглифы (1-3 знака), которые не стоят отдельного перевода."""
    def _one(line: str) -> str:
        n = len(CJK.findall(line))
        if 0 < n < MIN_FOREIGN:
            line = re.sub(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\u3040-\u30ff\uac00-\ud7af]", "", line)
            line = re.sub(r"[ \t]{2,}", " ", line)
        return line
    return "\n".join(_one(l) for l in text.splitlines())


def punct_count(text: str) -> int:
    return len(CJK_PUNCT.findall(text))


def foreign_count(line: str, lang: str) -> int:
    if lang == "zh":
        return len(CYR.findall(line))
    return len(CJK.findall(line))


def is_bad(line: str, lang: str) -> bool:
    return foreign_count(line, lang) >= MIN_FOREIGN


def scan(text: str, lang: str) -> dict:
    lines = text.splitlines()
    bad = [(i, l) for i, l in enumerate(lines) if is_bad(l, lang)]
    items = [l for l in lines if ITEM.match(l)]
    links = len(re.findall(r"\]\(https?://", text))
    return {
        "lines": len(lines),
        "chars": len(text),
        "foreign_lines": len(bad),
        "foreign_chars": sum(foreign_count(l, lang) for _, l in bad),
        "cjk_punct": punct_count(text),
        "any_cjk_broad": len(re.findall(r"[\u3000-\u9fff\uac00-\ud7af]", text)),
        "items": len(items),
        "links": links,
        "samples": [l[:120] for _, l in bad[:5]],
        "bad_indexes": [i for i, _ in bad],
    }


def front_matter_ok(text: str) -> bool:
    parts = text.split("---")
    return text.lstrip().startswith("---") and len(parts) >= 3 and len(parts[1].strip()) > 10


# --- исправление ------------------------------------------------------------
def translate_line(line: str, lang: str, keys: dict) -> str | None:
    """Переводит одну строку, сохраняя markdown-разметку, ссылки, эмодзи и рейтинг."""
    keep = re.findall(r"\[[^\]]*\]\([^)]*\)|`[^`]*`|⭐️\s*[\d.]+/10|#[\w\-А-Яа-яЁё ]+", line)
    prompt = (
        f"Переведи строку на {LANG_NAME.get(lang, lang)}. Правила:\n"
        "1. Верни ТОЛЬКО перевод, без пояснений и кавычек.\n"
        "2. Сохрани всю разметку Markdown: #, **, `, [текст](ссылка), списки, эмодзи, рейтинги вида ⭐️ 8.0/10.\n"
        "3. URLs не переводи и не меняй.\n"
        "4. Имена собственные и названия моделей можно оставить латиницей.\n"
        "5. Никаких иероглифов в ответе.\n\n"
        f"Строка:\n{line}"
    )
    out = ask_llm(prompt, keys)
    if not out:
        return None
    out = "\n".join(l for l in out.strip().splitlines() if l.strip()).strip().strip('"').strip()
    # модель иногда дописывает исходник — вырезаем любые иероглифы/кану
    out = re.sub(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\u3040-\u30ff\uac00-\ud7af]+", "", out)
    out = re.sub(r"[ \t]{2,}", " ", out)
    # ссылка-анкор из оглавления должна сохраниться
    m = re.search(r"\]\((#[^)]+)\)", line)
    if m and m.group(1) not in out and out.rstrip().endswith("]"):
        out = out.rstrip() + "(" + m.group(1) + ")"
    rating = re.search(r"⭐️\s*[\d.]+/10", line)
    if rating and rating.group(0) not in out:
        out = out + " " + rating.group(0)
    if lang == "ru" and not (CYR.search(out) or LAT.search(out)):
        return None
    if is_bad(out, lang):
        return None
    return out


ANCHOR = re.compile(r'^\s*<a\s+id="([^"]+)"')


def items_index(lines: list[str]) -> list[dict]:
    """Список материалов: строка заголовка, строка анкора (если есть), границы блока."""
    out = []
    for i, line in enumerate(lines):
        if not ITEM.match(line):
            continue
        anchor, a = None, i
        if i > 0:
            m = ANCHOR.match(lines[i - 1])
            if m:
                anchor, a = m.group(1), i - 1
        end = i + 1
        while end < len(lines) and not HEADING.match(lines[end]):
            end += 1
        out.append({"start": a, "heading": i, "end": end, "anchor": anchor})
    # блок материала заканчивается там, где начинается следующий (его анкор идёт ПЕРЕД заголовком)
    for k in range(len(out) - 1):
        if out[k + 1]["start"] < out[k]["end"]:
            out[k]["end"] = out[k + 1]["start"]
    return out


def fix(text: str, lang: str, keys: dict, drop_unfixable: bool = True, attempts: int = 3) -> tuple[str, dict]:
    text = strip_stray_cjk(normalize_punct(text))
    lines = text.splitlines()
    report = {"translated": 0, "dropped_items": 0, "failed": 0, "cache": 0, "attempts": attempts}
    cache_path = os.environ.get("QC_CACHE", "state/qc-translation-cache.json")
    cache: dict[str, str] = {}
    if os.path.exists(cache_path):
        try:
            cache = json.load(open(cache_path, encoding="utf-8"))
            cache = {k: v for k, v in cache.items() if isinstance(v, str) and not is_bad(v, lang)}
            stderr("  кеш перевода: %d годных строк" % len(cache))
        except Exception:  # noqa: BLE001
            cache = {}

    bad = [i for i in range(len(lines)) if is_bad(lines[i], lang)]
    for i in bad:
        line = lines[i]
        if line in cache:
            lines[i] = cache[line]
            report["cache"] += 1
            continue
        for _ in range(attempts):
            new = translate_line(line, lang, keys)
            if new:
                cache[line] = new
                lines[i] = new
                report["translated"] += 1
                break
            time.sleep(1.0)
        else:
            report["failed"] += 1

    # что осталось битым — вырезаем материалом вместе с его пунктом в оглавлении
    dropped_anchors: set[str] = set()
    remaining = [i for i in range(len(lines)) if is_bad(lines[i], lang)]
    if remaining and drop_unfixable:
        for item in items_index(lines):
            hits = [i for i in remaining if item["start"] <= i < item["end"]]
            if hits:
                stderr("  ВЫРЕЗАЮ материал %s (%s): %d строк не перевелись"
                       % (item["anchor"], lines[item["heading"]][:60], len(hits)))
                for h in hits:
                    stderr("    битая строка CJK=%r: %s" % (CJK.findall(lines[h])[:8], lines[h][:140].replace("\n", " / ")))
                if item["anchor"]:
                    dropped_anchors.add(item["anchor"])
    if dropped_anchors:
        drop_ranges = [(it["start"], it["end"]) for it in items_index(lines) if it["anchor"] in dropped_anchors]
        for s0, e0 in sorted(set(drop_ranges), reverse=True):
            del lines[s0:e0]
            report["dropped_items"] += 1
        lines = [l for l in lines if not any(a in l for a in dropped_anchors) or not TOC.match(l)]

    try:
        os.makedirs(os.path.dirname(cache_path) or ".", exist_ok=True)
        json.dump(cache, open(cache_path, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    except OSError:
        pass

    # мусор вне материалов
    leftover = [l for l in lines if is_bad(l, lang)]
    report["leftover_removed"] = len(leftover)
    lines = [l for l in lines if not is_bad(l, lang)]
    return "\n".join(lines) + ("\n" if text.endswith("\n") else ""), report


def renumber(text: str) -> str:
    """Глобальная перенумерация пунктов оглавления (1..N по всему выпуску)."""
    out, n = [], 0
    for line in text.splitlines():
        if TOC.match(line):
            n += 1
            out.append(re.sub(r"^\d+\.", f"{n}.", line))
        else:
            out.append(line)
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["report", "fix", "verify"])
    ap.add_argument("file")
    ap.add_argument("--lang", default="ru")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--no-drop", action="store_true")
    a = ap.parse_args()

    text = open(a.file, encoding="utf-8").read()
    before = scan(text, a.lang)
    result = {"file": a.file, "lang": a.lang, "before": before, "cmd": a.cmd}

    if a.cmd == "report":
        result["verdict"] = "PASS" if before["foreign_chars"] == 0 and before["cjk_punct"] == 0 else "FAIL"
        print(json.dumps(result, ensure_ascii=False, indent=1))
        return 0 if result["verdict"] == "PASS" else 1

    if a.cmd == "fix":
        keys = load_keys()
        if not any(keys.values()):
            stderr("Нет ни одного ключа LLM — перевод невозможен, только вырезание")
        fixed, frep = fix(text, a.lang, keys, drop_unfixable=not a.no_drop)
        fixed = renumber(fixed)
        after = scan(fixed, a.lang)
        result.update({"fix": frep, "after": after,
                       "front_matter_ok": front_matter_ok(fixed),
                       "verdict": ("PASS" if after["foreign_chars"] == 0 and after["cjk_punct"] == 0
                                   and after.get("any_cjk_broad", 0) == 0
                                   and (after["items"] >= 10 or after["links"] >= 10) else "FAIL")})
        if a.write:
            with open(a.file, "w", encoding="utf-8") as f:
                f.write(fixed)
            result["written"] = True
        os.makedirs("state", exist_ok=True)
        date = re.search(r"\d{4}-\d{2}-\d{2}", a.file)
        out = f"state/qc-digest-{date.group(0) if date else 'run'}.json"
        with open(out, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=1)
        result["report_path"] = out
        print(json.dumps(result, ensure_ascii=False, indent=1))
        return 0 if result["verdict"] == "PASS" else 1

    after = scan(text, a.lang)
    result["after"] = after
    result["front_matter_ok"] = front_matter_ok(text)
    result["verdict"] = ("PASS" if after["foreign_chars"] == 0 and after["cjk_punct"] == 0
                         and after.get("any_cjk_broad", 0) == 0
                         and (after["items"] >= 10 or after["links"] >= 10) and after["links"] > 0 else "FAIL")
    print(json.dumps(result, ensure_ascii=False, indent=1))
    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
