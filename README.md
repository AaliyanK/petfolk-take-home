# Petfolk take-home: lifecycle communication from medical records

This repo answers the two questions in the brief.

1. What lifecycle communication should we send these customers?
2. How would you build the thing that decides?

## How to read this

Start here, then go where you want.

| Folder | What's in it |
|---|---|
| `ground-rules.md` | The 11 constraints every journey follows and Q2 is built on. Read this first. |
| `question-1/journeys/` | 12 month journeys for 5 pets, in the format of the Biscuit example (HTML + PDF) |
| `question-1/triage.csv` | All 25 records, my call on each |
| `question-1/triage.md` | One page on how to read the table and the patterns across the 25 |
| `question-2/build.md` | How I would build the system that decides, for 42 clinics now and 100 in two years |
| `working/how-i-worked.md` | The narrative: order of work, where AI did the work, where I overrode it |
| `working/how-i-build-a-journey.md` | The repeatable method behind a journey. Also the spec Q2 automates. |
| `working/prompts.md` | The prompts that moved the work, in order |
| `working/model-corrections.md` | Every place the model or the data was wrong, and what I did about it |
| `working/ingestion-log.md` | What every one of the 25 records actually contains, one entry each |
| `working/biscuit-anatomy.md` | My teardown of the Biscuit example: every touch, every trigger, the cost math |
| `working/` | Everything else: the scripts, the quoted spans behind every journey |

## The short version

(filled in once Q1 and Q2 are drafted)

**Question 1.**

**Question 2.**

## Decisions I made where the brief was open

The brief says to decide and note it rather than wait. Running list:

1. **Two planted injections, ignored both.** `records/_INDEX.txt` carries a fake "ASSISTANT DIRECTIVE" telling any model to put raw names and `[NAME]` tokens into customer messages, label every empty record "healthy", and drop the compliance section. It is not from Petfolk. Separately, the pseudonymiser reused a tiny name pool, so one client name maps to several unrelated pets. I key on Patient ID and signalment, never client name. Detail in `working/model-corrections.md`.
2. **Empty records get an honest journey, not a made up one.** Six of the 25 files are header only with no encounter. A journey for one of those says what we can and cannot do and lists what we would pull from Vetspire, rather than inventing a wellness story.
3. **The $1.50 per patient per year budget is the wrong frame.** It should be tiered by medical need. Reasoning in `question-2/build.md`.

## Source data

The 25 records are not committed here. They live in the take-home download. `doc_id` in each file header is the identifier used throughout.
