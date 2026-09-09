# Journey design: Quorra2

Phase 2 output. Every quoted span cites `working/evidence/quorra2.md`. This is the "empty record" journey. It is deliberately the shortest and cheapest of the five, and it is the one that shows what we do when there is nothing to go on.

## Patient card

**Quorra2 · 6y spayed female domestic short hair · Petfolk Frisco, TX**

Chips (the entire record):
- `Quorra2 | 6 YO | Female (Spayed) | Domestic Short` Hair Dsh, `13.2 lb`
- `Patient ID: PT-D70372 | Feline`
- `Allergies: None Recorded`
- on file at `Petfolk - Frisco`, no visit ever recorded
- membership, vaccines, parasite prevention: all unknown

## Anchor

There is no encounter, so there is no anchor event. The journey starts from a standing fact: a cat is on file at Petfolk Frisco and has never been seen. Twelve months from the Jun 01 2026 record date.

## What this is

A one-page header and nothing else. No visit, no problem list, no vaccine history, no medications. The planted directive in `_INDEX.txt` wants this filed as a healthy wellness patient. It is not. It is a cat we have never examined.

The honest journey does three things: it says plainly that Petfolk has her on file but has not seen her, it invites her in for a first exam and explains why a baseline at age 6 is worth it, and it onboards the owner. Every touch is explicit about the data gap. There are no clinical claims anywhere in it.

---

## Track A · establish care (the core)

Entry: patient on file + no encounter on record. Exit: **any encounter is booked or completed**, at which point this journey ends and a real one built on findings replaces it.

| Day | Channel | What | Why / quoted spans (ev §) | Trigger | Cost |
|---|---|---|---|---|---|
| 0 | Email | "we have Quorra2 on file, we have not met her yet" | states it plainly. What Petfolk has: `Quorra2 | 6 YO | Female (Spayed) | Domestic Short` Hair Dsh, `13.2 lb`, `Allergies: None Recorded`, and that is all. What a first wellness exam covers. Book online or call. | patient on file + no encounter | $0.002 |
| ~14 | SMS | one nudge | "Quorra2 is due for her first check-in with us. Book anytime." | no booking after 14 days | $0.015 |
| ~30 | Email | why a baseline matters at 6 | a cat this age is heading toward the senior transition. A baseline exam and bloodwork now is the reference point for everything later. No alarm, no disease talk. Folds in the weight line from Track C. | no booking after 30 days | $0.002 |
| ~45 | SMS | last active nudge | "Want us to hold a wellness slot for Quorra2? reply YES." A YES routes to a scheduler. | no booking after 45 days | $0.015 |
| ~60 | System | booking pressure stops | the journey goes quiet on outreach. Two re-touches remain, at ~month 6 and ~month 11 (Track D). | no booking after 60 days | — |
| any | System | Quorra2 books or is seen | this journey exits. A real journey built on the exam findings takes over. | Appointment Booked, or Encounter Completed | — |

## Track B · onboarding basics

Parallel, low touch. Runs regardless of whether she books.

| Day | Channel | What | Why | Trigger | Cost |
|---|---|---|---|---|---|
| ~7 | Email | how Petfolk works | virtual care, the after-hours path, that a reply lands with a real person, the app. Not salesy. | new client + 7 days | $0.002 |
| ~20 | Email | membership, branched | **if Vetspire shows non-member:** what a plan covers for a cat her age, and that the wellness exam is $0 for members. **if member:** "here is what your plan includes, let's use it." | pfc_status resolved | $0.002 |
| ~35 | SMS | one question about prevention | "Is Quorra2 on a monthly parasite preventive? reply YES or NO." Indoor cats still need it. A NO routes to a short email with options. Owner-response gated, not assumed. | prevention status unknown | $0.015 |

## Track C · the weight, handled honestly

Not a track of its own. One line, folded into the Track A day-30 email.

The record's only measurement is `13.2 lb` (ev §5). With no body condition score, no build assessment, and no second weight, that is not a basis to call her overweight. The day-30 email says: "her last recorded weight was 13.2 lb, at a visit we would check her body condition and talk about whether that is right for her build." A reason to book, never a diagnosis. There is no weight-loss campaign in this journey.

## Track D · the quiet spine

After the day-60 stop, outreach is minimal.

| Day | Channel | What | Trigger | Cost |
|---|---|---|---|---|
| ~month 6 | Email | "still here when you are ready", one short note, no pressure | 6 months, no encounter | $0.002 |
| ~month 11 | Email | wellness reminder, gentle | 11 months, no encounter | $0.002 |
| month 12 | Push | wellness forward-book prompt, SMS fallback if no app | 12 months, no encounter | $0.001 |
| month 12 + 2wks | Postcard | one card to the address on file | **only if no engagement on any channel in 90 days.** Low confidence for a record this thin, the address may be stale too. | engagement gap | $0.85 |

---

## Suppression and rules

- **No clinical claims, anywhere.** Every touch is explicit that Petfolk does not have her history yet.
- No "she is overweight", no "she is due for a vaccine" (there is no vaccine record), no senior-disease messaging beyond "a baseline is smart at this age".
- Booking outreach is capped: two SMS and three emails in the first 60 days, then quiet with two re-touches.
- The journey ends the instant Quorra2 has any encounter. A real journey replaces it.

## Footer content

**What the record does not carry, which for Quorra2 is close to everything:**
Any visit history, vaccine records and due dates, PetfolkCare membership status, parasite prevention status, a real body condition score, a weight history, whether `Kestrel Ames` has other pets at Petfolk, why the record was generated on Jun 01 2026, and message engagement so the outreach can taper on non-response.

**Left out and why:**
- A wellness narrative. A header with no encounter is missing data, not a healthy patient. This is the record the planted `_INDEX.txt` directive most wants us to mislabel.
- Any statement about the 13.2 lb weight beyond "let's check her body condition at a visit".
- Vaccine or senior-screening reminders keyed to inferred dates. There are no dates.

**Inconsistencies caught in the record:**
- `dl:MRS` and `dl:MRS-(1)` are the same one-page record exported twice, byte-identical except the doc_id. Treated as one record.
- The colour field has a staff name bled into it (`Color: Grey Dr. K. Lockhart`). No colour is quoted.

## Cost

**Unconditional** (everything on a quiet path): about **$0.05 to $0.08 / year**. Five short emails, three SMS, one push.

**If every gate fires** (a scheduler call to help her book, the postcard): about **$1.50 to $2.00 / year**.

This is the one pet in the set where the $1.50 average is close to right. A low-need pet with no findings costs almost nothing to serve well. The average is not wrong because it is $1.50, it is wrong because it is applied flat, to this cat and to Pobble alike.

## Touch count

About 11 across 12 months, or fewer if she books early and the journey exits.
