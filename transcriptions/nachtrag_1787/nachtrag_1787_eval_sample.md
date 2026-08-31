# Nachtrag von weiteren Originalschriften — Evaluation Sample

Phase 3 (Correct): a representative sample of pages, manually corrected against the
scan image itself. See `transcriptions/anhang_1787/anhang_1787_eval_sample.md` for
the method and rationale — same approach here.

Spelling is preserved as printed. This document's OCR (Internet Archive, unlike the
Anhang's MDZ OCR) represents ä/ö/ü as a base vowel plus a combining "e" mark
(uͤ/aͤ/oͤ), matching this print's own small-e-above historic convention rather than
modern dot-umlauts — kept as-is below rather than "normalized" to ü/ä/ö, since that
would misrepresent what this OCR engine (correctly) preserved from the original type.

Source PDF: `scans/nachtrag_1787/nachtragvonweite121duke_0.pdf`. This document's OCR
has no page markers (see `todo.md` Phase 2/3), so page numbers below are the PDF's
own physical page numbers, cross-referenced by locating matching text with
`pdftotext`, not a marker in the transcription itself.

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

## PDF page 5 (title page)

**Raw OCR** (`nachtrag_1787_transcription.txt`, Phase 2 output):
> ; 1 = 5 ine a ee, e Aol , e a Canale, 7 00 4 5 2.4 | i 7 he z 15 2 1 FE | 25 5 nr
> 7 17 50 N Nachtrag Be von weitern Originalſchriften, welche die Illuminatenſekte
> uͤberhaupt, ſonderbar aber den Stifter derſelben Adam Wetshaupt, geweſenen
> Profeſſor zu Ingolſtadt 1 tveffen, 5 und bey der auf dem Baron Bellusiſchen
> Schloß zu Sandersdorf, einem bekannten IIluminaten-Neſte, vorgenommenen
> Vifitation entdeckt, ſofort auf Churfuͤrſtlich hoͤchſten Befehl gedruckt, und zum
> geheimen Archiv genommen worden ſind, um ſolche jedermann auf Verlangen zur
> Einſicht vorlegen zu laſſen. 3 wo Abtheilungen. e m — — —— N ide. 17 8 7 zu haben
> bey Joſeph Lentner.

**Corrected:**

Nachtrag
von weitern
Originalſchriften,

welche die Illuminatenſekte uͤberhaupt, ſonderbar aber den Stifter derſelben Adam
Weishaupt, geweſenen Profeſſor zu Ingolſtadt betreffen, und bey der auf dem Baron
Baſſuſiſchen Schloß zu Sandersdorf, einem bekannten Illuminaten-Neſte,
vorgenommenen Viſitation entdeckt, ſofort auf Churfuͤrſtlich hoͤchſten Befehl
gedruckt, und zum geheimen Archiv genommen worden ſind, um ſolche jedermann auf
Verlangen zur Einſicht vorlegen zu laſſen.

Zwo Abtheilungen.

Muͤnchen, 1787.
zu haben bey Joſeph Lentner.

