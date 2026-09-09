# Journey design: Ikko

Phase 2 output. This is the plan the HTML is built from. Every quoted span cites `working/evidence/ikko.md`.
Aaliyan reviews this before the HTML is built.

## Patient card

**Ikko · 7y spayed female Basset Hound Mix · Huntersville**

Chips (facts on file, quoted where possible):
- `Currently a Member` (PetfolkCare)
- `Body Condition Score: 8`, vet target `ideal weight ~27lbs`
- `Atopy - Oct 26, 2025`, on Apoquel long term
- `Chronic, displaced ungual process fracture of the right front fourth digit (P3, D4) - Jul 27, 2026`, amputation on the table
- `Nervous and resists meeting new people`, trazodone before visits
- `Odie pet insurance`
- housemate dog Rico (household not linked in the data, flagged not used)
- clinic `approximately an hour away`

## Anchor

Day 0 = the sedated nail procedure, `Jul 27, 2026`. The ortho follow-up email is day 1. The record's "now" is roughly day 2. Twelve months run to July 2027.

## What this is

One dog whose "recheck a toenail" turned into a chronic bone fracture of a weight-bearing toe, with amputation on the table, on top of a chronic skin allergy and a weight problem the vet has been chasing since last autumn.

---

## Track A · visit day and discharge

| Day | Channel | What | Why / quoted spans | Trigger | Cost |
|---|---|---|---|---|---|
| 0 | Visit | sedated nail-pull procedure, radiographs, culture taken | `Chronic, displaced ungual process fracture of the right front fourth digit (P3, D4).` (ev §4). Four meds dispensed. FAS handled with pre-visit trazodone. | Encounter Completed + Condition Diagnosed: nail fracture + Rx Dispensed ×4 + Sample Collected: culture + Procedure Performed | clinic visit |
| 0, eve | Email | enriched discharge summary | The diagnosis in the vet's words, plus home care: `strict rest with no jumping, stairs, or walks`, `she should be carried outside for elimination`, `An E-collar must be worn at all times to prevent licking at the bandage`, `return in two days for a recheck and bandage change`, and `A culture of the discharge from the nail bed was also collected today.` One line on the recessed vulva: watch for signs of a urinary or skin-fold infection (our words, it is on the problem list). | Encounter Completed | $0.002 |
| 1 | Email | the orthopedic opinion, follow-up | Already an email in the record. The journey makes sure it lands. Quotes `if the toe continues to be painful, amputation of the affected toe would provide the most reliable and definitive resolution`, `dogs generally adapt extremely well to the loss of a single digit and typically return to normal activity after recovery`, the conservative options `These include continuing antibiotics while the current infection resolves, using a soft padded bandage, or placing a splint under the paw`, and `A decision does not need to be made today`. | Consult Note Added | $0.002 |

---

## Track B · the nail, post-visit safety net

Entry: Condition Diagnosed: nail fracture + Rx Dispensed. Exit: Condition Resolved: nail, or Procedure Booked (the toe surgery, which hands off to the procedure funnel).

| Day | Channel | What | Why / gate | Trigger | Cost |
|---|---|---|---|---|---|
| 1 | SMS | recheck reminder: give trazodone 2 hrs before tomorrow's recheck, bring the E-collar | She is `Nervous and resists meeting new people`, protocol is `Trazodone 2 hrs prior to visit`. The recheck is already booked. | Appointment Booked: recheck + care_flag: high_fas | $0.015 |
| 2 | System | 2-day recheck happens, bandage change, wound assessed | branches: healing, or not | Encounter Completed: recheck | — |
| 3 | SMS | "how is Ikko's paw? reply 1 to 3." 1 = bandage clean and dry, she is leaving it alone. 2 = she keeps getting at it or the bandage slipped. 3 = swelling, odor, or she is not using the leg. | mirrors Biscuit's day-3 otitis check | Rx Dispensed: Cefpodoxime + Condition Diagnosed: nail fracture | $0.015 |
| 3 | Giga | answers the reply | A 1 or 2 handled in chat from the discharge, `An E-collar must be worn at all times to prevent licking at the bandage`. Anything it cannot answer from the record goes to Gladly. | reply received | $0.05 |
| 4 | Nurse | tele-advice call, paw not right | **only if she replied 3.** The nurse can see the radiograph, the culture status and the dispensed meds, and can rebook a recheck. | reply == 3 | $6.00 |
| ~7 | Email | culture result, current antibiotic is the right one | **only if the culture does not change the plan.** If it does, the nurse calls instead, no auto-message names a new drug. | Lab Result: culture + management_unchanged | $0.002 |
| ~12 | Email | the decision, no rush | Once the infection is settling. Restates the three options quoting the vet, and `A decision does not need to be made today`. Points to the surgeon and to the support line for cost. | Consult Note Added + Condition Status: stable | $0.002 |
| ~14 | Support agent | call about the surgical estimate | **only if a surgical estimate was issued and not booked after ~10 days.** Cost, scheduling, payment plan only. Not the findings. Mirrors Biscuit's day-34 agent call. | Estimate Issued: toe surgery + not booked | $4.00 |
| exit | System | toe surgery booked, procedure funnel takes over, or nail resolved, track exits | | Procedure Booked, or Condition Resolved: nail | — |

