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

- Caught that the ingestion log overstated coverage (had marked all 25 as fully read).
- Reading the 3 large journey targets (`z2_MRS`, `z1_MRS-45`, `z2_16MRS-16`) in full before drafting.
- Remaining 4 large files + rest of `dl_MRS-_4_` to be read in full before the triage table.

## Planned

- Small Python pass to split every record on the `---` header, pull `doc_id` + `page_count`, and dump the 4 header lines + signalment line into one CSV for the triage table skeleton.
- For the 5 journey targets: extract candidate verbatim spans (diagnoses, drug names+sig, weights/BCS, next-due dates, decline lines) into a per-pet file so quotes are copied, never retyped.
