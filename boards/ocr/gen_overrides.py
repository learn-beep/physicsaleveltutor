import json, pathlib, sys
# Writes the OCR page overrides that are edits of the AQA pages (boards/ocr/overrides/src/pages/...), so a change to an
# AQA page can be carried over: python3 boards/ocr/gen_overrides.py. It stops if a piece of AQA wording it expects has gone.
# Hand-written overrides (lib/groups.ts, Header, pag-practicals, data-booklet, decks) are not touched.
R = pathlib.Path(__file__).resolve().parents[2]; O = R/'boards/ocr/overrides/src'
BLANKET = [('7408', 'H556'), ('7407', 'H156'), ("AQA's", "OCR's"), ('AQA', 'OCR'), ('/formula-sheet/', '/data-booklet/'), ('/required-practicals/', '/pag-practicals/'), ("'malt-", "'malt-ocr-"), ('data and formulae booklet', 'Data, Formulae and Relationships Booklet')]
def gen(rel, reps):
    s = (R/'src'/rel).read_text()
    for a, b in reps:
        if a not in s: sys.exit(f'{rel}: missing {a[:70]!r}')
        s = s.replace(a, b)
    for a, b in BLANKET: s = s.replace(a, b)
    p = O/rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s); print('wrote', rel)

# ---- home
gen('pages/index.astro', [
 ('<p class="muted">AQA A-level 7408 and AS 7407 Physics. Sections 3.1 to 3.5 are the AS content; 3.6 to 3.8 and the Paper 3 options (Astrophysics, Medical, Engineering, Turning points, Electronics) are A-level only. The June 2026 papers will be added when AQA makes them public.</p>',
  '<p class="muted">OCR A-level Physics A (H556) and AS (H156). Modules 1 to 4 are the AS content; Module 5 (Newtonian world and astrophysics) and Module 6 (Particles and medical physics) are A-level only. There are no options. The June 2026 papers will be added when OCR makes them public.</p>'),
 ('<p class="board-note">Studying another board? <a href="/ocr/"><strong>OCR Physics A</strong> (H556 / H156)</a> and <a href="/eduqas/"><strong>Eduqas (WJEC)</strong> (A420QS / B420QS)</a> each have their own section: every paper since 2016 by topic, with mark schemes and examiners\' comments.</p>',
  '<p class="board-note">This is the <strong>OCR Physics A</strong> section. Studying another board? <a href="/">Go to the {"AQ" + "A"} section</a> or <a href="/eduqas/">the Eduqas section</a>.</p>'),
 ('<Base title="AQA A-level Physics: past-paper questions by topic, mark schemes and tutors"', '<Base title="OCR A-level Physics A: past-paper questions by topic, mark schemes and tutors" description="Free OCR A-level and AS Physics A (H556, H156) past-paper questions by topic, mark schemes, examiners\' comments, practice and the data booklet, with a specialist physics tutor."'),
 ('<h1>AQA A-level Physics, one topic at a time</h1>', '<h1>OCR A-level Physics A, one topic at a time</h1>'),
 ('>Formula sheet</a>\n    <a href="/maths-skills/">', '>Data booklet</a>\n    <a href="/maths-skills/">'),
 ('placeholder="e.g. momentum, capacitors, photoelectric, SHM"', 'placeholder="e.g. momentum, capacitors, stars, medical imaging"'),
 ('All {allTopics.length} topics, including the five options', 'All {allTopics.length} topics, Module 1 to Module 6'),
 ('<strong>Formula sheet</strong><span>What the AQA data and formulae booklet gives you, section by section, and what you have to learn</span>', '<strong>Data booklet</strong><span>What the OCR Data, Formulae and Relationships Booklet gives you, module by module, and what you have to learn</span>'),
 ('<strong>Required practicals</strong><span>All twelve, what the papers ask about each, and every question on them</span>', '<strong>PAG practicals</strong><span>The practical activity groups, what the papers ask about each, and every question on them</span>'),
 ('<strong>Six-mark questions</strong><span>Every extended response question, by topic, with a timed practice tool</span>', '<strong>Level of response</strong><span>Every six-mark level of response question, by topic, with a timed practice tool</span>'),
 ('<span>The definitions AQA asks for, topic by topic, with spaced repetition</span>', '<span>Definitions topic by topic, with spaced repetition</span>'),
 ('Paper 1, 2, 3 or AS', 'Paper 1, 2, 3 or the AS papers'),
 ('Marks by topic since 2016, the latest papers', 'Marks by topic since 2017, the latest papers'),
 ('who currently teaches AQA physics at a top sixth-form college', 'who currently teaches A-level physics at a top sixth-form college'),
])