---

## Track C · weight, the spine

Entry: Weight Status Changed (BCS 8). Exit: Weight Status Changed to normal.
**Suppressed while Track B has an open recheck loop.** A "come in for a weigh-in, let us talk exercise" message collides with `strict rest with no jumping, stairs, or walks`. First touch delayed to ~day 45.

| Day | Channel | What | Why / quoted spans | Trigger | Cost |
|---|---|---|---|---|---|
| ~45 | Email | weight program entry, framed for a Basset | She is `Body Condition Score: 8`, target `ideal weight ~27lbs`. Vet's plan quoted: `Advised reducing her current food volume by a quarter of a cup daily.`, `Discussed that low-sodium green beans can be used as a low-calorie supplement to help with satiety.`, `Recommended reducing or eliminating high-calorie treats and table scraps, including the cheese used for medication administration.` Health framing quoted: `Discussed the weight loss plan and the associated health risks of being overweight, including an increased risk for diabetes and ligament tears`. The cheese problem is named: she takes several meds in cheese (`The owner reports giving cheese to help with medication administration.`), so the email offers pill pockets or a low-calorie alternative. CTA: a free technician weigh-in. | Weight Status Changed + bcs + breed_key | $0.002 |
| ~59 | Handwritten note | card from the technician who weighed her | **only after a weigh-in happens.** Names the thing she noticed. Nothing to click. Direct Biscuit parallel. | Weigh-in Recorded | $2.75 |
| ~66, then monthly | SMS | "two-minute weigh-in, no appointment needed" | exits on Weight Status Changed to normal | recurring | $0.015 each |

Honest framing note: her weight went 32 → 36 over the winter, back to 33 by July. The email frames it as back toward her autumn weight, then on to 27, not a fresh 10 percent cut.

---

## Track D · atopy

Entry: Condition on file + Rx: Apoquel active. Chronic, so no clean exit, ends if Apoquel is discontinued.
Adherence touch **delayed to ~day 20** so it does not stack on top of the acute nail meds.

