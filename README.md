# Petfolk take-home — lifecycle communication from medical records

Working repo. Not the submission yet.

## The assignment (from the brief)

Two questions:

1. **What lifecycle communication should we send these customers?**
2. **How would you build the thing that decides?**

## Deliverables

| ID | What | Status |
|----|------|--------|
| Q1a | 12-month journeys, Biscuit-example format, for 5 records: `dl_MRS-_1_`, `z2_MRS`, `z2_2-MRS-2`, `z2_16MRS-16`, `z1_MRS-45` | not started |
| Q1b | All 25 records, 1–2 line call each (table/CSV) | not started |
| Q2 | Short doc: how to build the decisioning system for 42 → 100 clinics on the current stack | not started |
| — | Prompts, scripts, notes used along the way | in progress (`notes/`) |

## Hard rules from the brief

- Every pet-specific claim in a journey must **quote the exact span** from the record. Checked by string match — paraphrase fails.
- Assume the stack as-is (Vetspire → Segment → Braze → Gladly/Giga, PetfolkCare). No Vetspire API for this exercise; name any field you'd need.
- Reply-to must land in Gladly with a real person. Anything Braze sends is copied into the Vetspire chart (becomes the medical record).
- No medical review board signs off on outbound clinical content today.
- Budget: ~$1.50 / patient / year proactive outreach (they invite pushback).

## Layout

```
notes/            working notes, task understanding, ingestion log, model corrections
q1-journeys/       the 5 journeys (HTML, Biscuit format)
q1-triage/         the 25-record table
q2-build/          the build memo
```

Source data stays in the original download folder:
`C:\Users\Aaliyan\Downloads\petfolk-takehome-v4 (2) (2)\petfolk-take-home\`
