# physicsaleveltutor.com

Static Astro site for AQA A-level Physics (7408) and AS (7407) at the root, with an Eduqas section (A420QS / B420QS) under `/eduqas/` (added 18 November 2026) and an OCR Physics A section (H556 / H156) under `/ocr/` (added 19 November 2026), deployed on Netlify. Built from the chemistryaleveltutor.com template with the `subject-revision-site` skill on 12 November 2026. Tutor: Rosey.

## Run locally
    npm install
    npm run dev        # http://localhost:4321
    npm run build      # writes dist/ (234 pages)

## Deploy
Push to `main` of the linked GitHub repository (`learn-beep/physicsaleveltutor`); Netlify builds with `npm run build` (Node 22) and publishes `dist/`.
Set `CROPS=off` in Netlify's environment to replace every AQA crop with a link to AQA's site.

## Data
- `scripts/export.py --bank "<Question Bank folder>" --topics topics.json --config site.config.json [--images [--only <bundle>]]`
  reads the AQA Physics question bank (`Dropbox\Teaching\Physics\AQA\Question Bank`: `data/index.js`, `data/img/*.js`) and writes `src/data/questions.json`, `papers.json`, `topics.json`, `spec.json`, `weighting.json`, and with `--images` the WebP crops under `public/img/<bundle>/` (5,125 crops, 105 MB).
  `--only` rewrites the data files with a single paper: always follow it with the full run.
- AQA Physics bank specifics handled in `export.py`: MCQ answers from the bank's `key`; AO as `[ao1, ao2, ao3]` marks (older mark schemes print no AO, so `aoText` is empty); practical parts from `RP`, `PS`, `AT` skill codes or the "Practical and data analysis" type; skills list keeps `MS`, `PS`, `AT` and `RP` codes; `cp` becomes `contextCrops` (the opening part of the question, folded out above later parts); paper codes `1`, `2`, `3A`, `3BA`–`3BE`.
- `topics.json` maps the 641 specification statements to 45 site topics (36 core topics in sections 3.1 to 3.8, nine for the five options). `scripts/make_topics.py` generated it from the bank's spec. `src/lib/groups.ts` holds the section groups, badges, where each is examined and the topic motifs.
- `site.config.json` holds the site line, WhatsApp wording, exam dates, grade boundaries and paper names; `src/data/tutors.json` holds Rosey's profile.

## Pages that differ from the Chemistry template
- `/formula-sheet/` (was `/data-sheet/`): the AQA data and formulae booklet section by section, and what is not on it. Named for the search demand ("a level physics formula sheet" 8,100/month UK).
- `/required-practicals/` (was `/practicals/`): RP1 to RP12 with what the papers ask, and every question tagged to each.
- `/maths-skills/`: MS 0.1 to MS 4.7.
- `/six-mark-questions/`: the six-mark extended responses (one per Paper 3B option paper, most AS Paper 1s).
- `/mechanisms/` removed.
- `/mock/` assembles AQA-shaped papers: A-level Papers 1 and 2 = 60 structured marks + 25 MCQ; Paper 3 = 45 marks Section A + 35 marks of the chosen option; AS Paper 1 = 70 structured; AS Paper 2 = 40 structured + 30 MCQ. Structured questions are kept whole.
- Question types: Multiple choice, Calculation, Show that, Explanation, Diagram or graph, Extended response, Practical and data analysis, Short answer.
- Grade boundaries out of 250 (85 + 85 + 80, unweighted). AQA sets a separate A-level boundary per Paper 3 option; the page shows the indicative subject boundaries (tutor2u's summary of AQA's data) and says so. AS out of 140 from AQA.
- Past-paper index: columns Paper 1, Paper 2, Paper 3A and the five 3B options.

## Content that needs the tutor's check before launch
- The nine key-term decks in `src/data/decks/` (`"checked": false` shows a "being checked" line).
- The formula sheet "learn these" list, the required-practical notes, the maths-skills notes and the six-mark level summary.
- Rosey's profile in `src/data/tutors.json` (no photo yet: the page shows an initial; add `public/tutors/rosey.webp`, 320×320, and set `"photo": "/tutors/rosey.webp"`).

