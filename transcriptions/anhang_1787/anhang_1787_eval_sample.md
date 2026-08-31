# Anhang zu den Original-Schriften des Illuminaten-Ordens — Evaluation Sample

Phase 3 (Correct): a representative sample of pages, manually corrected against the
scan image itself (viewed directly, not re-run through a separate OCR engine), to
(a) measure how much the raw OCR actually needs fixing before trusting it broadly,
and (b) give Phase 4 (Translate) a small set of pages with known-reliable German text.

Spelling is preserved as printed (long ſ, "ey" for "ei", etc.) — this is the
diplomatic/original-spelling layer per the project's Phase 2/3 design. Modernizing
spelling is a Phase 4 concern, not this one.

Source PDF: `scans/anhang_1787/anhang_1787.pdf`. Page numbers below match that PDF's
page order and the `--- page N ---` markers in
`transcriptions/anhang_1787/anhang_1787_transcription.txt`.

## Methodology & status
Corrections made by Claude (Sonnet 5) on 2026-08-04, by direct visual inspection of
the page scan images (rendered from the source PDF at 300 DPI via `pdftoppm`) against
the raw OCR / Phase 2 transcription. Every correction below is logged with a
before/after and a reason, for traceability. This is an **AI-assisted first pass,
not a final scholarly correction** — every entry here is provisional until reviewed
by a human with relevant expertise. Historical/factual claims noted inline (e.g.
code-name attributions) are flagged separately where confidence is not full, and
should be independently verified before anything here is treated as citable in a
publication.

---

## Page 3

**Raw OCR** (`anhang_1787_transcription.txt`, Phase 2 output):
> 1 B Wezlar den 20ten May 1787 . ester Freund ! Die Ihnen bekannten wichti gen
> Ursachen verhindern mich noch immer . hin an der Erfulung meines innigsten Wun
> sches , entweder hier am Reichsgericht gegen das Verfahren des Münchner Cabinets
> Processe zu führen , oder doch wenigstens dem Publicum meine vouständige
> Schuhschrift vorzulegen . Das lez . tere ist zwar größten Theils durch einzelne
> von meinen in mehrern Journalen abgedruckten Anlangen und Briefen , welche ich
> dem Kurfursten und baierischen Ministerium zuschickte , gleich zu Anfang meiner
> zweyten lekten Verfolgung gesche hen . Diese sind von der baierischen Regierung
> ohne Antwort und ohne Widerlegung bis diese Stunde geblieben , und da die
> Behandlung gegen mich nur eine Fortsehung von jenen Gewaltthålig keiten war ,
> welche bereits von andern Ver . Na folg . ۱

**Corrected** (read directly from the scan image):

Wetzlar den 20ten May 1787.

Beſter Freund! Die Ihnen bekannten wichtigen Urſachen verhindern mich noch
immerhin an der Erfüllung meines innigſten Wunſches, entweder hier am
Reichsgericht gegen das Verfahren des Münchner Cabinets Proceſſe zu führen, oder
doch wenigſtens dem Publicum meine vollſtändige Schutzſchrift vorzulegen. Das
letztere iſt zwar größten Theils durch einzelne von meinen in mehrern Journalen
abgedruckten Anlangen und Briefen, welche ich dem Kurfürſten und baieriſchen
Miniſterium zuſchickte, gleich zu Anfang meiner zweyten letzten Verfolgung
geſchehen. Dieſe ſind von der baieriſchen Regierung ohne Antwort und ohne
Widerlegung bis dieſe Stunde geblieben, und da die Behandlung gegen mich nur eine
Fortſetzung von jenen Gewaltthätigkeiten war, welche bereits von andern Ver—

*[page-bottom: signature mark "A 2", catchword "folg." — continues "Verfolgungen" on the next page]*

**Corrections made:**
| Raw OCR | Corrected | Type |
|---|---|---|
| `1 B ... ester Freund` | `Beſter Freund` | Drop-cap "B" missed by OCR (decorative initial); stray "1" is noise from the woodcut headpiece above the text, not a character |
| `immer . hin` | `immerhin` | Spurious mid-word period |
| `Erfulung` | `Erfüllung` | Misread — missing umlaut and a dropped "l" |
| `Processe` | `Proceſſe` | Missing long-s |
| `vouständige Schuhschrift` | `vollſtändige Schutzſchrift` | Badly garbled ("complete vindication document") |
| `Das lez . tere` | `Das letztere` | Spurious period splitting the word |
| `Kurfursten` | `Kurfürſten` | Missing umlaut + long-s |
| `baierischen` (x2) | `baieriſchen` | Missing long-s |
| `Ministerium` | `Miniſterium` | Missing long-s |
| `zweyten lekten` | `zweyten letzten` | Misread |
| `gesche hen` | `geſchehen` | Missing long-s + un-rejoined line break (known Anhang gap) |
| `Diese sind` | `Dieſe ſind` | Missing long-s |
| `Fortsehung` | `Fortſetzung` | Misread ("tz" read as "h") |
| `Gewaltthålig keiten` | `Gewaltthätigkeiten` | Misread ("ä" garbled as "å") + un-rejoined line break |
| `Na folg . ۱` | *(signature mark "A 2" + catchword "folg.")* | OCR noise on the printer's gathering mark; "folg." itself was read correctly |
| *(throughout)* | ſ restored wherever OCR shows plain "s" mid-word | **Systemic**, not page-specific — confirms MDZ's OCR normalizes ſ→s across the whole document (see `anhang_1787_provenance.md`) |

**Uncertain / flagged:** none on this page — the scan is clean and legible throughout.

---

*(More pages to be added here as the representative sample is built out.)*
