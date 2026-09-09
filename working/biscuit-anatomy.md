# Anatomy of "Biscuit's Year" (the example)

Reverse-engineered from `EXAMPLE-biscuits-year.html`. This is the format and quality bar for Q1a.
Biscuit is invented — nothing here is an answer, it's the shape of an answer.

## The patient card — every line is a switch

`Biscuit · 7.5y neutered male Beagle Mix · Ballantyne`

| Chip | What it unlocks in the journey |
|---|---|
| `FAS 4 on file, trazodone PRN` | The entire **Phase A pre-visit fear-free track**. No high-FAS flag → Phase A collapses to the plain transactional spine. |
| `not a PetfolkCare member` | Membership-savings messaging: the day-17 dental line and the dedicated day-90 savings email. |
| `app installed` | The **push** channel (day −1, day 24, month 12). Not installed → those fold into SMS. |
| `housemate cat` | Context flag (zoonosis / parasite framing). Lightly used here. |
| `booked: "vaccine / routine care"` | The whole premise: a *routine booking* produced **3 diagnoses + 1 declined service**. The journey reacts to what was **found**, not what was **booked**. |

## The encounter that drives everything

One visit, day 0, emits **eight events**:

> `Encounter Completed + Condition Diagnosed ×3 + Service Declined + Vaccine Administered ×2 + Weight Status Changed + Care Flag Updated`

- 3 conditions: **dental grade 2**, **BCS 7/9 overweight**, **otitis externa**
- 1 decline: **senior panel**
- 2 vaccines: rabies + bordetella (each with a next-due date)
- FAS updated 4 → 3

Each of those spawns or feeds a **parallel track**. The tracks overlap in time; they are not sequential phases.

## Every touch, in order

Legend: **SMS** $0.015 · **Email** $0.002 · **Push/in-app** $0.001 · **Giga chat** $0.05 · **Support agent** $4.00 · **Nurse** $6.00 · **Handwritten note** $2.75 · **Postcard** $0.85

### Phase A · pre-visit fear-free track  (trigger: Appointment Booked + care_flag: high_fas)

| Day | Channel | Content | Trigger / gate | Cost |
|---|---|---|---|---|
| −7 | SMS | Booking confirmation — **existing spine, untouched** | Appointment Booked | 0.015 |
| −5 | Email | "let's make biscuit's visit his calmest yet" — fear-free tips **+ his own trazodone instructions quoted from the Rx on file** | Appointment Booked + care_flag: high_fas | 0.002 |
| −2 | SMS | Trazodone reminder + refill check | — | 0.015 |
| −1 | Push | Visit-day checklist card | **only because app installed** (else folds into day −2 SMS) | 0.001 |

### Phase B · visit day

| Day | Channel | Content | Trigger | Cost |
|---|---|---|---|---|
| 0 | Visit | dental gr2 · BCS 7/9 · otitis externa · senior panel declined · 2 vaccines · FAS 4→3 | the 8-event encounter | (clinic) |
| 0 eve | Email | Enriched discharge summary — **all three findings in the vet's own words** + ear-med instructions "twice daily for ten days" | Encounter Completed | 0.002 |

### Phase C · otitis track  (trigger: Condition Diagnosed: otitis + Rx Dispensed → exit: Condition Resolved: otitis)

| Day | Channel | Content | Trigger / gate | Cost |
|---|---|---|---|---|
| 3 | SMS | "how are biscuit's ears with the drops? reply 1 to 3" | Condition Diagnosed: otitis + Rx Dispensed | 0.015 |
| 3 | Giga | Answers the reply in chat — from the dispensed Rx + discharge instructions **on file**. Can't answer from the record → hands to Gladly, **not guessed** | reply received | 0.05 |
| 4 | Nurse | Tele-advice call, ears not improving — nurse can see cytology + dispensed med, can book a recheck on the call | **only if he replied 3** | 6.00 |
| 10 | Email | Finish the full course, book the recheck — recurrent-otitis education | — | 0.002 |
| 14 | System | Ears clear → otitis track exits | Condition Resolved: otitis | — |

### Phase D · dental track  (trigger: Dental Grade Updated: 2 + conditions catalog + pfc_intake_status)

| Day | Channel | Content | Trigger / gate | Cost |
|---|---|---|---|---|
| 17 | Email | "a note about biscuit's teeth from dr. k" — grade 2 explained, what a COHAT is, **+ the PetfolkCare savings line** | Dental Grade Updated: 2 + pfc_intake_status | 0.002 |
| 24 | Push | Light education: what grade 2 gum disease means | — | 0.001 |
| 31 | Email | COHAT booking — **with the declined senior panel folded in**: "Pre-anaesthetic bloodwork is required anyway, and at his age we run the senior panel on the same draw. One visit, both covered." | dental step 3 + Service Declined: bloodwork_diagnostics | 0.002 |
| 34 | Support agent | Call about the estimate — **cost / scheduling / payment plan only. Does not discuss findings; anything clinical → nurse queue** | **only if estimate opened and not booked** | 4.00 |
| 31–45 | System | Books → procedure funnel takes over. Doesn't → journey pauses | Procedure Estimate Issued | — |

