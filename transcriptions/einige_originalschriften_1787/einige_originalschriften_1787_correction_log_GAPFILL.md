# Einige Originalschriften (1787) — Phase 3 Correction Log, Gap-Fill Burn

AI-assisted first pass (Claude Opus 5.5, 2026-10-18), by direct visual comparison of 200-DPI
renders of the scan against the raw OCR text layer (`pdftotext` per physical page). Provisional
until human review. f/ſ (long-s) and missing combining-e (uͤ/aͤ/oͤ) fixes are applied silently.
Printed page numbers are recorded as `[printed p. N]`; catchwords and signature marks are dropped.
Paragraphs are reflowed and page-internal line-end hyphens joined; a word split across a page
break is kept with `⸗` at the page end. Covers the pages missing from corrected.txt after the
2026-10-18 A–F burn (pp. 1-24, 67-92, 126-160, 187-228, 266-296, 327-364, 385-428).

- page 1-4 — no OCR text; cover board, flyleaf with handwritten library shelf notes ("#24", "36+"), blank flyleaves — described, not transcribed
- page 5 — title page; corrections per pilot eval sample (verified against scan): "des" restored (dropped), "Hauspifitation" → "Hausviſitation", "kandshut" → "Landshut", "78%" → "1786.", "Mun ch e n" → "Muͤnchen", stray "|" and "5" dropped
- page 6 — epigraph; clean, line-end "Ein⸗/ſicht" joined, stray "." after "in" dropped
- page 7 — per pilot: "7 8 egenwaͤrtige" → "Gegenwaͤrtige" (drop-cap missed; "7 8" stamp noise), "80 . det" → "von dem", "Illa-ininaten" → "Illuminaten", "Sefte An" → "Secte, als", "der zu" → "oder zu", OCR line scrambling ("man", "zu" displaced) restored; catchword "Wer" dropped
- page 8 — clean; ornament (three asterisks) omitted
- page 9 — "Petites Lettres" (OCR "petites"); "fo viele" → "ſo viele"; "Wörter," → "Woͤrter."
- page 10 — Internet Archive digitization notice; not 1787 text, bracketed note only
- page 11 — cipher table fully garbled by OCR ("i 06 17, 0052 0:9. 98 Te ...") — rebuilt from scan: 12…1 = a…m, 13…21 = n…w, 22-24 = x,y,z
- page 11 — calendar list garbled ("SSunius", "Vd nu.", months 3-5 names dropped) → "3. Chardad … Junius", "4. Thirmeh … Julius", "5. Merdedmeh … Auguſtus" restored
- page 11 — "r. Pharavardin" → "1. Pharavardin"; signature "A" and catchword "6." dropped
- page 12 — calendar months 7-11 almost entirely garbled ("& ss", "&ftobe", "1. nen)", "SIEHUar.", "Binnen") → rebuilt from scan: Meharmeh/Oktober, Abenmeh/November, Adarmeh/Dezember, Dimeh/Januar, Benmeh/Februar; "8. Aben men" → "8. Abenmeh."; "32. Asphandar" → "12. Asphandar"
- page 12 — "NOMINNA. GEOGRAPHICA CV" → "NOMINA GEOGRAPHICA / PROVINCIÆ."; "NR BN U M." → "URBIUM."; "Hlyricum" → "Illyricum"; "Ansiochia" → "Antiochia"; two-column table re-paired (OCR emitted columns separately); catchword "Landshut," dropped
- page 13 — "Chalios" kept as printed; "Theſlalonica" → "Theſſalonica"; "Solzburg" → "Salzburg"; "Hleuſis" → "Eleuſis"; "peo non confcüs" → "pro non conſciis" ("peo" is a printer's slip for "pro" in the scan, normalized; flag for review)
- page 13 — "17768= 41:78" → "1776 — 77 — 78"; member list rebuilt: "T. May 7285 |" → "1. May 1776.", "VIEH. Aijax" → "777 Ajax", "283 Seipio" → "783 Scipio", "284 Cellus Ar" → "784 Celſus A.", "2g. Jul." → "28. Jul.", "278°.Tamerlan. II. … 17 7%" → "786 Tamerlan. Ill. … 16. Dec. 1776."; signature "A 2" and catchword "787" dropped
- page 14 — member list re-paired with dates (OCR separated columns); "289 Taſſo" → "789", "201 Democritus" → "801", "Perieles" → "Pericles", "Oſiris"/"Taſſo" long-s, "2 7. NOV." → "27. Nov."; dates for 795, 803, 806, 808-813 restored from scan; catchword "818" dropped
- page 15 — member list re-paired with dates; "878 Stilpe" → "818 Stilpo", "Deucalton" → "Deucalion", "3821" → "821", "Diomedes NI." → "Diomedes M.", "8380" → "830", "TO. Schahar" → "10. Schahar", "2. Mehar." restored (dropped), year "1779." restored (dropped)
- page 15 — section heading "V." restored (dropped); "Stucke" → "Stuͤcke"; "41 Vorſchlag" → "1. Vorſchlag"; "konnte" → "koͤnnte"; drop-cap D; catchword "Orden" (begins p. 6) kept as text start of next page
- page 16 — "Charakteren" → "Characteren" (as printed); "Geuuͤgen" → "Genuͤgen"; "Separierte" → "ſeparierte"; "unbekanne" → "unbekannt"; "Mans ner" → "Maͤnner"; "O (Ordens)" → "☉ (Ordens)"; "wis ren" → "waͤren"; "Beguüͤgung" → "Begnuͤgung"; "1 anf 2 Oktavblaätteen" → "auf 2 Oktavblaͤttern" (stray "1"); catchword "kurze" dropped
- page 17 — "Maunheim" → "Mannheim"; "a MAN WHEIM" → "à MANNHEIM"; "Prosreffen" → "Progreſſen"; "O Syſtem" → "☉ Syſtem"; "ebe Illum." → "kleinere Illum." (word misread); "L] (Loge)" → "▢ (Loge)"; "Cord" → "Corinth"; catchword "laͤrmen," dropped. Note: "beſtehet nun in Griechenland allein aus" — the number is left blank in the print itself
- page 18 — "[ä hinfahren" → "▢ hinfahren"; "fhone" → "ſchoͤne"; "Der D" → "Der ☉"; "a Bürger" → "und Buͤrger" (line order restored); "[I nach unſerm Sytem" → "▢ nach unſerm Syſtem"; "[◻ zu" / "national [_]" → "▢"; "Er O r eien" → heading "Progreſſen" (garbled); "polttiſchem" → "politiſchem"; "des O" → "des ☉"; catchword "fernt," dropped
- page 19 — every ☉ misread as "D"/"O" (5×) restored; section numbers 2/3/4/5/6 restored where OCR gave "5"/"0"/"I"/"„"; "find alle" → "ſind alle"; "unſem" → "unſerm"; "Wuchern" kept as printed; "Benelicien" → "Beneficien"; stray "|", "15", "“" noise dropped; catchword "7." dropped. Note: item 3 ends dangling "Und alſo" as printed (runs into item 4)
- page 20 — "Ephelus" → "Epheſus"; "Univerlität" → "Univerſitaͤt"; "eiſen" → "Reiſen"; "der O Mitglieder" → "der ☉ Mitglieder" (☉ restored 6× incl. one dropped after "dem"/"vom"); "Io;"/"ZI;" → "10."/"11."; "eben o" → "eben ſo"; "VBartholo⸗" → "Bartholo⸗"; catchword "hen;" dropped
- page 21 — "verjehen:" → "verſehen."; "konnen" → "koͤnnen"; "hoſſen" → "hoffen"; "O Anſtalten" → "☉ Anſtalten"; scrambled dash run re-ordered from scan ("durch — — — — — — —"); "Reve- nuen" → "Revenuͤen"; "Million" → "Miſſion"; "Univerätät3" → "Univerſitaͤts"; "IIlum." → "Illum."; final redaction dashes restored ("und — — — — —, — — — — — —."); stray "W" and catchword "VI." dropped
- page 22 — drop-cap "Sy" → "Da"; "vernüͤnftige" → "vernuͤnftige"; "I." → "1."; "fo mehr"/"fo größere"/"fie" → "ſo"/"ſo groͤßere"/"ſie"; "gebühe rend" → "gebuͤhrend"; catchword "de," dropped
- page 23 — "Bor: gleiche" → "oder gleiche" (word misread); "mehr." → "mehr" (spurious period); missing comma "bedienen, die" (per scan); "fo"→"ſo" (4×); catchword "8. Ver⸗" dropped (pilot confirms item 8 restated on p. 14)
- page 24 — "9. Verbreitet" → "8. Verbreitet" (numbering misread; per pilot); "entegegen" → "entgegen"; "Meynung an, Art," line scramble restored ("auf eure Art, nehmt keine Meynung an"); "umſtaͤnden" → "Umſtaͤnden"; "IT." → "11."; "1) … Folgen, und loͤſet" line order restored; "42 Uebt" catchword dropped (page 25 already in corrected.txt starts "4) Uebt")