| Day | Channel | What | Why / quoted spans | Trigger | Cost |
|---|---|---|---|---|---|
| ~20 | Email | Apoquel refill and adherence | The sig says `DO NOT skip doses, itching will return.` The record shows repeated Chewy refill friction. Confirms her refill is set and reminds her not to stop when the skin looks good. | Rx: Apoquel + days_supply low | $0.002 |
| ~240 (spring) | Email | allergy season is starting, the home-care plan | Her atopy is `consistent with a flare-up of environmental allergies` and worse since she `Recently relocated to North Carolina from the Poconos, with exposure to new grass and plants.` Quotes the vet's own advice: `I recommend bathing itchy dogs 1 to 2 times a week`, `wiping down your pet's fur with a moist cloth every time they come back inside`, `Omega 3 fatty acid supplementation also helps with allergies`, `non-scented, non-alcoholic baby wipe`. | season + geo + atopy on file | $0.002 |
| ~245 | SMS | "how is Ikko's skin? reply 1 to 3." 1 = fine. 2 = itchy but coping. 3 = raw, licking, red eyes. | she has `Allergic conjunctivitis` history, so red eyes is a real escalation signal | Condition on file + season | $0.015 |
| ~245 | Giga | answers the reply | 1 or 2 from the home-care plan. A 3 goes to the nurse. | reply received | $0.05 |
| ~247 | Nurse | tele-advice, flare not controlled | **only if she replied 3.** Real re-decision point: a Cytopoint injection or an Apoquel change. She declined Cytopoint twice before, so this is a genuine conversation, not a refill. | reply == 3 | $6.00 |

---

## Track E · dental

One touch plus a conditional line. Not a full track, the finding is minor and the estimate is stalled, not active.

| Day | Channel | What | Why / quoted spans | Trigger | Cost |
|---|---|---|---|---|---|
| ~90 | Email | a note about Ikko's teeth | `Discolored 203 tooth.` and `discussed sending estimates for dental cleaning and extraction of 202`. Explains a cleaning under anaesthesia, the PetfolkCare savings. The conditional bundle: if she needs sedation for the toe, 202 can be assessed on the same visit, one anaesthetic instead of two. | Dental finding on file + estimate not booked | $0.002 |

If a dental estimate is later issued and stalls, it folds into the procedure funnel, out of scope for this journey the same way Biscuit's does.

---

## Track F · the recurring spine

| Day | Channel | What | Why / quoted spans | Trigger | Cost |
|---|---|---|---|---|---|
| ~30 | Email | the insurance packet | She is `Odie pet insurance` and the record shows her `requesting email delivery of invoice and discharge notes for Ikko for pet insurance`. Auto-send the itemised invoice and discharge notes formatted for an Odie claim after the nail work. | Encounter Completed + insurance_provider on file | $0.002 |
| ~180 | Email | PetfolkCare savings, retrospective | "Ikko's last 6 months: the toe procedure, radiographs, the nail-bed culture, ongoing Apoquel. Your membership covered $X." She is a member, so this is "your membership is working", not a pitch. | 180-day event history + pfc member | $0.002 |
| Nov 12 (annual −7) | SMS | confirm the forward-booked annual on `Nov 19, 2026` | existing spine, the journey just notes it | existing | — |
| Nov 14 (annual −5) | Email | fear-free pre-visit for the annual | Biscuit Phase A, now for the annual. Quotes `Nervous and resists meeting new people` and the trazodone protocol. Fear-free tips. | Appointment: annual + care_flag: high_fas | $0.002 |
| Nov 17 (annual −2) | SMS | trazodone reminder | | | $0.015 |
| ~month 11 | Email | senior screening intro, age-framed | She turns 8 soon. Why baseline bloodwork starts at this age. Kept soft, the third-and-gentlest register, because she has been declining diagnostics. | Lifestage approaching senior (from DOB) | $0.002 |
| month 12 | Push | annual wellness forward-book for next year | SMS fallback if no app engagement | 12 months since annual + no future appointment | $0.001 |
| month 12 + 2wks | Postcard | one card to the address on file | **only if no email, app or SMS engagement in 90 days.** Unlikely for this owner. | engagement gap | $0.85 |

**No vaccine-due touch fires off the text export.** The two bordetella records conflict (ev §10B). Vaccine reminders depend on a structured Vetspire feed with a current-record flag. The annual visit sorts the vaccines in person.

---

## Footer content

**Data this journey leans on that the export does not carry cleanly:**
Appointment Booked, Estimate Issued, Consult Note Added, Rx days_supply and Refill Due, structured vaccine records with a current flag, weight history as a series, BCS as a coded field, an insurance_provider field, household links, message engagement.

**Left out and why:**
- The amputation decision itself. Owner's call, vet-led. The journey supports it, it does not push it.
- Household allergy management with Rico. The data does not link the household.
- Recessed vulva as a track. One line in the discharge email is enough.

**Inconsistencies caught in the record:**
- One radiograph block says `LEFT MANUS` and `left front digit four`, every other reference says right front digit 4. Treated as a clinic template error, quoted the right-front phrasing.
- Two bordetella records with different due dates. No vaccine touch fired off the export.
- Nail onset `Jun 23, 2026` on the problem list versus `07/03/2026` in a support note. Used the problem-list date.

## Cost

**Unconditional** (everything that fires on a quiet path): about **$0.24 / year**. Roughly 5 SMS plus 4 monthly weigh-in SMS, 10 emails, 1 push, 2 Giga chats.

**If every gate fires** (replied 3 on the nail, replied 3 on a spring flare, stalled surgical estimate, a weigh-in happened, digital silence): about **$19.80 / year**. Driven by two nurse calls, one agent call, the handwritten note and the postcard.

The spread is the point. A pet with an open surgical decision and a chronic allergy sits at the high end on purpose. The $1.50 average describes neither number.

## Touch count

About 20 across 12 months, in the Biscuit range.
