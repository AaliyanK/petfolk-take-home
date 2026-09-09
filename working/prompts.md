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
- Process note: evidence and design were produced in one pass here, collapsing the usual "evidence, Aaliyan reviews, then design" gate. Reason was the thin record (the evidence largely dictates the design). Aaliyan flagged it and confirmed the calls. Restoring the review gate for Pobble and Quorra2, which are large records.
- Phase 3: `question-1/journeys/quorra.html`, cloned from the Ikko3 HTML. 5 phases, 24 rows, 32 verbatim spans, 8 gates.
- Phase 4: `python working/scripts/verify_quotes.py question-1/journeys/quorra.html records/z2_2-MRS-2.txt`. Result: 32 spans, 12 raw / 20 whitespace-normalised / 0 misses. Tag depth balanced.

## Session 6 — Q1a, Pobble (evidence only, review gate restored)

- Read `records/z2_MRS.txt` end to end (6127 lines, 104 Petfolk pages + outside records). A single fecal table is duplicated across pages 57 to 82 (lines ~2560 to 4216), no content there.
- Phase 1: `working/evidence/pobble.md`. Five live threads: anxiety (serotonin-syndrome history from concurrent fluoxetine + trazodone at the first visit), atopy (Cytopoint failed, switched to Apoquel, now quiet and off meds), AVDC stage 3 periodontal disease (the live thread, PABW booked Sept 28 2026), a soft cardiac finding (murmur + arrhythmia heard twice in Sep 2024 under tremor, normal on the calm Jul 2026 exam), and 2 years of declined senior bloodwork (last panel Sep 2024 showed mild ALT/AST elevation, never rechecked).
- Central catch (evidence section 8 E): fluoxetine status is unclear. Med list shows it active (refilled Dec 2025, 3 refills), Jul 30 2026 intake says "no meds, just simparica trio". The vet's plan ties the stressful blood draw to "an effective anxiety management plan in place", and the PABW is now Sept 28. This is the journey's central branch.
- Per Aaliyan's instruction, stopped at evidence. Design not started until he reviews.
- Aaliyan reviewed and approved the calls (fluoxetine ambiguity as the central branch, cardiac finding as a DVM question, breed/name/move calls low stakes).
- Phase 2: `working/design/pobble.md`. Five tracks: A the dental spine (wellness visit to COHAT, with the anxiety-before-bloodwork check gating the Sept 28 PABW), B an appointment-keeping safety net (2 prior cancellations on record), C anxiety as a safety-framed standing spine (never fluoxetine + trazodone), D atopy as dormant-watch, E the recurring spine (cataracts, PetfolkCare, vaccines, fecal). ~24 touches plus a 6-touch post-op mini-track. Cost $0.28 unconditional / $24 if every gate fires.
- Tracked: decisions-log.md D-POBBLE-1..6 and C-POBBLE-1..5; model-corrections.md #6 (the med-list vs intake conflict as a "caught the model" example).

- Phase 3: `question-1/journeys/pobble.html`, cloned from the Quorra HTML. 6 phases (A dental spine, A after the dental, B appointment-keeping, C anxiety, D atopy, E recurring spine), 33 rows, 41 verbatim spans, 10 gates, all 10 pill types.
- Phase 4: `python working/scripts/verify_quotes.py question-1/journeys/pobble.html records/z2_MRS.txt`. Result: 41 spans, 34 raw / 7 whitespace-normalised / 0 misses. Tag depth balanced.

## Session 7 — Q1a, Quorra2 (the header-only stub)

