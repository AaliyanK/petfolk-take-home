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

## Planned

- Small Python pass to split every record on the `---` header, pull `doc_id` + `page_count`, and dump the 4 header lines + signalment line into one CSV for the triage table skeleton.
- For the 5 journey targets: extract candidate verbatim spans (diagnoses, drug names+sig, weights/BCS, next-due dates, decline lines) into a per-pet file so quotes are copied, never retyped.
