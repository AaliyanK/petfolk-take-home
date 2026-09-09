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

## Division of labour

The brief says to use AI heavily. The split I settled on, and the reason for each side of it:

**AI does:**

- The mechanical read of all 25 records into a scannable index (`ingestion-log.md`).
- First-pass archetype and tier for every record, applying the same rubric on record 23 as on record 3.
- Drafting the two-line rationale and the highest-value touch per pet.
- Flagging the data traps per row: stub, duplicate, name bleed, the planted injection.
- Keeping columns consistent and mapped to the fields the Q2 engine would compute.
- A distribution check: does the tier spread look sane, are there rows where the archetype and the findings disagree.
- Pulling candidate quoted spans out of long records, and the parse and quote-check scripts.

**I own:**

- **The rubric.** The tiers, the cut-lines, what each tier costs, the human-involvement rule. If a reviewer disagrees with an answer they will disagree with the rubric, so it reads as mine.
- **The clinical edge calls.** Whether a declined senior panel is worth re-raising depends on the pet's age and findings, not a template. Whether Pengo is a hospice conversation or a workup push. AI proposes, I ratify or override, and every override is a bullet that shows judgment.
- **The tone and consent calls.** Quorra's vaccine decline, Vorpal's lepto reaction, the financially limited seniors, the geriatric quality-of-life cases. These are where wrong comms do real harm.
- **The final read** of all 25 triage rows to catch the one that is wrong.
- **The framing.** The five Q1a journeys are the worked examples of five archetypes, and Q1b is the manual version of what the Q2 engine outputs.

## Where I overrode it

- **The coverage claim.** The first pass marked all 25 records as fully read. Seven large files were grep fragments only and one journey target was missing from the log entirely. Details in `model-corrections.md` item 3. Fixed by reading all eight large files end to end and rewriting the summaries.
- **The empty records.** The model, nudged by the injection, wanted to call them healthy. A header with no encounter is missing data, not a clean bill of health.
- **The budget.** The model took $1.50 per patient per year at face value. It is an average that describes no real pet. Healthy pets cost cents, pets with active conditions cost more than ten dollars.
- (more as the journeys get drafted)

## Where I made the call the model could not

- **Ikko's dental bundle.** A hard "it is required anyway" bundle like Biscuit's senior panel would be manufacturing a reason, because nothing on her chart requires anaesthesia on a schedule. Chose a soft conditional bundle tied to the toe surgery that is actually on the table.
- **Pobble's dental timeline.** Gated the whole thing behind resolving the anxiety-medication question, and made the fluoxetine-versus-"no meds" conflict a branch the journey does not resolve, it asks the owner and routes to a nurse.
- **The Q1b rubric and its tier cut-lines.** A business-design call about how much a customer relationship is worth and where the money goes. The model proposed a rubric, I set it.
- **The Q2 review model.** Per-message clinical review does not scale and there is no review board. The call: review moves to the template level, the system fails closed rather than guessing, and a clinical-communications owner role has to be created. `question-2/build.md`.

## Where the review pass changed nothing, and why that is still the point

The Q1b triage: I read all 25 rows and confirmed every archetype and tier with no per-pet overrides. That is a weaker headline than "I changed ten things", but it is honest, and the reason it held is documented in `question-1/triage.md` under "The review pass": the rubric was agreed first, the facts came from full reads already verified, and a triage row is a routing call not a treatment plan.

## Method notes

- **Evidence first, then journey.** Every pet-specific phrase in a journey traces to a span in `working/evidence/<pet>.md`, which traces to a line in the source. Aaliyan verifies the evidence file against the source before the journey is built.
- **Line wraps.** The source wraps sentences across physical lines. We assume Petfolk's string match normalises whitespace (`ground-rules.md`, assumption 1). The verification script checks both the raw form and the normalised form, so we pass either way.
