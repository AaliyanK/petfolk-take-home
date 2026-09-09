# How I worked

(draft, filled in as the work happens)

## The workflow

25 medical records, one page to 120 pages each, converted from PDF so the text is messy.
The job was to turn that into journeys and a build plan without trusting the model to read
for me.

Rough order:

1. Read the brief and the Biscuit example. Tore the example apart touch by touch so I knew
   exactly what "in the format of the Biscuit example" means. See `biscuit-anatomy.md`.
2. Read every record. Small and medium ones in full. The eight big ones I read in full for
   the clinical sections and skimmed the appointment reminder boilerplate. Everything went
   into `ingestion-log.md`, one line per record.
3. Caught the planted directive in `_INDEX.txt` on the first read of that file. Logged it.
4. Scoped Q1 before writing anything. Which five records, what each one has to prove,
   what template to reuse.
5. Built each journey off an evidence file of quoted spans, then ran a script that checks
   every quote against the source.

## Where AI did the work

- First pass reading and summarising 25 records into a scannable index
- Pulling candidate quoted spans out of long records
- First drafts of each journey and the build memo
- The parse and quote check scripts

## Where I overrode it

(running list, add as it happens)

- The empty records. The model, nudged by the injection, wanted to call them healthy. A
  header with no encounter is missing data, not a clean bill of health.
- The budget. The model took $1.50 per pet per year at face value. It is an average that
  describes no real pet. Healthy pets cost cents, sick pets cost more than ten dollars.
- (more to come as we draft the journeys)

## Where I made the call the model could not

- (running list)

## Method notes

- **The source files wrap sentences across physical lines.** A phrase only survives a string match if it has no line break inside it. So the evidence files record the usable span, meaning the part that sits on a single line, and journeys never stitch two lines into one quote. The verification script checks against the raw text with newlines intact, which is the strict case. If Petfolk normalises whitespace before matching, we still pass. If they do not, we still pass.
- Evidence first, then journey. Every pet-specific phrase in a journey traces to a line in `working/evidence/<pet>.md`, which traces to a line in the source. Aaliyan verifies the evidence file against the source before the journey is built.