- Read `records/dl_MRS-_1_.txt` (25 lines) and `records/dl_MRS.txt`. Byte-identical except the doc_id line (`dl:MRS-(1)` vs `dl:MRS`), same patient PT-D70372. One record exported twice.
- The whole record: Quorra2, 6y FS DSH cat, 13.2 lb, Frisco TX, owner Kestrel Ames, no encounter, no problem list, no vaccine history, nothing.
- Phase 1: `working/evidence/quorra2.md`. Sections 4 (what is NOT here) and 6 (what the journey can and cannot do) are the whole file.
- Phase 2: `working/design/quorra2.md`. The "empty record" journey. Three tracks: A establish care (get her in for a first exam, honestly, exits the moment she is seen), B onboarding basics, D a quiet spine. The 13.2 lb figure is a reason to book, never "overweight". No clinical claims anywhere. ~11 touches. Cost $0.06 unconditional / $1.85 if every gate fires, the one pet where the $1.50 average is close to right.
- Thin record, so evidence + design + HTML in one pass (like Quorra), flagged here.
- Phase 3+4: `question-1/journeys/quorra2.html`, 3 phases, 13 rows, 11 verbatim spans, 1 gate. verify_quotes.py: 11 spans, all raw, 0 misses.
- Tracked: decisions-log.md D-QUORRA2-1..3 / C-QUORRA2-1..4.

## All 5 Q1a journeys done

Ikko, Ikko3, Quorra, Pobble, Quorra2. Each: evidence file + design + HTML + verify_quotes pass (0 misses on all).

## Session 8 — Q1a index page + README short version

- Built `question-1/journeys/index.html`: the map to Q1a. One card per pet (signalment, the one-line shape, phase/touch count, cost range, link to the journey and its evidence file), the cost-spread table ($0.06 to $0.28 quiet, $1.85 to $24 loaded), the two hard nos, the 193-spans-0-misses line. Matches the journey CSS.
- Filled the README "short version": Q1a (what the journeys are + the verification), Q1b (the patterns), Q2 (pointer only, not drafted).
- No PDF exports, Aaliyan does not want them.
- Two forward links in index.html point to files not yet built: `../triage.md` (Q1b) and `../../question-2/build.md` (Q2). They resolve once those are written.
- Paused here per Aaliyan.

## Session 9 — Q1b, the 25-record triage

- Documented the AI / human division of labour: added a "Division of labour" section to `how-i-worked.md` and method decision M8 to `decisions-log.md`. Aaliyan wrote the split, I adapted it into the standing project model.
- Aaliyan approved the proposed rubric (archetypes, T0-T3 tiers with cost bands, cross-cutting flags).
- Built `question-1/triage.md`: the rubric, the 25-row table (archetype / tier / the 1-2 line call / do-not-send), a distribution check, a "What I changed" section for Aaliyan to fill after review, and the patterns section (compressed from `ingestion-log.md` observations).
- Built `question-1/triage.csv`: the same 25 rows as a machine-readable spec, columns mapped to Q2 engine fields (doc_id, archetype, tier, starts_on, highest_value_touch, do_not_send, flags, q1a_target).
- First-pass tier spread T0:5 / T2:10 / T3:9. Not a pyramid; flagged that the set is curated not sampled, and that Vorpal / Rylo / Ikko2 are the borderline T2-vs-T3 calls for Aaliyan.
- Data traps surfaced in the rows: the dl:MRS / dl:MRS-(1) export duplicate, Sindri (z1:MRS-16) as Pobble's housemate, Vorpal's contradictory "lepto booster Aug 7" note, the 6 stubs the injection wants mislabelled.

## Planned

- Aaliyan reads the 25 rows, marks what he would change, we fill "What I changed", revise.
- Then Q2: build memo (`question-2/build.md`) from `how-i-build-a-journey.md` + `ground-rules.md` + the Pengo3 raw Braze blocks.
- Voice-pass deliverable-facing docs. Aaliyan records the video.
- Q2: build memo (`question-2/build.md`) from `how-i-build-a-journey.md` + `ground-rules.md`.
- Voice-pass on deliverable-facing docs. Aaliyan records the video.
- Then `question-1/journeys/index.html`, PDF exports, README short version, Q1b triage from `ingestion-log.md`, Q2 build memo from `how-i-build-a-journey.md`.
