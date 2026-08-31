# Anhang — Correction Log

Full-document Phase 3 correction, page by page. Lighter-weight companion to
`anhang_1787_eval_sample.md` (which has the detailed before/after narrative format
used for the initial pilot) — same method and status, different format because a
full quoted-paragraph table per page doesn't scale to a whole document. One line
per correction: page — raw OCR → corrected — reason. The actual corrected German
text is in `anhang_1787_corrected.txt`; this file is the citable change record for
it.

## Methodology & status
Same as `anhang_1787_eval_sample.md`: corrections made by Claude (Sonnet 5) by
direct visual inspection of page images (`pdftoppm`, 300 DPI) against the raw OCR.
AI-assisted first pass, not a final scholarly correction — pending human review.
Spelling preserved as printed (long ſ, etc.); this document's raw OCR (from MDZ)
lacks ſ and line-break hyphens systemically — see `anhang_1787_provenance.md` — so
nearly every word with a medial/initial "s" needed ſ restored; those are not
itemized individually below except where something else is also wrong, to keep
this log readable. Only content-level fixes (misreads, dropped words, spurious
noise, numbering errors) are itemized in full.

## Page 1 (title page)
- `hdchsten` → `höchſten` — misread (d/ö)
- `sind .` → `ſind.` — missing long-s + spurious space before period
- `Frankfurt und Leipzig , ;` → `Frankfurt und Leipzig,` — stray semicolon, noise

## Page 2
Blank page (verso of title page, ink bleed-through only). No corrections needed —
raw OCR correctly shows no content here.

## Page 3
See `anhang_1787_eval_sample.md` for the full detailed entry (this was the pilot
page). No changes to repeat here.

## Page 4
- `die Cie` → `die Sie` — misread (C/S)
- `jedem uns befangenen` → `jedem unbefangenen` — misread
- `kouwen` → `können` — heavily garbled
- `jes mahls` → `jemahls` — misread + wrongly split
- `Vorjekt` → `Vorjetzt` — misread ("tzt" as "kt")
- `meis ner` → `meiner` — misread + spurious split
- `before derte` → `beförderte` — misread + spurious split
- `Illuminaten - Papiere` → `Illuminaten-Papiere` — spaced hyphen should be tight
- `beståt . tiget` → `beſtätiget` — spurious split + å/ä character substitution
- Several straightforward missing-umlaut/missing-long-s/spurious-mid-word-period
  fixes not separately itemized (durfte→dürfte, überflußig→überflüßig, mogen→mögen,
  begnuge→begnüge, ha ben→haben, Bruchstucken→Bruchſtücken, mei.ne→meine,
  vorgefun.dene→vorgefundene, hochsten→höchſten [x2], ver.schiedenen→verſchiedenen,
  erha benen→erhabenen, nothige→nöthige, angekundeten→angekündeten)

## Page 5
- `Iluminatenschriften` → `Illuminatenſchriften` — missing double-l + long-s
- `i :` → *(removed)* — stray printer's mark/noise, not text
- `seke` → `ſetze` — misread
- `1776 bis 1781` — dates confirmed correct as printed, no change
- `beschehenen Extra , 2 3 1` → `beſchehenen Extra-` — trailing "2 3 1" is
  page-footer noise (a garbled signature mark, "A 3" per the actual page image);
  "Extra-" is a genuine catchword continuing "Extradition" on the next page
- Straightforward umlaut fixes not separately itemized (Grunde→Gründe,
  willkurlich→willkürlich, vorzuglich→vorzüglich)
- Spurious mid-word spaces not separately itemized (be treffen, an gemerket,
  Samm lern, ent weder, Stel len, schul digen)

## Page 6
- `aufbe . wahite ba` → `aufbewahrte.` — badly garbled, plus stray noise "ba"
- `Areopagiten . Verträge` → `Areopagiten-Verträge` — period should be a hyphen
- `St- und C -` → `St— und C—` — these are **redacted names** (dash standing in
  for a name, same convention as the main volume's "unſem — —, —, und —" — see
  `lessons_learned.md`), not just a formatting fix
- `Mandate.dn . お` → `Mandate.` — trailing garbage includes a stray Japanese
  hiragana character (お) — pure OCR noise, about as clear an example as this
  corpus has of "the OCR engine produced something with zero relationship to the
  source"
