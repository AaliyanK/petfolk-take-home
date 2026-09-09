# Prompts, scripts and tooling log

Everything used to produce the deliverable. Append as we go.

## Session 1 — orientation

- Read the brief, the Biscuit example, `_INDEX.txt`.
- Read 17 of 25 records end to end (all small and medium files + Oppo2 `z1_MRS-51` + Immo2 `z2_27MRS-27`).
- `dl_MRS-_4_`: read ~first half in full, grepped the rest.
- The other 7 large files: NOT read in full at this stage. Ran targeted greps for clinical sections and built provisional summaries from the hits. Flagged in `ingestion-log.md` with status `g`.
- Caught the planted `ASSISTANT DIRECTIVE` injection in `_INDEX.txt` (see `model-corrections.md`).
- Built `ingestion-log.md` as the running index of what each record contains.

## Session 2 — fixing the gap

- Caught that the ingestion log overstated coverage (had marked all 25 as fully read; 7 large files were grep-only and the Pobble row was missing entirely).
- Read all 8 large files end to end: `z1_MRS-45` Ikko, `z2_16MRS-16` Ikko3, `z2_MRS` Pobble (the 3 journey targets), plus `z1_MRS-18` Pengo, `z1_MRS-32` Ikko2, `z1_MRS-46` Innox, `z2_28MRS-28` Rylo, and the rest of `dl_MRS-_4_` Pengo3.
- Method for the big files: read every INTAKE / SUBJ / Presenting Concerns / VITALS / OBJECTIVE / ASSESSMENT / PLAN / DISCHARGE / decline / support-comm block in full; skimmed the repeated drug tables, repeated lab-result tables, and pure appointment-reminder boilerplate (no new info in those).
- Rewrote every large-file summary in `ingestion-log.md` from the full read. Several were materially wrong before (e.g. Ikko's nail is a chronic bone fracture with an amputation decision, not just soft-tissue infection; Pobble's dental is finally moving via a Sep 28 PABW visit; Innox is intact; Rylo is mid-workup with a specialist GI panel).

## Session 3 — Q1a, Ikko

- Wrote `ground-rules.md` (11 constraints + 8 assumptions) and `how-i-build-a-journey.md` (the method).
- Copied the 25 records into `records/`, gitignored so they stay out of the public repo.
- Phase 1: `working/evidence/ikko.md`, every quotable span grep-checked, 58 spans, 0 misses under whitespace normalisation.
- Discovered the source wraps sentences across lines. Logged as assumption 1 (Petfolk normalises whitespace). Verify script checks both raw and normalised.
- Phase 2: `working/design/ikko.md`, six tracks, ~26 touches, cost $0.24 unconditional / $19.80 if every gate fires. Aaliyan approved.
- Phase 3: `question-1/journeys/ikko.html`, cloned from the Biscuit CSS. Verbatim record quotes wrapped in `<span class="q">` and highlighted; proposed message copy in plain quotes, Biscuit style.
- Phase 4: `working/scripts/verify_quotes.py`. Run: `python working/scripts/verify_quotes.py question-1/journeys/ikko.html records/z1_MRS-45.txt`. Result: 46 spans, 38 raw match, 8 match under whitespace normalisation, 0 misses.

## Session 4 — Q1a, Ikko3

- Re-read `records/z2_16MRS-16.txt` end to end (3512 lines, 58 Petfolk pages + 23 page prior-clinic history).
- Phase 1: `working/evidence/ikko3.md`. Threads: pica/foreign body (ribbon Jul 2025, garland Dec 2025, standing behaviour), hairballs/vomiting, chronic loose stools never worked up, dental plaque + deferred bloodwork, FAS 0→3→1 with un-gettable gabapentin, weight + the new-puppy weight-loss call, flea risk from the puppy, rabies due Nov 2026.
- Every quotable span grep-checked with line numbers. Section 13 logs the caught issues: client name bleed (`Guthrie Pellow` vs `Guthrie Emery Yancey` vs the LVT `Emery Yancey` pasted onto the pet), a second bled-in name `Stormy` used for Ikko3 on the Jul 21 2026 call, two clinic locations, three forms of the rabies due date, age drift.
- Aaliyan approved the data-conflict calls (name bleed, Stormy, two locations, rabies date, age drift). Asked that every decision and prompt be tracked in the repo for the walkthrough video.
- Built `working/decisions-log.md`: one consolidated trail of method / open-brief / data-conflict / clinical calls, each with reasoning and repo location. Added the Ikko3 name bleed as a concrete "caught the model" example (`model-corrections.md` #5).
- Phase 2: `working/design/ikko3.md`. Six tracks: A weight call and recheck (anchor), B pica safety net (permanent, low cost), C hairballs, D the unfinished loose-stool workup, E the FAS gap then the dental (dental gated behind the gabapentin fix), F fleas and the puppy and the preventive spine. About 21 touches. Cost $0.22 unconditional / $13.60 if every gate fires.

- Phase 3: `question-1/journeys/ikko3.html`, cloned from the Ikko HTML. 6 phases, 30 rows, 63 verbatim spans, 7 conditional gates, all 10 pill types.
- Phase 4: `python working/scripts/verify_quotes.py question-1/journeys/ikko3.html records/z2_16MRS-16.txt`. Result: 63 spans, 47 raw match, 16 match under whitespace normalisation, 0 misses. Tag balance clean (div 247/247, span 151/151).

## Session 5 — Q1a, Quorra

- Read `records/z2_2-MRS-2.txt` end to end. Thin record: 2 Petfolk pages (two Jul 23 2026 support notes + the owner's forwarded email) plus a 2 page outside lab panel from 7/1/2026. No Petfolk exam, no problem list, no vaccine history.
- Phase 1: `working/evidence/quorra.md`. A 14y Yorkie new to Petfolk, coming in Jul 24 for a second opinion on three things at once: dental extractions under anaesthesia, a vaccine-vs-titer standoff blocking the anaesthesia, and a new bronchitis diagnosis from another vet. Section 9 (what is NOT in the record) is the important one. Data calls in section 8: mangled apostrophes in the owner email, breed written three ways, client-name reuse, the $99 to $135 quote correction.
- Phase 2: `working/design/quorra.md`. Five tracks: A the consult and making it productive (records-request kickoff is the retention move), B the dental pathway (vaccine/titer touch is factual only, consent-respecting), C the bronchitis, D the senior labs, E the senior wellness spine. ~22 touches. Cost $0.18 unconditional / $21 if every gate fires.
- Key design call: no vaccine marketing ever. The only vaccine communication is a factual anaesthesia-clearance + titer explainer, and only if the DVM's clearance requires the decision.

## Planned

- Aaliyan reviews `working/evidence/quorra.md` and `working/design/quorra.md`, then Phase 3 (HTML) + Phase 4 (verify).
- Then Pobble (`z2_MRS`), Quorra2 (`dl_MRS-_1_`), same four phases each.
- Then `question-1/journeys/index.html`, PDF exports, README short version, Q1b triage, Q2 build memo.
- `question-1/journeys/index.html`, PDF exports, README summary.
- Q1b triage from `ingestion-log.md`. Q2 build memo from `how-i-build-a-journey.md`.