# ---- questions index
gen('pages/questions/index.astro', [
 ('from measurements to the Paper 3 options', 'from practical skills to medical imaging'),
 ("Paper 3 Section A (practical skills and data analysis) questions appear under whichever topic they are about; the five options of Paper 3 Section B have their own topics at the end.", "A part that tests two topics appears under both. Module 1 (practical skills) is examined in every paper, so its questions are also filed under the topic the experiment is about."),
 ('six-mark extended responses', 'six-mark level of response questions'),
])

# ---- question types
gen('pages/questions/type/[type].astro', [
 ("'Every multiple-choice question: Section B of A-level Papers 1 and 2 (25 each) and Section B of AS Paper 2 (30), with the answer behind the button. Allow about 1 minute 12 seconds each.'", "'Every multiple-choice question: Section A of A-level Papers 1 and 2 (15 each) and Section A of AS Paper 1 (20), with the answer behind the button. Allow about a minute and a quarter each.'"),
 ("AQA gives method marks, and an error carried forward from an earlier part still scores.", "OCR gives method marks (C marks) even when the final answer (the A mark) is wrong, and an error carried forward from an earlier part still scores."),
 ("'Six-mark extended response questions', 'The six-mark questions marked by level. Level 3 needs the full set of physics points and a clear, logical line of reasoning.'", "'Six-mark level of response questions', 'The six-mark questions marked with an asterisk on the paper and marked by level. Level 3 needs the full set of physics points and a well-developed, logical line of reasoning.'"),
 ("'Questions on the twelve required practicals, planning, measurements, uncertainties, graphs and evaluation, most of them from Paper 3 Section A.'", "'Questions on the practical activity groups (PAGs), planning, measurements, uncertainties, graphs and evaluation. Practical skills are examined in every paper.'"),
])

