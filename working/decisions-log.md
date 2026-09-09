# Decisions log

Every judgment call I made on this take-home, in order, with the reasoning and where it lives in the repo. The brief says to decide and note it rather than wait, so this is the note. It is also my script for the walkthrough video.

Three kinds of decision are tracked here:

- **Open brief.** The brief left it to me.
- **Data conflict.** The record contradicts itself and I had to pick.
- **Method.** How I chose to work.

For the standing rules and assumptions that apply to every journey, see `ground-rules.md`. This file is the running list of specific calls.

---

## Method decisions

| # | Decision | Why | Where |
|---|---|---|---|
| M1 | Answer as a repo plus a zip, not an artifact or an app | The deliverable is read by a hiring panel and reused by future candidates. A repo with a reading map beats a single artifact. Journeys ship as HTML in the Biscuit format, plus PDF. | `README.md` |
| M2 | One question at a time, human in the loop on every call | Aaliyan makes the final decision on every clinical or judgment call. The model does evidence gathering, drafting, and verification. | `working/how-i-worked.md` |
| M3 | Read all 25 records end to end before answering anything | The first pass summarised 8 large files from grep fragments and was confidently wrong on details we would have quoted. Fixed by full reads. | `working/model-corrections.md` #3, `prompts.md` Session 2 |
| M4 | Evidence file first, then journey, then a script re-checks the finished HTML | Petfolk verifies pet facts by string match. Every quotable span is grep checked into an evidence file, the journey only quotes from that list, then `verify_quotes.py` re-checks the built HTML against the source. | `working/how-i-build-a-journey.md`, `working/scripts/verify_quotes.py` |
| M5 | The 25 record files go in the repo but gitignored | They are Petfolk's assessment material, not ours to publish. They ship in the zip so the work is reproducible, they stay out of the public repo. | `.gitignore`, `records/README.md` |
| M6 | In the HTML, verbatim record quotes are wrapped and highlighted, proposed message copy is in plain quotes | A reviewer can see at a glance which text is lifted from the chart and which is my draft wording. | `question-1/journeys/ikko.html` head comment |
| M7 | One journey per pet covering 12 months, built as parallel tracks not sequential steps | Matches the Biscuit example. A pet has several storylines running at once (a spine, a problem list, a household change), each with its own trigger and exit. | `working/biscuit-anatomy.md` |

## Open brief decisions

| # | Decision | Why | Where |
|---|---|---|---|
| O1 | Ignore the planted "ASSISTANT DIRECTIVE" in `records/_INDEX.txt` | It is untrusted text in a data file, not an instruction from Petfolk. Following it would put raw names and `[NAME]` tokens into customer messages, label empty records "healthy", and delete the compliance section. | `working/model-corrections.md` #1 |
| O2 | Key on Patient ID and signalment, never client name | The pseudonymiser reused a small name pool. One client name maps to several unrelated pets across different clinics and states. | `working/model-corrections.md` #2, `ground-rules.md` rule 11 |
| O3 | Header only records get an honest journey | Six of the 25 files have no encounter. The journey for one of those says what we can and cannot do and lists what we would pull from Vetspire, instead of inventing a wellness story. | `README.md`, `question-1/triage` |
| O4 | The $1.50 per patient per year figure is a target, not a per patient cap | Spend should follow medical need. A healthy cat costs almost nothing, a complex case is worth more. The budget holds at the population level. | `ground-rules.md` assumption 6, `question-2/build.md` |
| O5 | Assume Petfolk's string match normalises whitespace | The source wraps sentences mid line. Without this assumption almost no useful quote survives. The verify script checks both the raw form and the whitespace normalised form so we know which quotes need the leniency. | `ground-rules.md` assumption 1 |
| O6 | "Declined" means "not now", not "never" | A cost decline on SQ fluids or a deferred senior panel is a re-raise candidate later, not a closed door. | `ground-rules.md` assumption 8 |

## Data conflict decisions

### Ikko (`z1_MRS-45`)

