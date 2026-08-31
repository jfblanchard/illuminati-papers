# Provenance — Anhang zu den Original-Schriften des Illuminaten-Ordens (1787)

- Title (source label): Anhang zu den Originalschriften des Illuminatenordens, welche auf
  höchsten Churfürstlichen Befehl zum Druck befördert worden sind.
- Publication: Frankfurt und Leipzig, 1787.
- Holding institution: Bayerische Staatsbibliothek (BSB), via MDZ (Münchener DigitalisierungsZentrum).
- Source page: https://www.digitale-sammlungen.de/de/view/bsb10381760
- IIIF manifest: https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb10381760/manifest
- OPAC record: https://opacplus.bsb-muenchen.de/title/BV010563793
- License: https://rightsstatements.org/vocab/NoC-NC/1.0/ (No Copyright – Non-Commercial Use Only)
- Page count: 40

## How this copy was assembled
Unlike the two Duke University items (which ship a ready-made PDF + djvu.txt), MDZ
serves this item as per-page IIIF images and per-page hOCR. Retrieved on 2026-08-03:

1. Full-resolution page images via IIIF Image API
   (`.../iiif/image/v2/bsb10381760_{page:05d}/full/full/0/default.jpg`), combined into
   `scans/anhang_1787/anhang_1787.pdf` (page order preserved, no re-compression beyond
   what PIL's PDF writer does).
2. Per-page hOCR via `.../ocr/bsb10381760/{page}`, text content extracted (tags
   stripped, one line per `ocr_line`) and concatenated into
   `ocr_raw/anhang_1787/anhang_1787_ocr.txt`, with `--- page N ---` separators.

This is a machine OCR layer from MDZ, not manually corrected — same caveats apply as
the raw OCR for the other two documents (Fraktur misreads, long-s, hyphenation).

## Known gap: line-final word breaks have no hyphen marker
Unlike the two Internet Archive documents (whose djvu.txt preserves the original
word-division mark — ⸗, =, or a misOCR'd em-dash — at the end of a broken word),
MDZ's hOCR line segmentation drops the hyphen glyph entirely. A word like
"wichtigen" broken across a line comes back as two separate hOCR lines, "wichti"
and "gen", with no character signalling they're one word. Verified by re-fetching
page 3's hOCR directly (`api.digitale-sammlungen.de/ocr/bsb10381760/3`) — the source
data itself lacks the marker, this isn't an artifact of the extraction script.
Consequence: `src/normalize_ocr.py`'s dehyphenation (Phase 2) cannot reconnect these
for the Anhang the way it does for the other two documents — every line-final word
in `anhang_1787_transcription.txt` is left as-is, space-joined, whether or not it was
actually broken. This needs to be handled during Phase 3 manual correction.

## Known gap: long-s (ſ) is normalized away throughout, not just at line breaks
Confirmed via direct visual correction of page 3 (see
`transcriptions/anhang_1787/anhang_1787_eval_sample.md`): MDZ's OCR renders every
long-s in the original print as a plain modern "s" — e.g. "Urſachen" comes back as
"Ursachen", "Miniſterium" as "Ministerium". This is systemic across the whole
document, not page-specific. The two Internet Archive documents' OCR does preserve
ſ (confirmed separately — see `lessons_learned.md`), so this is specifically an
Anhang/MDZ gap. Restoring ſ where the original used it is part of Phase 3 correction
for this document; it can't be inferred mechanically since MDZ's output gives no
signal of which "s" were originally long.