# ---- past papers
gen('pages/past-papers/index.astro', [
 ("const cell = (series, spec, code) => allPapers.find((p) => p.series === series && p.spec === spec && String(p.paperNo).replace(/^0/, '') === code);\nconst OPTS = [['3BA', 'Astro'], ['3BB', 'Medical'], ['3BC', 'Engineering'], ['3BD', 'Turning points'], ['3BE', 'Electronics']];", "const cell = (series, spec, code) => allPapers.find((p) => p.series === series && p.spec === spec && String(p.paperNo).replace(/^0/, '') === code);"),
 ('<Base title="AQA A-level Physics past papers (7408 and AS 7407) 2016–2025 with question-by-question tables"', '<Base title="OCR A-level Physics A past papers (H556 and AS H156) 2016–2025 with question-by-question tables" description="Every OCR A-level and AS Physics A paper since 2016 with a question-by-question table of topics, marks and question types, mark schemes and examiners\' comments."'),
 ('<h1>AQA A-level Physics past papers</h1>', '<h1>OCR A-level Physics A past papers</h1>'),
 (">AQA's assessment resources</a>", ">OCR's past papers and mark schemes</a>"),
 ("<thead><tr><th>Series</th><th>Paper 1</th><th>Paper 2</th><th>Paper 3A</th><th>Paper 3B (option)</th></tr></thead>", "<thead><tr><th>Series</th><th>Paper 1 Modelling physics</th><th>Paper 2 Exploring physics</th><th>Paper 3 Unified physics</th></tr></thead>"),
 ("{['1', '2', '3A'].map((n) => { const p = cell(s, '7408', n); return <td>{p ? <a href={`/past-papers/${p.slug}/`}>{n === '3A' ? 'Section A' : p.paper}</a> : '—'}</td>; })}<td>{OPTS.map(([c, name], i) => { const p = cell(s, '7408', c); return p ? <>{i ? ' · ' : ''}<a href={`/past-papers/${p.slug}/`}>{name}</a></> : null; })}</td></tr>", "{['1', '2', '3'].map((n) => { const p = cell(s, '7408', n); return <td>{p ? <a href={`/past-papers/${p.slug}/`}>{p.paper}</a> : '—'}</td>; })}</tr>"),
 ("<thead><tr><th>Series</th><th>Paper 1</th><th>Paper 2</th></tr></thead>", "<thead><tr><th>Series</th><th>Paper 1 Breadth in physics</th><th>Paper 2 Depth in physics</th></tr></thead>"),
 ("the November 2020 and November 2021 papers are the autumn series AQA ran instead, using the papers written for June 2020 and June 2021. The A-level papers start in June 2017 and the AS papers in June 2016; the specimen papers are listed at the bottom of the A-level table. Paper 3 is one exam: Section A (practical skills and data analysis) and Section B, the option you studied.", "the November 2020 and November 2021 papers are the autumn series OCR ran instead. The A-level papers start in June 2017 and the AS papers in June 2016. Paper 1 covers Modules 1, 2, 3 and 5; Paper 2 covers Modules 1, 2, 4 and 6; Paper 3 covers all six. OCR removed one multiple-choice question (Q10) from the June 2025 AS Paper 1, so that paper is shown without it."),
])

# ---- grade boundaries
gen('pages/grade-boundaries/index.astro', [
 ('with a calculator that turns your three paper marks into a total out of 250', 'with a calculator that turns your three paper marks into a total out of 270'),
 ("<p>Papers 1 and 2 are marked out of 85 and Paper 3 out of 80 (45 for Section A and 35 for your option). AQA adds the three raw marks, so the overall boundaries are out of 250 (Papers 1 and 2 are 34% of the A level each and Paper 3 is 32%). AQA sets a slightly different boundary for each Paper 3 option; the figures below are the indicative subject boundaries, so treat them as a guide to within a few marks. Boundaries move every year with the difficulty of the papers, so use the last few series as a range, not a target.</p>",
  "<p>Papers 1 and 2 are marked out of 100 and Paper 3 out of 70. OCR adds the three raw marks with no scaling, so the overall boundaries are out of 270 (Papers 1 and 2 are 37% of the A level each and Paper 3 is 26%). The AS is two papers of 70 marks, so its boundaries are out of 140. Boundaries move every year with the difficulty of the papers, so use the last few series as a range, not a target.</p>"),
 ('Paper 1 mark (out of 85) <input type="number" min="0" max="85"', 'Paper 1 mark (out of 100) <input type="number" min="0" max="100"'),
 ('Paper 2 mark (out of 85) <input type="number" min="0" max="85"', 'Paper 2 mark (out of 100) <input type="number" min="0" max="100"'),
 ('Paper 3 mark (out of 80) <input type="number" min="0" max="80"', 'Paper 3 mark (out of 70) <input type="number" min="0" max="70"'),
 ('out of 250</h2>', 'out of 270</h2>'),
 ('${total}/250: grade A*', '${total}/270: grade A*'),
 ('${total}/250: grade ${grade}', '${total}/270: grade ${grade}'),
])