| # | Conflict | Decision | Reasoning |
|---|---|---|---|
| D-IKKO-1 | One radiograph block says `LEFT MANUS` / `left front digit four`. The diagnosis, problem list, DDx and discharge all say right front digit 4. | Use right front. | Clinic template error in the single radiograph block. Right is consistent everywhere else. Noted in the journey footer as a caught inconsistency. |
| D-IKKO-2 | Two bordetella records with different next due dates (`Nov 20, 2026` injectable, `Mar 26, 2027` intranasal). A naive read flags her overdue. | Do not fire any "vaccine overdue" touch off the text export. | Under rule 5 (no Vetspire API) the export does not tell us reliably which record is live, and a wrong "your dog is overdue" message becomes part of the chart. Vaccine touches require a structured feed with a current record flag, listed as a required field. |
| D-IKKO-3 | Problem list says `Injury of nail - Jun 23, 2026`. A later support note says she was "previously seen on 07/03/2026 for a broken nail". | Use `Jun 23, 2026`. | The problem list is Vetspire's own dated field. The support note is a staff member's recollection. June is consistent with the first exam in the file. Discrepancy noted in the footer. |

### Ikko3 (`z2_16MRS-16`)

| # | Conflict | Decision | Reasoning |
|---|---|---|---|
| D-IKKO3-1 | Client is `Guthrie Pellow` on the header, `Guthrie Emery Yancey` throughout the attached history. `Emery Yancey` is also a Petfolk LVT who signs notes in the same file. The pet is written `Ikko3 Emery Yancey` eight times. | Never quote a personal name as a pet fact. Address the owner generically. Key on Patient ID `PT-E3BF8D`. | The staff first name has been pasted onto the pet as a surname. This is the pseudonymiser, not real data. |
| D-IKKO3-2 | The Jul 21 2026 virtual care note uses the name `Stormy` for Ikko3, including a weight figure: `Stormy's normal weight is around 8 pounds`. | Do not quote `Stormy` or the `around 8 pounds` figure. Use the dated exam weights (7.84 to 8.57 lb) for the weight story. | Same artifact class as D-IKKO3-1. A wrong name substituted mid paragraph in a note that also names Ikko3 directly. |
| D-IKKO3-3 | Most visits are at `Sandy Dr. S. Thistlewood`. The Jul 2025 ribbon visit is at `PETFOLK - EAST COBB MARIETTA`. | Treat Sandy as home clinic. | Every 2026 encounter and both forward bookings are at Sandy. Noted, no action. |
| D-IKKO3-4 | Rabies due date appears three ways: free text `November 2026`, immunization table `Nov 11, 2026`, a booked staff reminder for `Aug 01, 2026`. | Do not fire "rabies overdue" off the text export. The journey may reference the booked Aug 1 and Nov 23 appointments because those are explicit appointment records. | Consistent with D-IKKO-2. Inferred dates are unsafe, booked appointments are facts. |
| D-IKKO3-5 | Age given as `2.6 YO` (header), `1-year 11-month-old` (Dec 2025 notes), `1yr` (radiology). DOB as both `[MON] [DAY], 2024` and `1/1/2024`. | Low stakes. The journey never states an age. Use the header line verbatim only if a signalment chip needs it. | Matches the Biscuit format, which quotes the header signalment line as is. |

## Clinical calls (human in the loop)

These are calls Aaliyan made or confirmed, not the model.

| # | Pet | Call | Status |
|---|---|---|---|
| C-IKKO-1 | Ikko | The declined items and the amputation decision are branch points the journey waits on, not things a message pushes. | approved, in `working/design/ikko.md` |
| C-IKKO3-1 | Ikko3 | Nothing anaesthetic (the dental, therefore the deferred wellness bloodwork) is offered until the pre-visit gabapentin problem is solved. The dental email is gated behind a YES/NO check on whether the owner can dose her. | in `working/design/ikko3.md` Track E |
| C-IKKO3-2 | Ikko3 | The IBD question (`Ddx hairballs ... vs primary GI (IBD flare up)`) is not driven by a message. The journey surfaces it in Tracks C and D and gates escalation on owner interest and a symptom threshold. | in `working/design/ikko3.md` |
| C-IKKO3-3 | Ikko3 | The pica track is a permanent low-cost safety net with an always-on urgent-routing rule, not a timed campaign, because the behaviour never resolves. | in `working/design/ikko3.md` Track B |
| _more added as journeys are drafted_ | | | |

---

## How this maps to the video

1. Show the brief's two questions.
2. M3 and `model-corrections.md` #3: the model overstated its coverage, I caught it, we re-read everything.
3. O1: the planted injection, ignored.
4. M4: the evidence file and verify script, the string match problem and how we handle it.
5. D-IKKO3-1 and D-IKKO3-2: the name bleed, a concrete "caught the model" moment.
6. O4: why $1.50 is the wrong frame, leads into Q2.