### Phase E · weight track  (trigger: Weight Status Changed + bcs + breed_key → exit: Weight Status Changed: normal)

| Day | Channel | Content | Trigger / gate | Cost |
|---|---|---|---|---|
| 45 | Email | Weight program entry — BCS 7/9, target ~10% over four months, framed for a food-motivated Beagle, free tech weigh-in as CTA | Weight Status Changed + bcs + breed_key | 0.002 |
| 59 | Handwritten note | Card from the technician who weighed him — "two pounds down," signed, names the thing she noticed. **Nothing to click, nothing to buy** | **only after a weigh-in actually happens** | 2.75 |
| 66 | SMS | "two-minute weigh-in, no appointment needed" — **monthly after that** | — | 0.015 |

### Phase F · the recurring spine (always on)

| Day | Channel | Content | Trigger / gate | Cost |
|---|---|---|---|---|
| 90 | Email | PetfolkCare savings — **retrospective math**: "Biscuit's last 90 days: ear treatment, dental consult, senior screening ahead. A membership would have covered $X." | 90-day event history + pfc_intake_status: not_member | 0.002 |
| month 10 | Email | Bordetella due in 60 days — existing vaccine canvas + per-vaccine plain-language explainer | Vaccine Administered.next_due_date | 0.002 |
| month 11 | Email | Senior onboarding — bi-annual cadence, age-framed senior-panel education. **"The third and gentlest ask."** | Lifestage Changed: senior (computed from DOB) | 0.002 |
| month 12 | Push | Annual wellness booking, forward-book framing | 12 months since Encounter Completed + no future appointment | 0.001 |
| month 12 + 2wks | Postcard | Physical card to the address on file — **"the last channel that still works when the digital ones have stopped. One card, not a series."** | **only if no email/app/SMS engagement in 90 days** | 0.85 |

## The cost math (this is the answer to "is $1.50 right?")

**Unconditional spend — everything that fires for every pet like Biscuit:**
4 SMS (0.06) + 9 Email (0.018) + 3 Push (0.003) + 1 Giga (0.05) ≈ **$0.13 / year**

**If every conditional gate fires:**
+ nurse 6.00 + agent 4.00 + handwritten note 2.75 + postcard 0.85 ≈ **+$13.60**

So a fully-escalated year ≈ **$14**, a quiet year ≈ **$0.13**. The $1.50 average is meaningless as a flat number — it's the blended result of most pets costing cents and a few costing $10+. **Spend follows medical need.** Our Q1b/Q2 answer: tier the budget (~$0.30 healthy / $3–8 active-condition), don't average it.

## The 12 design moves to reuse in our journeys

1. **Event-driven, not calendar-driven.** Every touch hangs off a named event, not a date.
2. **Parallel condition tracks**, each with an entry trigger **and an exit trigger**, that self-terminate (`Condition Resolved`, `Weight Status Changed: normal`).
3. **Cheap-first escalation ladder.** SMS check-in → Giga → nurse, each step gated on the pet parent's own signal (`replied 3`).
4. **Two human queues, split by nature.** Nurse = clinical. Agent = cost/scheduling/payment. They don't cross.
5. **Every clinical claim is quoted from the record** ("the vet's own words," "the Rx on file"). This is the string-match rule, lived.
6. **Additive to the transactional spine**, never replacing it. "existing spine, untouched."
7. **Channel chosen by profile** — app installed? engagement in last 90 days? — with graceful fallback (push → SMS, digital → postcard).
8. **Declines re-raised opportunistically and bundled** into a visit they're already having ("same draw, one visit, both covered"). Highest-value play in the whole journey.
9. **Membership woven into clinical moments**, plus one dedicated retrospective-math email with a concrete "$X."
10. **Repeated asks are spaced and softened** — senior panel asked 3×, explicitly "the third and gentlest."
11. **At least one human gesture with no CTA** — the handwritten note. Relationship, not conversion.
12. **Digital-silence fallback to physical mail — one card, not a series.**

## What the example leaves implicit (gaps our answer should close)

- **No consent / opt-out / STOP handling shown.** Clinical-comms opt-in vs marketing opt-out is unaddressed.
- **No template-approval / medical-review step** — the exact risk the brief flags ("no medical review board sign-off").
- **No suppression during an active clinical recheck loop.** Biscuit's otitis track politely exits, but real records (Immo2 every 2 wks, Ikko's nail weekly) would collide with marketing cadence.
- **`$X` membership savings** implies a computed figure — needs a data source we don't have in the export.
- **The "2" reply path** (mild concern) isn't shown — only 1 (fine, Giga) and 3 (escalate, nurse).
- **FAS 4→3 is recorded but doesn't change any downstream cadence** in the example. Should it?
