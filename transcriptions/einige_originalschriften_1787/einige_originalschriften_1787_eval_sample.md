# Einige Originalschriften des Illuminatenordens — Evaluation Sample

Phase 3 (Correct): a representative sample of pages, manually corrected against the
scan image itself. See `transcriptions/anhang_1787/anhang_1787_eval_sample.md` for
the method and rationale.

Spelling preserved as printed, including this document's combining-e convention for
umlauts (uͤ/aͤ/oͤ) — same reasoning as `nachtrag_1787_eval_sample.md` (same OCR
engine/source, Internet Archive, Duke University Jantz Collection).

Source PDF: `scans/einige_originalschriften_1787/einigeoriginalsc01duke_0.pdf`. No
page markers in this document's OCR either; page numbers below are the PDF's
physical page numbers, located via `pdftotext` + text search, not a transcription
marker.

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

**Raw OCR** (`einige_originalschriften_1787_transcription.txt`, Phase 2 output):
> Einige
>
> Originalſchriften
>
> Illuminatenordens,
>
> welche bey dem geweſenen Regierungsrath Zwack durch vorgenommene Hauspifitation
> zu kandshut den 11. und 12. Oktob. ꝛc.
>
> 78% vorgefunden worden.
>
> Auf hoͤchſten Befehl Seiner Churfuͤrſtlichen Durchleucht zum Druck befördert. |
>
> Mun ch e n,
>
> gedruckt bey Anton Franz, Churfl. Hofbuchdrucker, und 5 zu haben in den drey
> Buchhandlungen.

**Corrected:**

Einige
Originalſchriften
des
Illuminatenordens,

welche bey dem geweſenen Regierungsrath Zwack durch vorgenommene Hausviſitation zu
Landshut den 11. und 12. Oktob. ꝛc.
1786.
vorgefunden worden.

Auf hoͤchſten Befehl Seiner Churfuͤrſtlichen Durchleucht zum Druck befördert.

Muͤnchen,
gedruckt bey Anton Franz, Churfl. Hofbuchdrucker, und
zu haben in den drey Buchhandlungen.

**Corrections made:**
| Raw OCR | Corrected | Type |
|---|---|---|
| `Originalſchriften` / `Illuminatenordens,` (no "des" between) | `Originalſchriften des Illuminatenordens,` | **A whole word dropped by OCR**, not just a misread — worth remembering as a category of error the raw OCR can produce (omission, not just distortion) |
| `Hauspifitation` | `Hausviſitation` | Misread ("Hausvisitation" = house search) |
| `kandshut` | `Landshut` | Capital L misread as lowercase k |
| `78%` | `1786.` | Badly garbled year — resolves a garbled fragment flagged all the way back when this project first skimmed the raw OCR in Phase 1 |
| `befördert. \|` | `befördert.` | Stray pipe character is noise |
| `Mun ch e n,` | `Muͤnchen,` | Decorative large-cap "München" broken up by OCR |
| `und 5 zu haben` | `und zu haben` | Stray "5" is noise |

**Uncertain / flagged:** none — page is clean and fully legible.

---

## PDF page 7 (preface prose)

**Raw OCR:**
> 7 8 egenwaͤrtige Sammlung iſt auf Churfuͤrſtl.
>
> 8 höchſten Befehl zum Druck befordert worden, um das in⸗ und auslaͤndiſche
> Publicum 80 . det offenbaren Ungrund, womit die Illaininaten noch immer über
> ungerechte Gewalt und Verfolgung in Bayern ſchreyen, deſto mehr zu uͤberzeugen,
> und ſelbes ſowohl von dieſer epidemiſchen Sefte An all andern dergleichen
> verbothenen Winkelgeſellſchaften zu
>
> warnen, worin man nur Leichtglaubige zu
>
> betruͤgen, Geld zu ſchneuzen, und ſtatt der
>
> vorgeſpiegelten Wahrheitsaufklaͤr⸗ und Sittenverbeſſerung, dieſe vielmehr im
> Grund zu verderben, und jene gaͤnzlich zu unterdruͤcken, der zu verfaͤlſchen
> bemuͤhet iſt.

**Corrected:**

Gegenwaͤrtige Sammlung iſt auf Churfuͤrſtl. hoͤchſten Befehl zum Druck befoͤrdert
worden, um das in⸗ und auslaͤndiſche Publicum von dem offenbaren Ungrund, womit
die Illuminaten noch immer uͤber ungerechte Gewalt und Verfolgung in Bayern
ſchreyen, deſto mehr zu uͤberzeugen, und ſelbes ſowohl von dieſer epidemiſchen
Secte, als all andern dergleichen verbothenen Winkelgeſellſchaften zu warnen,
worin man nur Leichtglaͤubige zu betruͤgen, Geld zu ſchneuzen, und ſtatt der
vorgeſpiegelten Wahrheitsaufklaͤr⸗ und Sittenverbeſſerung, dieſe vielmehr im Grund
zu verderben, und jene gaͤnzlich zu unterdruͤcken, oder zu verfaͤlſchen bemuͤhet
iſt.

