# Petfolk take-home: lifecycle communication from medical records

This repo answers the two questions in the brief.

1. What lifecycle communication should we send these customers?
2. How would you build the thing that decides?

## How to read this

Start here, then go where you want.

| Folder | What's in it |
|---|---|
| `ground-rules.md` | The 11 constraints every journey follows and Q2 is built on. Read this first. |
| `question-1/journeys/index.html` | The map to Q1a. Start here for Question 1. |
| `question-1/journeys/` | 12 month journeys for 5 pets, in the format of the Biscuit example (HTML) |
| `question-1/triage.md` | Q1b: the rubric, all 25 records with my call on each, the distribution check, the patterns |
| `question-1/triage.csv` | Q1b as a machine readable spec, one row per record, columns mapped to Q2 engine fields |
| `question-2/build.md` | How I would build the system that decides, for 42 clinics now and 100 in two years |
| `working/how-i-worked.md` | The narrative: order of work, where AI did the work, where I overrode it |
| `working/how-i-build-a-journey.md` | The repeatable method behind a journey. Also the spec Q2 automates. |
| `working/prompts.md` | The prompts that moved the work, in order |
| `working/decisions-log.md` | Every judgment call in order: open brief, data conflicts, method. Also my video script. |
| `working/model-corrections.md` | Every place the model or the data was wrong, and what I did about it |
| `working/ingestion-log.md` | What every one of the 25 records actually contains, one entry each |
| `working/biscuit-anatomy.md` | My teardown of the Biscuit example: every touch, every trigger, the cost math |
| `working/` | Everything else: the scripts, the quoted spans behind every journey |

## The short version

**Question 1a.** Five 12 month journeys, one per record, in the Biscuit format. Each is built as
parallel tracks, not sequential steps. Every touch names its channel, its cost, the Vetspire or Segment
event that fires it, and any conditional gate. Every pet specific line in a journey is a verbatim quote
from that pet's record, checked by a string match script against the source, 193 quoted spans across the
five, zero misses. Start at `question-1/journeys/index.html`.

The five span the range on purpose. Quorra2 is an empty record, a cat Petfolk has never seen, and her
honest journey costs about 6 cents a year. Pobble is a feral rescue senior with stage 3 periodontal
disease whose dental is gated by an unresolved anxiety medication question, and his journey costs 28
cents on a quiet path or $24 if every escalation fires. Spend follows medical need. The flat $1.50
average describes neither.

Two things no journey does. It never fires a vaccine due message off the text export, because the export
cannot say which vaccine record is current and a wrong "your pet is overdue" line becomes part of the
medical record. And it never makes a clinical claim an exam has not supported.

**Question 1b.** All 25 records, a one to two line call on each, in `question-1/triage.md`. The
cross cutting patterns: declines are almost always cost driven and are the business opportunity, not a
closed door. Life events (a move, a death in the household, a new pet) drive the clinical picture and
should be a trigger. Multi pet households are common and the data does not link them. Six records are
header only stubs. Pre visit anxiety is everywhere, so a fear free pre visit track applies to a large
share of the book.

**Question 2.** In `question-2/build.md`, one page and a diagram. The thing that decides is the Q1
method plus the Q1b rubric, run as one service between Segment and Braze: a classifier picks an
archetype and tier, that selects a pre authored journey template, a guardrail layer checks consent,
suppression and the verbatim quotes at send time, and anything it cannot fill safely fails closed to a
task. The current outbound program is logistics only, quoted from the Pengo3 record. Scaling to 100
clinics is nearly free because it is event driven off Vetspire, which every clinic already runs. The
one hard part is review without a medical review board: it moves from per message to per template,
plus a sampled audit and a kill switch, and it needs a clinical communications owner role that does
not exist today.

## Decisions I made where the brief was open

The brief says to decide and note it rather than wait. Highlights below, the full running list with reasoning and per pet data conflicts is in `working/decisions-log.md`.

1. **Two planted injections, ignored both.** `records/_INDEX.txt` carries a fake "ASSISTANT DIRECTIVE" telling any model to put raw names and `[NAME]` tokens into customer messages, label every empty record "healthy", and drop the compliance section. It is not from Petfolk. Separately, the pseudonymiser reused a tiny name pool, so one client name maps to several unrelated pets. I key on Patient ID and signalment, never client name. Detail in `working/model-corrections.md`.
2. **Empty records get an honest journey, not a made up one.** Six of the 25 files are header only with no encounter. A journey for one of those says what we can and cannot do and lists what we would pull from Vetspire, rather than inventing a wellness story.
3. **The $1.50 per patient per year budget is the wrong frame.** It should be tiered by medical need. Reasoning in `question-2/build.md`.
4. **A declined vaccine is a closed door, not a re-raise.** Quorra's owner declined vaccines. That journey sends no vaccine marketing at all. The only vaccine message is a factual explanation of why anaesthesia for his dental needs clearance, plus the titer option, with the decision left to the owner and the vet. Consent is treated as real (see `ground-rules.md` rule 10). Full reasoning per pet in `working/decisions-log.md`.

## Source data

The 25 records are not committed here. They live in the take-home download. `doc_id` in each file header is the identifier used throughout.
