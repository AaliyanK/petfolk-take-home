# Q1a plan: the five journeys

## The pipeline, per pet

Five phases, one pet at a time, no batching. Full detail in `how-i-build-a-journey.md`.

1. Evidence file, grep-checked, Aaliyan verifies against the source.
2. Design in markdown, tracks and touches, Aaliyan makes the judgment calls.
3. HTML from the Biscuit template.
4. `verify_quotes.py` re-checks every quote.
5. Add to the index, export a PDF.

## Order and why

| # | Pet | Record | Why this slot |
|---|---|---|---|
| 1 | **Ikko** | `z1_MRS-45` | The Biscuit analogue. Weight spine plus an atopy track plus an acute track. Building it also builds the shared tooling: the evidence-file format, the cloned Biscuit template, `verify_quotes.py`, the footer structure. |
| 2 | **Ikko3** | `z2_16MRS-16` | Different shape. A cat, no headline diagnosis. The journey is built on a problem-list cluster, pica, hairballs, dental plaque, rising FAS, plus a household change, the new puppy. Tests whether the method works with no "Encounter Completed with three diagnoses" to anchor to. |
| 3 | **Quorra** | `z2_2-MRS-2` | The friction case. Triggered by support-desk events, not an encounter. Vaccine refusal blocking the dental the owner came in for. Outside lab data folded in by quoting the other clinic's report. Tests the two-human-queue split hard, nurse for the titer question, agent for the $869 estimate. |
| 4 | **Pobble** | `z2_MRS` | The complex chronic, 104 pages. The work is subtraction. In scope: COHAT support as the spine since it is already booked for Sep 28, a fluoxetine safety-net gated on the med being active, behavioural-urination resources. Out and named: cataracts, cardiac, liver enzymes. Benefits from the patterns being down. |
| 5 | **Quorra2** | `dl_MRS-_1_` | The empty stub. An honest near-empty journey: the transactional spine, one re-engagement touch, and a prominent "here is what we would need from Vetspire" block. Fast once the philosophy is set. Doubles as the clearest rebuttal of the `_INDEX.txt` injection. |

## Shared vs unique

**Built once for Ikko, reused for the other four:** the evidence-file format, the Biscuit CSS and HTML template, `verify_quotes.py`, the 11 ground rules, the footer structure, the trigger vocabulary, the assumptions.

**Unique per pet:** the evidence file, which threads become tracks, the judgment calls, the channel and gate choices, the "left out and why" list.

## Cadence with Aaliyan

For each pet: I do the evidence file and the design, Aaliyan verifies the evidence against the source and makes the calls, I build the HTML, the script verifies, we commit. Then the next pet. Every place Aaliyan pushes back goes into `how-i-worked.md`.

Rough weight: Ikko is the expensive one because it builds the template and the script. Ikko3, Quorra and Pobble are each lighter. Quorra2 is quick.

## After the five journeys

1. `question-1/journeys/index.html`, a one-paragraph explainer plus a table of pet, archetype, touch count, annual cost range, with links.
2. PDF exports of all five.
3. Fill in the README "short version" for Question 1.
4. **Q1b, the 25-record triage.** Most of this is already done. `ingestion-log.md` has a full entry per record. The triage table is that, compressed to a scannable row per pet with a recommended journey archetype and a priority.
5. **Q2, the build memo.** `how-i-build-a-journey.md` is the manual process. Q2 is "how this runs automatically across 100 clinics", which is the same eight steps turned into a system, plus the event contract with Vetspire, the guardrails, and the scaling and cost argument.