*[catchword: "Wer" — continues onto the next page]*

**Corrections made:**
| Raw OCR | Corrected | Type |
|---|---|---|
| `7 8 egenwaͤrtige` | `Gegenwaͤrtige` | Decorative drop-cap "G" missed (same failure pattern as the Anhang's missing "B" in `anhang_1787_eval_sample.md`); "7 8" is noise from a library catalog stamp visible in the top-right corner of this page, and decorative ornaments above the text |
| `befordert` | `befoͤrdert` | Missing combining-e mark |
| `Publicum 80 . det offenbaren` | `Publicum von dem offenbaren` | Genuine misread, not just noise — "80 . det" replaces "von dem" |
| `Illaininaten` | `Illuminaten` | Misread |
| `Sefte` | `Secte` | Misread ("Sekte/Secte" = sect) |
| `zu\n\nwarnen` / `Leichtglaubige` | `zu warnen` / `Leichtglaͤubige` | Reflow across a block boundary that Phase 2 didn't merge (short line, no hyphen mark, so the mechanical dehyphenation correctly left it — this one needed a human to join) + missing combining-e |
| `der zu verfaͤlſchen` | `oder zu verfaͤlſchen` | Missing "o" |

**Uncertain / flagged:** none.

---

## PDF pages 23–24 (a numbered list spanning a page break — numbering error)

**Raw OCR** (page 23 ends, page 24 begins):
> 7. Steht eurem Amt in der buͤrgerlichen Geſellſchaft mit Treu und Eifer vor;
> denn ſeyd ihr dort nachlaͤßig, ſo werdet ihr es auch bey uns ſeyn. |
>
> 8. Ver⸗
>
> 4
>
> 9. Verbreitet Wiſſenſchaften, Kuͤnſte, Induſtrie, geſellſchaftliche Neigungen,
> und Tugenden, und hindert, was ihnen ente gegen ſteht.
>
> 9. Darum betrachtet ſich auch der Orden in dieſer Klaſſe als eine gelehrte
> Geſellſchaft, wobey das Beyſpiel und Unterricht den Verſtand leiten und das Herz
> beſſern.

**Corrected:**

7. Steht eurem Amt in der buͤrgerlichen Geſellſchaft mit Treu und Eifer vor; denn
ſeyd ihr dort nachlaͤßig, ſo werdet ihr es auch bey uns ſeyn.

*[page break — item 8's number is restated at the top of the next page, a real
printing convention this book uses for a list item split across pages; "4" is that
next page's printed page number]*

8. Verbreitet Wiſſenſchaften, Kuͤnſte, Induſtrie, geſellſchaftliche Neigungen, und
Tugenden, und hindert, was ihnen entgegen ſteht.

9. Darum betrachtet ſich auch der Orden in dieſer Klaſſe als eine gelehrte
Geſellſchaft, wobey das Beyſpiel und Unterricht den Verſtand leiten und das Herz
beſſern.

**Corrections made:**
| Raw OCR | Corrected | Type |
|---|---|---|
| `ſeyn. \|` | `ſeyn.` | Stray pipe, noise |
| `4` (isolated) | *(page-footer number, not body text)* | Page-transition noise, as elsewhere in this corpus |
| `9. Verbreitet Wiſſenſchaften...` | `8. Verbreitet Wiſſenſchaften...` | **Numbering error, not a spelling error — the more consequential class of mistake in this sample.** Confirmed directly against the scan: page 23 ends "8. Ver⸗" (item 8's number plus the first word-fragment, split by the page break) and page 24 restarts with "8." again before completing "Verbreitet..." — the printer's own convention for a list item split across a page. The raw OCR misread this second "8." as "9.", which would silently renumber every item from here on by one if not caught (a scholar citing "rule 9" downstream would be citing the wrong rule). The true item 9 is the next paragraph ("Darum betrachtet..."), correctly numbered "9." in the raw OCR by coincidence. |
| `ente gegen ſteht` | `entgegen ſteht` | Spurious word-break, no hyphen mark present (OCR just added a space) |

**Uncertain / flagged:** none — resolved with high confidence by direct comparison of both page images.

---

*(More pages to be added here as the representative sample is built out.)*