**Corrections made:**
| Raw OCR | Corrected | Type |
|---|---|---|
| `1 = 5 ine a ee, e Aol , e a Canale, ...` (entire opening line) | *(removed)* | Pure noise — a handwritten ownership signature/stamp at the top of the physical page, not printed text |
| `Nachtrag Be` | `Nachtrag` | Stray "Be" is noise, not part of the title |
| `Wetshaupt` | `Weishaupt` | Misread (Adam Weishaupt, the order's founder) |
| `Ingolſtadt 1 tveffen, 5 und` | `Ingolſtadt betreffen, und` | Misread — "betreffen" (concerning) lost its "be-" prefix, stray "1"/"5" are noise |
| `Baron Bellusiſchen Schloß` | `Baron Baſſuſiſchen Schloß` | Misread ("of Baron Bassus's castle") |
| `IIluminaten-Neſte` | `Illuminaten-Neſte` | Doubled capital "I" misread |
| `Vifitation` | `Viſitation` | Missing long-s |
| `3 wo Abtheilungen.` | `Zwo Abtheilungen.` | "Z" misread as "3" |
| `e m — — ——` | *(removed)* | A decorative typographic rule, not text |
| `N ide. 17 8 7` | `Muͤnchen, 1787.` | Large decorative-cap "München" badly garbled |

**Uncertain / flagged:** none — page is legible and matches the known catalog title closely enough to resolve every misreading with confidence.

---

## PDF page 6 (body prose — an epigraph)

**Raw OCR:**
> Wenn man überlegt , wie die fchlechteſten Menſchen, wenn fie nur liſtig, und auf
> einen Ton geſtimmt, nach einerley Grundſaͤ⸗ tzen gebildet waren, aus ihren
> Mitbruͤdern alles zu machen verſtanden, derſelben ſchwache Seiten und herrſchende
> Leidenſchaften zu ihrem Vortheil zu nuͤtzen, fie mit falſchem Enthufiafmus fuͤr
> nichtswuͤrdige, der Rechtſchaffenheit, Vernunft und ihrem eignen Interefle
> entgegengeſetzte Dinge zu erfuͤllen wußten; — ſo muß man billig trauren.— — 4
> Philo im Circulari an die Logen. II. Abth. S. 137.

**Corrected:**

Wenn man uͤberlegt, wie die ſchlechteſten Menſchen, wenn ſie nur liſtig, und auf
einen Ton geſtimmt, nach einerley Grundſaͤtzen gebildet waren, aus ihren
Mitbruͤdern alles zu machen verſtanden, derſelben ſchwache Seiten und herrſchende
Leidenſchaften zu ihrem Vortheil zu nuͤtzen, ſie mit falſchem Enthuſiaſmus fuͤr
nichtswuͤrdige, der Rechtſchaffenheit, Vernunft und ihrem eignen Intereſſe
entgegengeſetzte Dinge zu erfuͤllen wußten; — ſo muß man billig trauren. — —

Philo
im Circulari an die Logen.
II. Abth. S. 137.

**Corrections made:**
| Raw OCR | Corrected | Type |
|---|---|---|
| `überlegt` (plain u) | `uͤberlegt` | Inconsistent with this document's own combining-e convention elsewhere on the same page — corrected for consistency |
| `fchlechteſten` | `ſchlechteſten` | "f"/"ſ" confusion — a common Fraktur OCR error (long-s and lowercase f are visually similar) |
| `Grundſaͤ⸗ tzen` (unjoined) | `Grundſaͤtzen` | **This was a Phase 2 script bug, not an OCR error** — found here, then fixed in `src/normalize_ocr.py` and re-run for all documents (see `lessons_learned.md`) |
| `fie` (x2) | `ſie` | f/ſ confusion, as above |
| `Enthufiafmus` | `Enthuſiaſmus` | f/ſ confusion (x2 in one word) |
| `Interefle` | `Intereſſe` | Misread |
| `trauren.— — 4` | `trauren. — —` | The trailing "4" is page-transition noise (a page number), not text |
| `Philo im Circulari an die Logen. II. Abth. S. 137.` | *(same, reformatted as attribution)* | No content error — "Philo" was Adolph Freiherr von Knigge's Illuminati code-name (not Weishaupt's, who used "Spartacus" — see the main volume's page-5 epigraph, same pattern). Worth flagging for Phase 5 (Annotate); this claim should get an independent check before publication, not just taken on my memory. |

**Uncertain / flagged:** none.

---

## PDF page 11 (printed page "3" — a numbered list, spanning a page-transition artifact)

**Raw OCR** (continues from the previous page's item 4, which is outside this sample):
> 3 es gewiß von ſelbſten auf. Die etwas minder Untauglichen ließ ich gaͤnzlich
> verſaumen, und ihnen nicht mehr ſchreiben. 8
>
> 5) Ein Haupkunitgrif ift, daß nicht beym erſten Eintritt ſchon der neu
> Aufgenommene alle Vorzuͤge, Bekanntſchaft und Geſellſchaft der Veteranen genießen
> darf.
>
> 6) Die junge Leute wollte ich an einen geſtandenen gebildeten Mann zum
> Unterricht vertheilen. f
>
> 7) Die, denen ſie zum Unterricht zugegeben werden, ſollen ſich niemalen mit
> ihren Untergebenen familiar machen, ſich ſuchen laſſen.
>
> 8) Hauptſaͤchlich aber koͤmmt es darauf an, welche Leute ſie in die Illuminaten
> Klaſſe aufnehmen werden: werden dieſe gut gewaͤhlt, ſo kann es auch recht gut
> gehen. Aber ich glaube, ſie muͤßen neues Blut in den ſiechen Körper. verſchaffen.
> Wenn neue vorher unbekannte, angeſehene, reſpectable Perſonen in dieſer Klaſſe
> erſcheinen, fo werden fie die ans genehmſten Folgen davon erfahren.
>
> 9) Vor allen ende die Güte der Sachen das eigene Beyſpiel; Man muß das ſelbſt
> ſeyn, wenigſtens ſcheinen, wozu man andere machen will. Nichts ſchadet der guten
> Sache
>
> 2 mehr,
>
> .
>
> 4
>
> mehr, als wenn die Worte mit den Thaten

