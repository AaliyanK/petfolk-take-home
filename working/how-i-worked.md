# How I worked

The narrative of the work. For the repeatable method behind a single journey, see `how-i-build-a-journey.md`. For the specific catches, see `model-corrections.md`. For the prompt log, see `prompts.md`.

## Order of work

1. Read the brief, the DOCX and the PDF. Confirmed they carry the same content.
2. Tore the Biscuit example apart touch by touch, so "in the format of the Biscuit example" had a precise meaning. See `biscuit-anatomy.md`.
3. Read all 25 records and `_INDEX.txt`. Caught the planted directive in `_INDEX.txt` on the first read of that file.
4. Built `ingestion-log.md`, one entry per record.
5. Scoped Q1 before writing anything. Which five, what each one has to prove, which threads become tracks.
6. Wrote `ground-rules.md`, the 11 constraints every journey follows.
7. Per journey: an evidence file of grep-checked quoted spans, then a design in markdown, then the HTML, then a script that re-checks every quote against the source.

## Where AI did the work

- First pass reading and summarising 25 records into a scannable index.
- Pulling candidate quoted spans out of long records.
- First drafts of each journey and the build memo.
- The parse and quote-check scripts.

## Where I overrode it

- **The coverage claim.** The first pass marked all 25 records as fully read. Seven large files were grep fragments only and one journey target was missing from the log entirely. Details in `model-corrections.md` item 3. Fixed by reading all eight large files end to end and rewriting the summaries.
- **The empty records.** The model, nudged by the injection, wanted to call them healthy. A header with no encounter is missing data, not a clean bill of health.
- **The budget.** The model took $1.50 per patient per year at face value. It is an average that describes no real pet. Healthy pets cost cents, pets with active conditions cost more than ten dollars.
- (more as the journeys get drafted)

## Where I made the call the model could not

- **Ikko's dental bundle.** A hard "it is required anyway" bundle like Biscuit's senior panel would be manufacturing a reason, because nothing on her chart requires anaesthesia on a schedule. Chose a soft conditional bundle tied to the toe surgery that is actually on the table.
- (more as the journeys get drafted)

## Method notes

- **Evidence first, then journey.** Every pet-specific phrase in a journey traces to a span in `working/evidence/<pet>.md`, which traces to a line in the source. Aaliyan verifies the evidence file against the source before the journey is built.
- **Line wraps.** The source wraps sentences across physical lines. We assume Petfolk's string match normalises whitespace (`ground-rules.md`, assumption 1). The verification script checks both the raw form and the normalised form, so we pass either way.