# ---- specification
gen('pages/specification/index.astro', [
 ("import { GROUPS } from '../../lib/groups';\nconst papers = GROUPS.map((g) => [Number(g.sec.split('.')[1]), g.heading]);", "const papers = [[1, 'Module 1: Development of practical skills in physics'], [2, 'Module 2: Foundations of physics'], [3, 'Module 3: Forces and motion'], [4, 'Module 4: Electrons, waves and photons'], [5, 'Module 5: Newtonian world and astrophysics (A level only)'], [6, 'Module 6: Particles and medical physics (A level only)']];"),
 ("description={`All ${total} content statements of the AQA A-level Physics specification (7408) as a tickable checklist, from measurements to the five options, with the AS content (sections 3.1 to 3.5) marked and links to the past-paper questions for each topic.`}", "description={`All ${total} learning outcomes of the OCR A-level Physics A specification (H556) as a tickable checklist, Module 1 to Module 6, with the AS content marked and links to the past-paper questions for each topic.`}"),
 ("all ${total} statements, tickable", "all ${total} learning outcomes, tickable"),
 ("<p>Every content statement in the AQA Physics specification (7408, version 1.4), under AQA's section numbers; we number the statements within each subsection (3.6.1.1-04 is the fourth statement of 3.6.1.1). Tick what you're confident with; ticks are saved in this browser only. Sections 3.1 to 3.5 are the whole of the AS (7407). Paper 1 covers 3.1 to 3.5 and 3.6.1 (periodic motion); Paper 2 covers 3.6.2 to 3.8; Paper 3 Section A is practical skills and data analysis, and Section B is the one option you study (3.9 to 3.13).</p>",
  "<p>Every learning outcome in the OCR Physics A specification (H556, version 3.0, March 2026), under OCR's own numbers (3.2.1(a) is outcome (a) of section 3.2.1). Tick what you're confident with; ticks are saved in this browser only. Outcomes marked AS are also in the AS (H156): that is Modules 1 to 4, apart from the practical endorsement (1.2). Paper 1 covers Modules 1, 2, 3 and 5; Paper 2 covers Modules 1, 2, 4 and 6; Paper 3 covers all six.</p>"),
 ("{st.text}{st.guidance && ", "{st.text}{st.as && <> <span class=\"asb\">AS</span></>}{st.guidance && "),
])

# ---- search
gen('pages/data/search.json.ts', [
 ('{"t": "Six-mark extended response questions", "u": "/six-mark-questions/", "kind": "Tool"}, {"t": "Formula sheet (data and formulae booklet)", "u": "/formula-sheet/", "kind": "Tool"}', '{"t": "Six-mark level of response questions", "u": "/six-mark-questions/", "kind": "Tool"}, {"t": "Data booklet: what is given", "u": "/formula-sheet/", "kind": "Tool"}'),
 ('{"t": "Required practicals", "u": "/required-practicals/", "kind": "Tool"}', '{"t": "PAG practicals", "u": "/required-practicals/", "kind": "Tool"}'),
 ('{"t": "Practical questions", "u": "/questions/type/practical-questions/", "kind": "Tool"}]', '{"t": "Practical questions", "u": "/questions/type/practical-questions/", "kind": "Tool"}, {"t": "AQ" + "A section", "u": "/", "kind": "Tool"}, {"t": "Eduqas section", "u": "/eduqas/", "kind": "Tool"}]'),
])

# ---- practice
gen('pages/practice/index.astro', [
 ("const groups = GROUPS.map((g) => [g.sec + ' ' + g.key.replace('Option: ', ''), g.key]);", "const groups = GROUPS.map((g) => [g.key, g.key]);"),
 ("{GROUPS.slice(0, 8).map((g) => <button class=\"chip\" type=\"button\" data-all={g.key}>All {g.sec}</button>)}", "{GROUPS.map((g) => <button class=\"chip\" type=\"button\" data-all={g.key}>All {g.key}</button>)}"),
 ("{t.name.split(':').pop().trim()}", "{t.name.split(':')[0].trim()}"),
 ('Six-mark extended response</button>', 'Six-mark level of response</button>'),
])