**Corrected:**

*(continuing item 4)* ...es gewiß von ſelbſten auf. Die etwas minder Untauglichen
ließ ich gaͤnzlich verſaͤumen, und ihnen nicht mehr ſchreiben.

5) Ein Hauptkunſtgriff iſt, daß nicht beym erſten Eintritt ſchon der neu
Aufgenommene alle Vorzuͤge, Bekanntſchaft und Geſellſchaft der Veteranen genießen
darf.

6) Die junge Leute wollte ich an einen geſtandenen gebildeten Mann zum Unterricht
vertheilen.

7) Die, denen ſie zum Unterricht zugegeben werden, ſollen ſich niemalen mit ihren
Untergebenen familiar machen, ſich ſuchen laſſen.

8) Hauptſaͤchlich aber koͤmmt es darauf an, welche Leute ſie in die Illuminaten
Klaſſe aufnehmen werden: werden dieſe gut gewaͤhlt, ſo kann es auch recht gut
gehen. Aber ich glaube, ſie muͤßen neues Blut in den ſiechen Körper verſchaffen.
Wenn neue vorher unbekannte, angeſehene, reſpectable Perſonen in dieſer Klaſſe
erſcheinen, ſo werden ſie die angenehmſten Folgen davon erfahren.

9) Vor allen empfiehlt die Guͤte der Sache[n?] das eigene Beyſpiel; Man muß das
ſelbſt ſeyn, wenigſtens ſcheinen, wozu man andere machen will. Nichts ſchadet der
guten Sache

*[page footer: printed page number "3" (top), signature mark "A 2" and catchword
"mehr," (bottom) — these are what produced the "2 mehr," / "." / "4" noise in the
raw OCR, interleaved with the real text; "4" is the following page's printed page
number, and the real sentence continues "...Sache mehr, als wenn die Worte..."]*

**Corrections made:**
| Raw OCR | Corrected | Type |
|---|---|---|
| leading `3` | *(page number, not body text — kept as page-footer note instead)* | Noise from page layout |
| `verſaumen` | `verſaͤumen` | "versäumen" (to neglect) isn't a real word without the ä — corrected on lexical grounds even though the diacritic itself is small and hard to confirm at this image resolution (flagged below) |
| `Haupkunitgrif ift` | `Hauptkunſtgriff iſt` | Heavily garbled ("Hauptkunstgriff" = "chief trick/technique") |
| `vertheilen. f` | `vertheilen.` | Trailing "f" is noise |
| `Aber ich glaube` region: `Körper. verſchaffen` | `Körper verſchaffen` | Spurious mid-word/mid-phrase period — **this is the third time this exact failure mode has shown up** (also `immer . hin`, `Das lez . tere` in the Anhang sample), i.e. the OCR inserts a period mid-phrase for no visible reason on the page. Worth watching for throughout Phase 3. |
| `fo werden fie die ans genehmſten` | `ſo werden ſie die angenehmſten` | f/ſ confusion + "ans" should be part of "angenehmſten" (most agreeable) |
| `ende die Güte` | `empfiehlt die Guͤte` | Misread — "empfiehlt" (recommends), not "ende" (ends) |
| `2 mehr, / . / 4` | *(page-footer noise: signature "A 2" + catchword "mehr," + next page's number "4")* | Page-transition artifact — see `todo.md` Phase 2/3 notes |

**Uncertain / flagged:**
- `Sache` vs `Sachen` in "die Güte der Sache[n]": the line wraps right at this word
  and I can't confirm with full confidence which it is from the scan alone. The
  same phrase later in the same paragraph ("Nichts ſchadet der guten Sache") is
  unambiguously singular, which weakly favors "Sache" here too by parallelism, but
  this is not certain — flagged for a second look rather than silently guessed.
- The diacritic on `verſaͤumen` is small enough at this image resolution that I'm
  inferring it from the word's lexical validity (no such word as "versaumen"
  without it), not from a fully confident visual read.

---

*(More pages to be added here as the representative sample is built out.)*