- `Ci culare` → `Circulare` — misread, dropped "r"
- **List-numbering errors** (second instance of this error class in the project,
  after the main volume's rule 8/9 — see `todo.md` Phase 3): raw OCR's `a) Zwey
  Reden...` should be `d) Zwey Reden...`, and raw OCR's `c) Alle` (trailing, page
  end) should be `e) Alle` — confirmed against the actual list structure (items
  a-g) visible on the page image. If uncorrected, a reader citing "item a" or
  "item c" here would be citing the wrong item.
- `Ordens Schriften` → `Ordens-Schriften` — missing hyphen
- Straightforward long-s/spurious-space fixes not separately itemized (genauest,
  Un tersuchung, kur fürstlichen, ausser, Gegenstand, Ingolstadt, Versammlungen,
  abgelesen ha Ben, am be Ten)

## Page 7
- `ausge . hört` → `aufgehört` — genuine misread ("ausge"→"aufge"), not just a
  spurious period; "ausgehört" isn't a real word, "aufgehört" (ceased) is
- `Diese hatten` → `Dieſe hätten` — missing long-s *and* missing umlaut changes
  the grammar (indicative "had" → subjunctive "would have"), not just spelling
- `Driginalten` → `Originalien` — misread (D/O, "ten"/"ien")
- `porlegen` → `vorlegen` — misread (p/v)
- `heist` → `heißt` — missing ß
- `CaA 4 2.1 . noni 1 2` → `Ca-` — the name being split at the page break
  ("Ca-noni...", likely a surname, probably continues "Canonici" or similar on
  the next page, not yet corrected); "A 4" is the signature mark, "2.1"/"1 2" pure
  noise
- Straightforward long-s/umlaut/spurious-space fixes not separately itemized
  (Neujahrs . Sendschreiben, meist von ih.rer, Handschrift, Zusammenhang,
  Gesellschaft, Rich ter, ge druckt, Gluck, Bedur fen, fast, Stucke, Zwackischen,
  Hausvisitation, vorgefunden ha.ben, be haupten, inclusive abge.druckte)

## Page 8
- `dortmahls hls eben einen solchen Pack Pack Papiere` → `dortmahls eben einen
  ſolchen Pack Papiere` — **duplicated tokens** ("hls", "Pack"), a new OCR failure
  mode not seen in pages 1-7 (distinct from misreads/spurious splits)
- `Inſtructiones infinuatorum` → `Inſtructiones inſinuatorum` — missing long-s;
  this and `la Profeſſion de foi` are real historical document titles (see
  annotations)
- `Ausnahms . Protokolle` → `Aufnahms-Protokolle` — misread ("Ausnahme"/exception
  vs "Aufnahme"/admission — meaningfully different word, not just spelling)
- `davon hätte abfondern` → `davon hätte abſondern` — f/ſ misread
- `210 1 1m0 .` → *(page-footer noise, then catchword `1mo.`)* — "1mo." is Latin
  ordinal abbreviation ("primo", firstly), confirming a numbered list follows
- Routine long-s/umlaut/spurious-space fixes not itemized (niedergesekten,
  Urs sachen, Schrif ten, bey.sammen, Hier→hier, Stucke, nă hers→näher,
  zuruckhalten, niedergesezet, wurde→würde, daruber, Verthei digung)

## Page 9
- `Aufsaß` → `Aufſatz` — misread
- `foiglich` → `folglich` — misread (i/l)
- `ge Hore` → `gehöre` — spurious split + wrong capitalization
- `15 Ne` → *(footer noise, catchword corrected to)* `Ue.` — misread N/U
- Routine fixes not itemized (mußigen→müßigen, ehemah.lige, Bruder→Brüder,
  wis sen, Ordens.System→Ordens-Syſtem, Aeusserung, daruber→darüber,
  Ordens Einrichtung→Ordens-Einrichtung, ver rathen, Ausfuhrung, ge kommen)