## Upkeep
New papers (AQA publishes each summer's papers the following summer): run the bank pipeline, then `export.py --images`, commit `src/data` and `public/img`. Grade boundaries (`site.config.json` → `src/data/boundaries.json`) in August; exam dates (`src/data/exams.json`) when AQA publishes the final timetable.

## OCR section (/ocr/)
- Built the same way as the Eduqas section: `scripts/build.mjs` loops over `['eduqas', 'ocr']`. OCR files are in `boards/ocr/`: `data/` (47 papers, 1,885 parts, 45 topics), `topics.json`, `site.config.json`, `exams.json`, `boundaries.json`, `replace.json` (AQA → OCR wording, H556/H156, data booklet, PAG practicals, storage keys `malt-ocr-`) and `overrides/`.
- Overrides: `lib/groups.ts` (Modules 1–2, 3, 4, 5, 6), the header, `pag-practicals`, `data-booklet` and the decks are hand-written; the home page, topic index, question types, past papers, grade boundaries, spec checklist, search, practice, six-mark level of response, mock builder and maths skills are the AQA pages with edits, written by `python3 boards/ocr/gen_overrides.py` (re-run it after changing one of those AQA pages).
- Data: `python3 scripts/export.py --bank "<Dropbox>/Physics/OCR/Question Bank" --topics boards/ocr/topics.json --config boards/ocr/site.config.json --out boards/ocr/data`, then `python3 scripts/webp_all.py "<Dropbox>/Physics/OCR/Question Bank"`. `site.config.json` carries OCR-only settings read by `export.py`: `formatMap` (bank question types → the site's), `skillText` (full wording of maths skills the bank holds shortened), `erClean`, `asFromCode`/`asExclude` (AS = Modules 1 to 4 except 1.2).
- Paper shapes in the mock builder: A-level Papers 1 and 2 are 15 multiple choice + 85 structured (2 h 15), Paper 3 is 70 structured (1 h 30); AS Paper 1 is 20 multiple choice + 50, AS Paper 2 is 70. Totals 270 (A level) and 140 (AS), unweighted.
- The header's board switch (AQA | OCR | Eduqas) is in `src/components/Header.astro` and in each board's header override; the board home's canonical is set in `build.mjs`.

## Eduqas section (/eduqas/)
- `npm run build` runs `scripts/build.mjs`: the AQA build as before, then a copy of the repo in `.build/eduqas` with the Eduqas data, the string replacements in `boards/eduqas/replace.json` (AQA → Eduqas wording, Data Booklet, specified practicals, storage keys `malt-edq-`) and the whole-page overrides in `boards/eduqas/overrides/` (home, topic index, question types, Data Booklet, specified practicals, maths skills, QER, mock builder, past papers, grade boundaries, spec checklist, practice, search, header, `lib/groups.ts`, decks). That build is moved under `dist/eduqas/` with its internal links prefixed; the tutors, about, legal and form pages come from the AQA build only. One sitemap is written for the whole site.
- Data: `python3 scripts/export.py --bank "<Dropbox>/Physics/Eduqas/Question Bank" --topics boards/eduqas/topics.json --config boards/eduqas/site.config.json --out boards/eduqas/data`, then `python3 scripts/webp_all.py "<Dropbox>/Physics/Eduqas/Question Bank"` for the crops (public/img/<bundle>, lossless WebP for text crops). Exam dates and boundaries: `boards/eduqas/exams.json`, `boards/eduqas/boundaries.json` (copied from `site.config.json`).
- 31 topics: one per specification topic (1.1 to 3.10, options 3.A to 3.D) plus Component 1 comprehension. Mock shapes: C1 80 + 20 comprehension; C2 100; C3 100 + 20 option; AS 75 each. Boundaries out of 320 (100 + 100 + 120), AS out of 150.
- To change an Eduqas page, edit its override (or add a replacement); pages without an override are the AQA page with the replacements applied.
