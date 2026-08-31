#!/usr/bin/env python3
"""Phase 2 (Normalize): clean raw OCR into a UTF-8 diplomatic transcription.

Dehyphenates line-final word-division marks (the historic ⸗, plain OCR "-", and
the older "=" convention) and reflows blank-line-delimited blocks into continuous
paragraphs. Does not touch spelling, ligatures, or long-s (ſ) — this is the
original-spelling layer per the project's phase design. It also does not try to
identify or strip page-boundary noise (running catchwords, page numbers) that the
OCR interleaves into the text stream — those are left as short isolated blocks
for a human to handle in Phase 3, not guessed at here.
"""
import re
import unicodedata
from pathlib import Path

HYPHEN_CHARS = ("⸗", "=", "-", "—")
# Em-dash is ambiguous: this print uses it for real punctuation (always with a
# preceding space, e.g. "Briefe — werden") and for name/word redaction, as well
# as (misOCR'd from ⸗) line-final word-division. Checked directly: every em-dash
# immediately after a letter (no space) at line-end in this corpus is a genuine
# word break (e.g. "ver—" + "ſprechen" -> "verſprechen") — the no-space-before
# check below is what keeps this safe.
PAGE_MARKER_RE = re.compile(r"^--- page (\d+) ---$")


def _is_word_char(ch: str) -> bool:
    """True for letters and combining marks (e.g. U+0364 COMBINING LATIN SMALL
    LETTER E, this print's convention for ä/ö/ü as "aͤ"/"oͤ"/"uͤ"). Plain
    str.isalpha() returns False for combining marks, which silently broke
    rejoining for words like "Grundſaͤ⸗" + "tzen" -> "Grundſätzen" (85 cases
    across the two Internet Archive documents) — caught by manual correction of
    a real page during Phase 3, not by inspection of the code alone."""
    return ch.isalpha() or unicodedata.combining(ch) != 0

ROOT = Path(__file__).resolve().parent.parent
DOCS = {
    "einige_originalschriften_1787": "einigeoriginalsc01duke_0_djvu.txt",
    "nachtrag_1787": "nachtragvonweite121duke_0_djvu.txt",
    "anhang_1787": "anhang_1787_ocr.txt",
}


def join_block_lines(lines: list[str]) -> tuple[str, int]:
    """Join a paragraph block's lines into one line of continuous text,
    resolving line-final word-division marks. Returns (text, num_rejoins)."""
    if not lines:
        return "", 0
    result = lines[0].strip()
    rejoins = 0
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        if result and result[-1] in HYPHEN_CHARS and len(result) >= 2 and _is_word_char(result[-2]):
            result = result[:-1] + line
            rejoins += 1
        else:
            result = f"{result} {line}" if result else line
    return result, rejoins


def normalize_text(raw: str) -> tuple[str, dict]:
    lines = raw.split("\n")
    out_blocks: list[str] = []
    current_block: list[str] = []
    total_rejoins = 0
    num_pages = 0

    def flush():
        nonlocal total_rejoins
        if current_block:
            text, rejoins = join_block_lines(current_block)
            total_rejoins += rejoins
            if text:
                out_blocks.append(text)
            current_block.clear()

    for line in lines:
        stripped = line.strip()
        m = PAGE_MARKER_RE.match(stripped)
        if m:
            flush()
            out_blocks.append(f"--- page {m.group(1)} ---")
            num_pages += 1
            continue
        if stripped == "":
            flush()
            continue
        current_block.append(line)
    flush()

    text = "\n\n".join(out_blocks) + "\n"
    stats = {"blocks": len(out_blocks), "rejoins": total_rejoins, "pages": num_pages}
    return text, stats


def main() -> None:
    for doc, fname in DOCS.items():
        src_path = ROOT / "ocr_raw" / doc / fname
        if not src_path.exists():
            print(f"SKIP {doc}: {src_path} not found")
            continue
        raw = src_path.read_text(encoding="utf-8")
        cleaned, stats = normalize_text(raw)
        out_dir = ROOT / "transcriptions" / doc
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{doc}_transcription.txt"
        out_path.write_text(cleaned, encoding="utf-8")
        page_note = f", {stats['pages']} page markers" if stats["pages"] else ""
        print(
            f"{doc}: {len(raw)} -> {len(cleaned)} chars, "
            f"{stats['blocks']} blocks, {stats['rejoins']} dehyphenation joins{page_note}"
        )


if __name__ == "__main__":
    main()