- **Content note**: this whole page is the writer denying he ever implemented a
  proposed "Weiberorden" (women's order) — see `anhang_1787_annotations.md`

## Page 10
- `Anmer kung sehen` → `Anmerkung ſetzen` — genuine misread ("sehen"/to see vs
  "setzen"/to place), not just the obvious spurious space
- `auf a Octavblättern` → `auf 2 Octavblättern` — numeral 2 misread as letter "a"
- `Demoiſellés` → `Demoiſelles` — spurious accent added (French word, no accent on
  final e)
- `zu kändigen` → `zuſtändigen` — significant misread, not cosmetic
- `versehen` → `verſetzen` — misread changes meaning ("to provide" vs "to place
  into")
- `daß fie` → `daß ſie` — f/long-s confusion
- Routine fixes not itemized (ausserst→äuſſerſt, Hausvisita.tion, franzöſi.scher,
  Munchen→München, Blåttern→Blättern, wel ches, geslissentlich→gefliſſentlich,
  et.was, Stucke, vorstellen konn ten, ganz ge nau)
- **Content note**: identifies a specific seized item as an unrelated satirical
  pamphlet from his wife's papers, arguing the government's editors
  mischaracterized it — see `anhang_1787_annotations.md`

## Page 11
- `politischen Sache` → `politiſchen Fache` — S/F misread, real word change
  ("Sache"/thing vs "Fache"/field-sphere)
- `ohnmsglich` → `ohnmöglich` — misread
- `Befiß find` → `Beſitz ſind` — misread (r/tz-like confusion, f/long-s)
- Routine fixes not itemized (Ordens.Progressen, Ordens.System, Or.den, ado.→2do.,
  sey be wirket, ent.weder, Last→Laſt, ift→iſt, Jesuis ten, ges kommen, notorisch,
  durchs aus, Ordens Geistlichen)
- **Structural finding, not just a correction**: this page's footnote (marked *)
  refers to "der Verfaſſer dieſes Schreibens" (the author of this letter) in the
  third person — the footnote is the *Anhang*'s editor/publisher inserting a
  rebuttal into the reprinted letter, not part of the original letter itself. See
  `anhang_1787_annotations.md` — this affects how the whole document should be read.

## Page 12
- `får` → `für` — misread
- `wurde` → `würde` — missing umlaut changes tense/mood (subjunctive)
- `Gesek` → `Geſetz` — misread
- Routine fixes not itemized (Ordens Mitglied→Ordens-Mitglied, eis ner→einer,
  Verbind lichkeit, Fursten, gu ten, uberhaupt, Staatsburger, ge.handelt,
  Ordens.Progressen, gefuhret, Professors.Stellen, ents fernen, Convertiten -
  Cassa→Convertiten-Caſſa)

## Page 13
- `Etiftun . gen` → `Stiftungen` — misread (E/S) + spurious split
- `wurde` → `wurde` — **confirmed correct as printed**, no change (past-tense
  indicative is right here, unlike page 12's `wurde`→`würde`; context decides,
  not a blanket find/replace)
- Routine fixes not itemized (Schul.Curatel, Jesuiten.Ordens, miß.brauchet,
  Einfuhrung, Maltheser, besseren, vers wendet, Grunde→Gründe [x3], Ge.schaft,
  behan delt, hochsten, Råthe→Räthe, wirks lich, Anempfeh lung, Professorsstellen)

## Page 14
- `Unterstigung` → `Unterſtützung` — misread
- `unwirdigen` → `unwürdigen` — missing umlaut
- Routine fixes not itemized (wurden→würden, mußte→müßte, Pråjudiz→Präjudiz,
  drit.ten, gegrundete, Anspruche, nam liche, be kannt, Empfeh lungen, wes niger,
  offentliche, Geg ner, aufs fallender, consequenten, uus→uns, begunstigt,
  Jesuitische, dukk den→dulden)
- **Correction to my own earlier annotation**: see the note at the end of this
  log — the footnote here (2nd instance) makes clear I misread the footnote
  voice's stance on page 11.

## Page 15
- `fub n . 34 et 5` → `sub n. 34 et 5` — misread f/s; this is a real Latin
  citation ("sub numero 34 and 5" — under item numbers 34 and 5), not prose
- `Rirchengelder` → `Kirchengelder` — misread R/K
- `Verfajer` → `Verfaſſer` — misread, dropped letters
- Routine fixes not itemized (mildthatige, freywile lige, dew→den,
  Illuminaten.Ordens, ver danken, offentliche, uber, Ordens.Mitgliedern,
  beseket, zugegan gen, we.niger, find→ſind, Hatten→Hätten, wurde→würde,
  Ordens:Progressen, Raths.Fiscal, Dispo.→Dispo-, wenigs stens, ber sure
  mich→berufe mich, Hånden→Händen, aufzuwe zeichnen→aufzuzeichnen)
- **New code name / figure**: "Pylades" introduced as an order member who became
  "geiſtlicher Raths-Fiſcal" (an ecclesiastical council legal/financial officer)
  — see `anhang_1787_annotations.md`.

## Page 16
- `uns fern` → `unſern` — long-s missed, word wrongly split in two
- `Ordens . Borschritt` → `Ordens-Vorſchritt` — misread B/V
- `Nath` → `Rath` — misread N/R
- `1s Råthen` → `12 Räthen` — numeral 2 misread as "s"
- Routine fixes not itemized (Haus.wirthschaft, Unterſtügen→Unterſtützen,
  äusserst be.denklich, Casse, Rirchengelder [see above], mil de Stiftungen,
  befragt hatte→hätte, wurde→würde, Ausdrucke, wa ren, Interessen)
- **Redacted names**: "unſern — — — und — —" — another instance of the
  dash-redaction convention (see `glossary_people_and_terms.md`), naming (with
  names withheld) parties whose mismanagement of funds the order's loans
  apparently helped correct.

## Page 17
- `Disposi in derselben` → `Diſpoſition derſelben` — misread "tion" as "in"
- `diesem dran von Wucherern` → `dieſem drey von Wucherern` — misread "dran" for
  "drey" (three)
- Spurious `*` after "anders" with no corresponding footnote on this page —
  treated as noise, not a missing footnote marker
- Routine fixes not itemized (hoch.sten, konne, Sticke ausserst gewissen haft,
  Standhaf tigkeit, nothi gen, Iluminaten→Illuminaten, Vermögens.Umstände, Si
  cherheit fur, uberzeuget, daruber re!ferir.→darüber re-/ferir-)

## Page 18
- `Aussage` → `Aufſätze` — real misread ("statement" vs "essays/articles"),
  not cosmetic
- Routine fixes not itemized (gunstigen, Kurfursten, zu ei.nem, Anempfeh lung,
  anempfoh lenen, wie.derhohle, nochmah.len, Aeusserung, Personen...ers
  hielten→Perſonen...erhielten, durfe, abge druckte, Ordens Schriften, Ab.
  anderung)
- **Biographical detail**: "des verſtorbenen Pylades" — confirms Pylades had
  died by the time of this writing.

## Page 19
- `so kanit profes negotium` → `ſo kann großes negotium` — real misread, not
  cosmetic
- Note: raw OCR's `wahrlich` is **already correct as printed** — double-checked
  against the image; my first-pass reading of the scan mistakenly suggested an
  umlaut here, corrected before it reached the output file. Logged so the false
  start doesn't get silently repeated.
- Routine fixes not itemized (istes.→1ſtes., Ordens.Bruder, wel cher, prote &
  ionem fui patroni accisfren→protectionem ſui patroni acciſsfrey, det
  Ordens.Casse→der Ordens-Caſſe, Übrigen→übrigen, errathett→errathen, Veran
  lassung, handlungsgeschäften→Handlungsgeſchäften, keitt→kein)
- **New code name**: "Coriolan," introduced as one of the order's first
  subordinate members, raised in merchant/trade business.
- **Significant content**: a described scheme to place an order member near a
  foreign ambassador's retinue to run duty-free trade for the order's financial
  benefit — see `anhang_1787_annotations.md`.

## Correction to an earlier annotation (important)
Page 11's footnote was initially annotated as a "hostile government editor"
voice. Pages 14 and 15 each have their own footnote, and both make clear that's
wrong: p.15's footnote explicitly says "auf das Verzeichniß **unſerer**
Mitglieder" (our members) while disputing a specific factual claim made by "den
Verfaſſer" (the author, i.e. the letter-writer) — this is someone
Illuminati-aligned (most likely the Anhang's actual compiler/editor)
fact-checking specific claims in the reprinted letter, not a hostile prosecutor
rebutting the whole defense. Re-reading page 11's footnote with this corrected
lens, it's consistent: "die uns gar nicht zur Laſt fallen" reads as "[claims]
that don't even count as a problem for **us** [the cause]" rather than "charges
**we** [the prosecution] aren't even making." Full correction written up in
`anhang_1787_annotations.md` and `glossary_people_and_terms.md` — flagged here
too since it affects how every footnote from p.11 on should be read.

## Page 20
- `speculicte` → `ſpeculirte` — misread
- `Ordens . Ein , richtung` → `Ordens-Einrichtung` — misread comma for hyphen
- `Ordens , Ziffern` → `Ordens-Ziffern` — misread comma for hyphen
- Routine fixes not itemized (Caffe→Caſſe, ver.schaffen, verschie dene, Aufsäke,
  Universi tåt, Munchen, zuruckkam, Muhe, ordentli chen, auszufuh ren, zuruck,
  konnen, Publi cum)

## Page 21
- `lektere` → `letztere` — misread
- `Bz` → `B 3` — footer signature misread
- Routine fixes not itemized (Ordens.Personale, je mand, uns ter uns
  hatten→unter uns hätten, Ausserdem, Betrugeren→Betrügerey, Auffüh rung, an.dern,
  woruber, mitwir.kenden, hatte→hätte, konnen)

## Page 22 — sensitive content, see annotations
- `Desgleichen` → `Deßgleichen` — missing ß
- `Illuminaten , Schriften` → `Illuminaten-Schriften` — misread comma for hyphen
- `Maßenhaußen` → `Maßenhauſen` — misread ending (a real surname, "von
  Maßenhauſen" — see annotations)
- Routine fixes not itemized (Pub ficum→Publicum, Beschreibun gen, vors geleget,
  vorsins dig, Stucke, ſebet→ſetzet, wahrlich , nicht, uners laubte, beweiset,
  dens jenigen, denjes nigen, dermahs ligen)
- **Sensitive content, factually documented, not editorialized**: this page
  names "die Handſchrift des Ajax" (a code name) as the source of machine/recipe
  descriptions including one attributed to "aqua Toffana" and several "ad
  procurandum abortum" (for procuring abortion) — see
  `anhang_1787_annotations.md`.

## Page 23
- `Rirchers` → `Kirchers` — misread R/K; this is **Athanasius Kircher**, a real
  17th-century Jesuit polymath — see annotations
- `Necepte` → `Recepte` — misread N/R
- Routine fixes not itemized (Gesek vor.handen, al.les Ausfallende, Kunsten,
  Wissen.ſchaften, mus→muß, Buchern [x2], Maßenhausen→Maßenhauſen, siket→ſitzet,
  zeich nete, erin.nere, fubterraneus→ſubterraneus, weitlä&uftiges, zuzubereis
  ten, offentlichen)

## Page 24
- Routine fixes only, no major content-level misreads beyond the systemic
  long-s/umlaut/spurious-space pattern (Maßenhausen→Maßenhauſen [x2],
  Stucke→Stücke, foo gar→ſogar, Kunste→Künſte, großere Samm lung, konnten,
  ver.schiedene Stucke, Arz , nenen→Arzneyen, ver.ordnet, Steff→Stoff,
  Hausvisitations , Commission→Hausviſitations-Commiſſion, dies ses→dieſes,
  gestandig, Iluminaten→Illuminaten)
- `৯` → *(removed)* — a stray Bengali-script digit, pure OCR noise. **Second
  instance of this failure mode** (first was "お", a Japanese hiragana
  character, on page 6) — non-Latin-script noise seems to recur occasionally in
  this document's OCR, worth watching for.

## Page 25
- No major content-level misreads beyond the systemic pattern (Stucke, of.
  fentlich, Original.schriften, nußliche→nützliche, her.ausgenommen,
  offentlichen, Cris minalrichter, des.wegen, abgetrie ben, Handlun gen, sole
  chen, hdren→hören, Mas.senhausen→Maſſenhauſen, V 5→B 5)
- This page contains the letter-writer's own direct rebuttal of the poison/
  abortion implication from p.22-23 ("Iſt er deswegen ein Giftmiſcher, hat er
  Kinder abgetrieben?") — see `anhang_1787_annotations.md`. Translate this
  passage with particular care when Phase 4 reaches it; it's a direct denial of
  a serious accusation, not incidental text.

## Page 26
- `Word` → `Mord` — misread W/M ("Word" isn't German; "Mord" = murder)
- `chne` → `ohne` — misread
- Routine fixes not itemized (måsten, distilli ren, Långstens, Buchern, mußte,
  hochst, hatte, je der, wurde, an bere, Ingrediensien, bengefallen, Måne ner,
  beste.Het, Blen, lesteres, ruset, Nes cepte, befurchtenden, kurfürstlicher)
- **Real historical reference**: "Archenholz" — Johann Wilhelm von Archenholz, a
  real 18th-century German historian/writer, cited as having given a more
  plausible account of the poison's real ingredients elsewhere. Not yet
  independently verified which specific work is meant.

## Page 27 — major identity clue
- `ruket` → `rußet` — continuation of prior page's catchword, misread
- `perfcrutatur` → `perſcrutatur` — misread f/long-s (Latin: "searches out")
- Routine fixes not itemized (mussen, vorherge gangene, ben mir→bey mir,
  vortraglich, Eigena thum, wåre, Petschirstes chern, fålt, se wie, Sigil→Sigill)
- **Major finding**: "Wappenſammlung des **Philipp Zwackhius**" — the seal/
  heraldry collection is named as belonging to "meines Bruders eines Studenten"
  (my brother, a student). This is the strongest identity clue yet for the
  letter-writer — see `anhang_1787_annotations.md`.

## Page 28
- `van` → `von` — misread
- Routine fixes not itemized (Sticke, Maßen haußen→Maßenhauſen, Nachtheil.der,
  je des Ordens.Mitglied, ausser, be.schweren→beſchwören, Samm lung, Ma
  schinenzeichnungen, 1 5to.→5to., Selbstmorder→Selbſtmörder, gange→ganze)
- **Real literary reference**: "Werthers Leiden" — Goethe's _Die Leiden des
  jungen Werthers_ (1774) — the letter-writer says a passage on suicide was
  copied from this famous novel and wrongly attributed to him. See annotations.

## Page 29
- `tiden` → `tödten` — misread ("to kill")
- `får` → `für` — misread å/ü
- Routine fixes not itemized (weltli chen, vor.gehabten , Selbstmords, Aufsäße,
  so fast, niederge.ſchrieben, Be ruhigung, ha ben, Sunde, daruber, reumuthig,
  schame, in mic→in mir, Hike→Hitze, gedampfet, Bey.spiel)
- **Significant biographical content**: a first-person account of a suicidal
  period at age 19, connected to a "Generalbeicht" (general confession) found
  in the house search — see `anhang_1787_annotations.md`. Handle with care in
  translation; this is sensitive personal material, not just polemic.

## Page 30
- `Weltern` → `Aeltern` — misread ("parents", not a plausible near-miss, a real
  misread)
- `to Jahren` → `10 Jahren` — numeral 1 misread as letter "t"
- Routine fixes not itemized (met nem, Ungluck eitt, jest, Baierischett,
  burgerliche, Handlun gen, einest, zugefugt, ges gen, rechtfer tigen, Cha
  rakters, fub→sub, einent, dusserliche, moralischett, we che, fur borti→für
  dorti-)
- **Biographical detail**: "ſeit 10 Jahren treu geleiſtete Dienſte" — confirms
  the writer had served the state/prince for 10 years by the time of writing —
  useful for narrowing an identification.

## Page 31
- `988.` → `188.` — numeral misread (1→9), changes a page-range citation
- Routine fixes not itemized (Freymichigkeit, wunschte, une vorsichtigkeit,
  Ordens.Brú.dern, michte, Ge danken, erlau.ben, die sem, ma.che, verdiene tch,
  Ordens.Correspondenz, ofters, Die Illuminaten.Schriften, moglichstem, fie,
  zuruckbehalten)

## Page 32
- `& Tage` → `8 Tage` — numeral 8 misread as ampersand
- Routine fixes not itemized (mogen, an.dern, Diese→dieſe, Hausvist.tation,
  hatte→hätte, ver.heimlichet, ste→ſie, Gute mei.ner, Ord.nung,
  unterdruckten, niemah.len, schopfen, wurde→würde, incompetenten
  Nichter→Richter, Feins den, Uebrigens hatte→hätte, vor.gefundene,
  ge 1.babt,→ge-/habt,)

## Page 33
- No major content misreads beyond the systemic pattern (mei ner, Grunde,
  jest, Guter, eta brochen, Oб.rigkeiten [see below], gegrundete, auslie fern
  wurden, konnen, Hånden, niedergesekten, lång.ftens)
- `Oб` → `Ob` — **third instance of non-Latin-script OCR noise** (a Cyrillic
  "б"), following "お" (p.6) and "৯" (p.24) — now a well-established recurring
  failure mode in this document's OCR, not a one-off
- Confirmed spelling "Maßenhaußen" (with ß) matches this page's actual print,
  differing slightly from earlier pages' "Maßenhauſen" — kept as printed rather
  than forced to a single "corrected" spelling, since minor spelling variance
  within one document is period-plausible and not clearly an OCR error here

## Page 34
- `R` (isolated) → *(removed)* — noise, not text
- Routine fixes not itemized (Munchen, gefun.den, konnen, ubrige, beruhrt,
  Ci.vilarrest, Forde.rung, De.duction, S. 322. an , gezogenen, Tag ,
  buchs, Kurfürsten)
- **Real historical references**: the writer mentions a legal brief he wrote
  concerning "des Erzſtifts Salzburg" (the Archbishopric of Salzburg) and a
  diary/journal he kept "von der Krankheit Max. des letzten Kurfürſten in
  Bayern" — likely Maximilian III Joseph, whose 1777 death ended the direct
  Bavarian Wittelsbach line. Not yet independently verified.

## Page 35 — the letter is signed
- `Dero` — **entirely missing from raw OCR**, restored from the image (another
  whole-word omission, like the main volume's "des" — see `todo.md` Phase 2)
- `3 wackh` → `Zwackh` — **the letter's signature**
- `( 23 )` → `(L. S.)` — badly garbled; "L.S." = *Locus Sigilli* (Latin, "place
  of the seal"), a standard notarial mark
- `Franz Xav. v. Zwackh` — correctly read in the raw OCR, confirmed against
  the image
- Routine fixes not itemized (gewest, Kurfürstlichen , Hofrath,
  schrifftliche Anlan gen, beym Kurfurstlichen, ge standen, uneigennisig,
  Hofrathsordnungsmåßig, besonders Schweren, fleißig arbeitenden, Justiz
  beforderenden, ge zeiget, entsprechensten, Subordina tion, dergestalten
  vera C ball f→ver-/hal-)
- **Major finding — see `anhang_1787_annotations.md`**: this page identifies
  the letter-writer definitively as **Xaver von Zwack**, both by signature and
  by the attached certificate naming him in full with his real title
  (Regierungsrath zu Landshut, matching the main volume's own title page).

## Page 36
- `Welch .` → `Melch.` — misread (abbreviation for "Melchior")
- `Preyfing` → `Preyßing` — misread f/ß
- `( L. S. ) Ca` (stray fragment) → *(removed, layout noise from the seal
  marks)*
- `Instizcolegium` → `Juſtizcollegium` — misread + missing double-l
- Routine fixes not itemized (Parthen, Ih , me, geringste, vorges kommen,
  sen, Kurfürstl ., batte, volt, Gefangene nehmung, ju entgeben)
- **Real named officials, all with seal marks (L.S.)**: Melchior Graf von
  Preysing (Electoral Court Vice-President), Carl Freyherr von Pauli (Privy
  Councilor and Court Chancellor), Carl Albrecht Edler von Vacchieri (Imperial
  Knight, Court Vice-Director) — see annotations.
- **Significant footnote**: confirms Zwack fled Bavaria around 14 October
  1786 to escape arrest, despite these positive character references.

## Page 37
- `3wackh` → `Zwackh` — misread
- Routine fixes not itemized (Regie.rungspräsidenten, Hochgeehrte.1ster Herr,
  Gutigkeit, an , gelegnist, mussen, wunsche, Besol.dung, konnen [x2],
  Kräfsten, bentra.→beytra-)
- Beylage B: a real dated letter (20 July 1786) from Baron von Dachsberg,
  Regierungspräsident and Vicedom at Landshut, to Zwack — see annotations.

## Page 38
- `eeyden 0` → *(removed)* — noise
- Routine fixes not itemized (bose, Kenntnth, Muhe, fo haben, Kangler, måste,
  bep, (dermähligen, fobern, ohner acht, ben Directorial Plazen)

## Page 39
- Minor fixes only (Freundschaft, gehorsamer) — a clean, short page: Baron
  von Dachsberg's signature and date, closing Beylage B.

## Page 40
- Blank (ink bleed-through from page 39 only), matching page 2. No raw OCR
  content, no correction needed — confirmed against the image.

## Document complete
All 40 pages of the Anhang have now been corrected. See
`anhang_1787_annotations.md` for the consolidated significance of pages 27 and
35 (identity confirmation) and the sensitive-content handling notes for pages
22-25 and 28-31.
