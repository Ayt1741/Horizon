"""Deterministic normalization for localized AI output."""

from opencc import OpenCC

import re


_TRADITIONAL_TO_SIMPLIFIED = OpenCC("t2s")

_CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\u3040-\u30ff\uac00-\ud7af]")
_CYR_RE = re.compile(r"[\u0400-\u04ff]")
_LAT_RE = re.compile(r"[A-Za-z]")
# сколько знаков чужой письменности допускаем (названия моделей и аббревиатуры — латиницей это норма)
_MIN_FOREIGN = 4


def normalize_language(text: str, language: str) -> str:
    """Normalize generated text to the script implied by its language tag."""
    if language.lower() == "zh":
        return _TRADITIONAL_TO_SIMPLIFIED.convert(text)
    return text


def foreign_script_count(text: str, language: str) -> int:
    """How many characters of a script that is wrong for `language` the text contains."""
    tag = language.lower()
    if tag == "zh":
        return len(_CYR_RE.findall(text))
    return len(_CJK_RE.findall(text))


def script_mismatch(text: str, language: str) -> bool:
    """True when the text is written in a different script than the target language.

    Used as a generation-time guard: an artifact in the wrong script is rejected and retried
    instead of silently leaking into the digest.
    """
    return foreign_script_count(text, language) >= _MIN_FOREIGN