# ---- six-mark level of response
gen('pages/six-mark-questions/index.astro', [
 ('<Base title="Every AQA A-level Physics six-mark extended response question, by topic, with a timed tool" description="All the six-mark extended response questions set on AQA Physics since 2016', '<Base title="Every OCR A-level Physics A six-mark level of response question, by topic, with a timed tool" description="All the six-mark level of response (LoR) questions set on OCR Physics A since 2016'),
 ('<h1>Six-mark extended response questions</h1>', '<h1>Six-mark level of response questions</h1>'),
 ("Each Paper 3B option paper has one; AS Paper 1 usually has one; A-level Papers 1 and 2 set them less often.", "They are the questions marked with an asterisk (*) on the paper. Every A-level paper (1, 2 and 3) has two, and so does AS Paper 2; AS Paper 1 has none."),
 ("<td>All the parts of the question are covered with correct physics, in a coherent and logical answer with linked reasoning.</td>", "<td>Clear and correct physics on every part of the question, with a well-developed line of reasoning that is clear and logically structured; the information is relevant and substantiated.</td>"),
 ("<td>Most parts are covered with some correct physics, but one part is missing or weak, or the reasoning is only partly linked.</td>", "<td>Some correct physics on most of the question, with a line of reasoning that has some structure; the information is mostly relevant and supported by some evidence.</td>"),
 ("<td>Some relevant physics on one part, with little structure.</td>", "<td>A few relevant points; the information is basic and communicated in an unstructured way.</td>"),
 ("then the higher or lower mark in that level. Most questions", "then the higher or lower mark in that level from the quality of the communication. Most questions"),
])

# ---- mock builder
gen('pages/mock/index.astro', [
 ('in the shape of Paper 1, 2 or 3 with your option (or the AS papers)', 'in the shape of Paper 1, 2 or 3 (or the AS papers)'),
 ("A-level Papers 1 and 2 are 60 marks of structured questions (Section A) and 25 multiple-choice questions (Section B), in 2 hours. Paper 3 is 45 marks of practical skills and data analysis (Section A) and 35 marks on your option (Section B), in 2 hours. AS Paper 1 is 70 marks of structured questions; AS Paper 2 is 40 marks of structured questions and 30 multiple-choice questions, each in 1 hour 30 minutes.", "A-level Papers 1 and 2 are 15 multiple-choice questions (Section A) and 85 marks of structured questions (Section B), in 2 hours 15 minutes. Paper 3 is 70 marks of structured questions on all six modules, in 1 hour 30 minutes. AS Paper 1 is 20 multiple-choice questions and 50 marks of structured questions; AS Paper 2 is 70 marks of structured questions, each in 1 hour 30 minutes."),
 ('>Paper 1 (3.1 to 3.6.1)</button>', '>Paper 1 (Modules 1, 2, 3 and 5)</button>'),
 ('>Paper 2 (3.6.2 to 3.8)</button>', '>Paper 2 (Modules 1, 2, 4 and 6)</button>'),
 ('>Paper 3 (practical and option)</button>', '>Paper 3 (all modules)</button>'),
 ('    <h3>Option (Paper 3 only)</h3>\n    <div class="chips" data-group="opt"><button class="chip" type="button" data-v="Astrophysics" aria-pressed="true">Astrophysics</button><button class="chip" type="button" data-v="Medical physics">Medical physics</button><button class="chip" type="button" data-v="Engineering physics">Engineering physics</button><button class="chip" type="button" data-v="Turning points">Turning points</button><button class="chip" type="button" data-v="Electronics">Electronics</button></div>\n', ''),
 ("const SHAPE = { 'A level': { 'Paper 1': [25, 60, 85], 'Paper 2': [25, 60, 85], 'Paper 3': [0, 80, 90] }, AS: { 'Paper 1': [0, 70, 77], 'Paper 2': [30, 40, 77] } };", "const SHAPE = { 'A level': { 'Paper 1': [15, 85, 81], 'Paper 2': [15, 85, 81], 'Paper 3': [0, 70, 77] }, AS: { 'Paper 1': [20, 50, 77], 'Paper 2': [0, 70, 77] } };"),
 ("      const p3 = sel.level === 'A level' && sel.paper === 'Paper 3';\n      const t = {", "      const p3 = false;\n      const t = {"),
 ("`${st} marks of structured questions${mc ? ` and ${mc} multiple-choice questions` : ''} (${mc + st} marks,", "`${mc ? `${mc} multiple-choice questions and ` : ''}${st} marks of structured questions (${mc + st} marks,"),
 ("${sel.level === 'AS' ? '1 hour 30 minutes' : '2 hours'}).` };", "${sel.level === 'AS' || sel.paper === 'Paper 3' ? '1 hour 30 minutes' : '2 hours 15 minutes'}).` };"),
 ("      const p3 = sel.level === 'A level' && sel.paper === 'Paper 3';\n      const ok =", "      const p3 = false;\n      const ok ="),
 ("else { fill(groups, st).forEach(add); picked = picked.concat(mcqs.slice(0, mc)); }", "else { picked = mcqs.slice(0, mc); fill(groups, st).forEach(add); }"),
])

