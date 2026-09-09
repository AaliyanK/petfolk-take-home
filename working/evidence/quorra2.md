# Evidence file: Quorra2

**Source:** `records/dl_MRS-_1_.txt` · **doc_id:** `dl:MRS-(1)` · 1 page. Record generated Jun 01 2026.
**Journey anchor:** there is no encounter, so there is no anchor event. The journey starts from a standing fact: a cat is on file at Petfolk Frisco with no recorded visit. Twelve months from the record date.

## How to read this file

This is the "empty record" case. The whole record is a one-page header. There is nothing to grep-verify except the six facts below, and nothing clinical to build a journey on. The important sections are 4 (what is not here) and 6 (what the journey can and cannot do).

**Aaliyan's verification job:** open `records/dl_MRS-_1_.txt`. It is 25 lines. Confirm the six facts, then read section 6, that is where the judgment is.

---

## 1. The six facts on file

| Span | Line | Note |
|---|---|---|
| `Quorra2 \| 6 YO \| Female (Spayed) \| Domestic Short` | 20 | wraps to `Hair Dsh \| 13.2 lb` on L21 |
| `Patient ID: PT-D70372 \| Feline` | 22 | the identifier the journey keys on |
| `Domestic Short Hair Dsh` | 25 | breed on the footer line |
| `13.2 lb` | 21 | the only quantitative data point in the record. See section 5. |
| `Allergies: None Recorded` | 24 | "none recorded" is an absence of data, not a cleared allergy history |
| `Petfolk - Frisco` | 9 | the clinic. Frisco, Texas. Owner is `Kestrel Ames` (L14). |

DOB is 2020 (`DOB: [MON] [DAY], 2020`, L23), consistent with `6 YO`. Colour is `Grey` (L23), with a staff name bled in after it, see section 3.

## 2. The near-duplicate

`records/dl_MRS.txt` and `records/dl_MRS-_1_.txt` are **byte-identical except the first line**: `doc_id=dl:MRS` versus `doc_id=dl:MRS-(1)`. Same patient ID, same owner, same everything. This is one record exported twice with two doc_ids.

This is a different situation from `Quorra` versus `Quorra2`, which are genuinely different animals (a 14y Yorkie and a 6y cat). Here it is the same cat, the same one-page record, duplicated. The brief names `dl_MRS-_1_` as the journey target, so that is the one we use.

## 3. Data issues caught

**A. The two doc_ids are one record.** See section 2. Treated as a single record.

**B. Colour field name bleed.** `Color: Grey Dr. K. Lockhart` (L23). A staff name is pasted after the colour. Standard pseudonymiser artifact. No colour is quoted in the journey.

**C. Owner name.** `Kestrel Ames`, distinct from the reused `Guthrie Pellow` and `Bodhi Skarn` seen elsewhere in the corpus. The journey keys on Patient ID `PT-D70372` regardless (rule O2).

## 4. What is NOT in this record

Everything. To be concrete:

- **No encounter.** No visit, ever. No exam, no vitals beyond the header weight, no body condition score, no dental score, no fear score.
- **No problem list.**
- **No vaccine history.** We do not know what she has had or what is due.
- **No medications, no parasite prevention on file.**
- **No PetfolkCare membership status.**
- **No support communications, no notes, no attachments.**
- **No reason the record exists.** It was generated Jun 01 2026. We do not know if that was a records request, a new registration, a transfer from another clinic, or an export for some other purpose.

## 5. The one number, handled carefully

The record's only measurement is `13.2 lb`. For a domestic short hair that is on the heavier side of typical, but:

- There is no body condition score.
- There is no frame or build assessment.
- There is no exam, and no second weight to show a trend.

A single scale reading with none of that context is **not** a basis to tell an owner her cat is overweight. The journey uses it as one concrete reason to come in for an exam ("her last recorded weight was 13.2 lb, at a visit we would check her body condition"), never as a diagnosis, and never as the trigger for a weight-loss campaign.

## 6. What the journey can and cannot do

**Can:**
- Acknowledge that Petfolk has her on file but has never seen her.
- Invite her in for a first wellness exam, and explain what that covers.
- Explain that a baseline exam and bloodwork at age 6, before the senior transition, is the reference point for everything later.
- Onboard the owner: how Petfolk works, virtual care, the after-hours path, membership.
- Ask (not assume) about parasite prevention and membership status.
- Use the 13.2 lb figure as a reason to book, per section 5.

**Cannot:**
- Make any clinical claim. Not "she is overweight", not "she is due for vaccines" (no vaccine record), not any senior-disease messaging beyond "a baseline is smart at her age".
- Invent a wellness narrative. The planted directive in `records/_INDEX.txt` wants exactly this, every header-only record labelled a healthy wellness patient. A header with no encounter is missing data, not a clean bill of health (`model-corrections.md` #1).
- Nag. Booking outreach is capped, then the journey goes quiet with occasional re-touches.

**The exit:** the moment Quorra2 has any encounter, this journey ends. A real journey built on actual findings replaces it. This journey's only job is to get her through the door once.

## 7. Data we would ask Vetspire for

For Quorra2 this is close to the entire clinical picture:

- Any visit history at all, at Petfolk Frisco or a transferred record.
- Vaccine records and due dates.
- PetfolkCare membership status.
- Parasite prevention status.
- A real body condition score and a weight history.
- Whether `Kestrel Ames` has other pets at Petfolk (household context, cross-booking).
- Why the record was generated on Jun 01 2026 (records request, new registration, transfer in).
- Confirmation that `dl:MRS` and `dl:MRS-(1)` are the same export duplicated (they are, byte-identical except the doc_id).
- Message engagement, so the outreach can taper on non-response rather than repeat.