# ---- maths skills
gen('pages/maths-skills/index.astro', [
 ("s.code.startsWith('MS '))", "s.code.startsWith('M '))"),
 ("'MS 2.5': 'Logarithms for quantities over many orders of magnitude: decibels, absolute magnitude (astrophysics option), log–log graphs.',", "'MS 2.5': 'Logarithms for quantities over many orders of magnitude: log scales on graphs, log–log and ln plots.',\n  'MS 1.3': 'Simple probability: the random nature of radioactive decay, the decay constant as a probability per unit time.',\n  'MS 2.1': 'The symbols =, <, <<, >>, >, ∝, ≈ and Δ, read and used correctly in working.',\n  'MS 3.9': 'Rates of change handled step by step or graphically, without calculus: iterative models of decay or discharge in a table or spreadsheet.',\n  'MS 3.10': 'Reading a logarithmic plot: values from a log scale, and what a straight line on it means.',\n  'MS 3.12': 'Sketching the shape of a relationship: y = kx, k/x, kx², k/x², sin, cos and exponentials, for example g against r or the charge on a discharging capacitor against time.',"),
 ("'MS 0.4': 'Estimates: the order of a quantity from everyday values, such as the mass of a car or the energy of a sneeze.',", "'MS 0.4': 'Estimates: the order of a quantity from everyday values, such as the mass of a car or the power of a kettle.',"),
 ("'MS 1.1': 'Significant figures: give the answer to the same number as the least precise data, usually 2 or 3. \"Show that\" answers need one more figure than shown.',", "'MS 1.1': 'Significant figures: give the answer to the same number as the least precise data, usually 2 or 3. \"Show that\" answers need more figures than the value shown.',"),
 ("'MS 4.1': 'Angles in 2D and 3D shapes: crystal structures, prisms and optical fibres.',", "'MS 4.1': 'Angles in 2D and 3D shapes: prisms, refraction and total internal reflection.',"),
 ("MS 0.1 to MS 4.7", "M0.1 to M4.7"),
 ("'MS ", "'M "),
 (">The A-level Physics formula sheet</a>", ">What the data booklet gives you</a>"),
 ("AQA's mark schemes give marks for each step and allow an error carried forward", "OCR's mark schemes give method marks (C marks) for each step and allow an error carried forward"),
 ("<a href={`#${c.replace(' ', '').replace('.', '-')}`}>{c}</a>", "<a href={`#${c.replace(' ', '').replace('.', '-')}`}>{c.replace(' ', '')}</a>"),
 ("<h2>{c}: {codes[c].text}</h2>", "<h2>{c.replace(' ', '')}: {codes[c].text}</h2>"),
])
