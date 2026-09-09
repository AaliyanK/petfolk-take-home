# Journey design: Ikko3

Phase 2 output. This is the plan the HTML is built from. Every quoted span cites `working/evidence/ikko3.md`.
Aaliyan reviews this before the HTML is built. The data-conflict calls behind it are D-IKKO3-1 to D-IKKO3-5 in `working/decisions-log.md`.

## Patient card

**Ikko3 · 2.6y spayed female Persian Mix · indoor only · Sandy clinic, Atlanta**

Chips (facts on file, quoted where possible):
- `Currently a Member` (PetfolkCare), not insured
- `Ikko3 is an indoor-only cat.` · `a domestic longhair cat`
- `Pica - Dec 02, 2025` · `Likes chewing on plants and xmas decorations`
- `Acute vomiting - Dec 02, 2025`, chronic hairballs, `Vomits approximately 2 times per week`
- `chronic intermittent loose stools - Dec 02, 2025`, never worked up
- `Dental plaque formation - Nov 11, 2025`, `Grade 1/4 dental tartar`, wellness bloodwork `deferred until a future anesthetic procedure, such as a dental cleaning`
- `Scared and typically does not cooperate`, FAS hit 3 in Nov 2025, gabapentin `Dispensed for pre-visit sedation` but the owner `reports difficulty administering this medication`
- new 8-week Golden Retriever puppy in the house about a month (household not linked in the data, flagged not used)
- rabies due Nov 2026, forward-booked reminder `Aug 01, 2026` and wellness `Nov 23, 2026`

## Anchor

Day 0 = the virtual care call on `Jul 21 2026` about possible weight loss after the puppy arrived. An in-person weight recheck was booked off that call for "Friday at 12:00 PM", about Jul 24, which is day 3. The record ends before that exam. The record's "now" is late July 2026. Twelve months run to July 2027.

## What this is

An indoor Persian cat with no headline diagnosis but a stubborn problem-list cluster. She eats non-food items, two foreign-body events on record. She vomits hairballs on a chronic basis. She has chronic loose stools the clinic said it would look into and never did. She has early dental plaque, and her routine bloodwork is on hold until she is under anaesthesia for a dental. She is getting more frightened at the vet each visit, and the sedation drug meant to fix that is one the owner cannot get into her. On top of all that, a new puppy just moved in and the owner thinks she is losing weight over it.

The journey does two things at once. It runs the anchor event (the weight call and recheck) and it works the problem list, in an order that respects the one dependency that matters: nothing anaesthetic happens until the gabapentin problem is solved.

---

## Track A · the weight call and the recheck

Entry: Support/Med Update logged + Appointment Booked (weight recheck). Exit: recheck completed and weight explained, or a workup opens.

| Day | Channel | What | Why / quoted spans (ev §) | Trigger | Cost |
|---|---|---|---|---|---|
| 0 | Virtual care | call logged, weight recheck booked | Owner thinks she is lighter since the puppy. Advice given: `Advised that cats may take several months to adjust to a new pet in the home and that subtle weight changes should still be evaluated, as cats can hide signs of illness.` (§9) | Med Update Logged + Appointment Booked | clinic |
| 0, eve | Email | recheck confirmation and what to bring | Confirms the booked time. Ask her to bring a fresh stool sample. The record shows `a fecal sample was not brought to the appointment` and a drop-off never happened, twice. One visit, two problems. Pre-visit sedation note points to Track E. | Appointment Booked | $0.002 |
| 3 | System | weight recheck happens | branches: weight stable, or weight down | Encounter Completed: recheck | — |
| 4 | Email | the result, in plain terms | **branch A, weight stable:** quotes the "several months to adjust" line, what to watch, when the puppy settling is not the answer. **branch B, weight down:** no numbers invented, points to the vet's next step. No auto-message names a diagnosis. | Encounter Completed + weight_status | $0.002 |
| 5 | Handwritten note | card from the technician who weighed her | **only if branch B, she came in and weight was a real concern.** Names the thing they noticed. Nothing to click. Biscuit parallel. | Weigh-in Recorded + concern_flag | $2.75 |
| 4 | SMS | "how is Ikko3 settling with the puppy? reply 1 to 3." 1 = eating and using the litter box normally. 2 = eating less or hiding more. 3 = not eating, vomiting, or not using the box. | cats hide illness, the record says so | Encounter Completed + household_change | $0.015 |
| 4 | Giga | answers the reply | 1 or 2 handled in chat from the visit notes and the "adjust over months" framing. A 3 goes to the nurse. | reply received | $0.05 |
| 6 | Nurse | tele-advice call | **only if she replied 3.** The nurse can see the weight trend, the GI history and the pica history and can rebook. | reply == 3 | $6.00 |

---

## Track B · pica and foreign body, the safety net

Entry: `Pica - Dec 02, 2025` on the problem list. No clean exit. This is a standing behaviour, so the track is a permanent low-cost safety net with an escalation path, not a timed campaign. Biscuit's safety-net pattern.

| Day | Channel | What | Why / quoted spans (ev §4) | Trigger | Cost |
|---|---|---|---|---|---|
| ~10 | Email | the linear-item safety brief | The single most important line in her record: `The owner was explicitly warned NOT to pull on a string if it is ever seen protruding from the rectum`. Why it matters: `A detailed discussion was had regarding the risks of linear foreign bodies, including the potential for them to anchor and cause the intestines to bunch up (plication), which is a surgical emergency.` The home fix: `It was recommended to remove access to all linear items, including ribbons, strings, hair ties, and wand toys`. New angle: a puppy in the house means new chew items and gift wrap around. | Pica on file + household_change | $0.002 |
| ~330 (early Dec) | SMS + email | holiday decorations warning | She has a December foreign-body history, `chewing on plastic garland`, and the problem list literally says `Likes chewing on plants and xmas decorations`. Tinsel, ribbon, garland, fake plants. What ingestion looks like, when to call versus when to go straight to the ER. | Pica on file + seasonal window | $0.015 + $0.002 |
| any | Giga to Nurse | urgent-symptom routing | **always on.** If a chat or reply pairs vomiting or retching with a known chew exposure, route to the nurse and the urgent-visit path, do not self-serve. | inbound + symptom + exposure match | $0.05 then $6.00 |

---

## Track C · hairballs and vomiting

Entry: `Acute vomiting - Dec 02, 2025` + long coat. Chronic, so no clean exit. Adherence touch delayed to ~day 20 so it does not stack on the anchor week.

| Day | Channel | What | Why / quoted spans (ev §5) | Trigger | Cost |
|---|---|---|---|---|---|
| ~20 | Email | the hairball plan, confirm the tools she has | `Recommended starting Laxatone to help manage hairballs by lubricating the gastrointestinal tract.` · `Give 0.5 to 1 teaspoon initially to help clear any existing accumulation.` · delivery trick for a cat that refuses things: `place a small dab on her paw, which encourages her to lick it off.` · `Please be mindful that giving too much can cause diarrhea.` · `Discussed using a slow-feeder bowl` · `REC getting a water fountain to encourage drinking more often.` Baseline to hold against: `Vomits approximately 2 times per week`. Grooming line: `Recurrent matting occurs on the back legs.` and she is `resistant to being brushed`, so a sanitary trim can ride along on the dental (Track E). | Vomiting on file | $0.002 |
| ~150 | SMS | "how many times a week is Ikko3 bringing up hairballs? reply with a number." | above her baseline of 2, or a number paired with weight or appetite change, is the signal for the `Ddx hairballs ... vs primary GI (IBD flare up)` question the record keeps raising | Vomiting on file | $0.015 |
| ~152 | Nurse | tele-advice | **only if the number is well above baseline or paired with weight loss.** This is the real re-decision point between a hairball problem and an IBD workup. | reply above threshold | $6.00 |

---

## Track D · chronic loose stools, the unfinished workup

Entry: `chronic intermittent loose stools - Dec 02, 2025` on the problem list, plus the clinic's own words `this is something that we can discuss in more detail at a future visit`, which never happened. Owner-interest gated so we do not push a workup she does not want.

| Day | Channel | What | Why / quoted spans (ev §6) | Trigger | Cost |
|---|---|---|---|---|---|
| ~40 | Email | name the loose stools, offer to pick it back up | The clinic flagged this and dropped it. `The owner reports a chronic history of intermittent loose stools`. The visible cost at home: `having to trim matted fur from the perineal area due to episodes of loose stool`. The open question: `Underlying intestinal disease like IBD possible.` Ask: a fecal and a diet conversation at the next visit, and bring a stool sample this time. | Loose stools on file + no workup event | $0.002 |
| ~44 | SMS | "want us to look into Ikko3's loose stools at her next visit? reply YES and we will add it to her chart." | a YES sets a care flag on the next encounter. No YES and it waits for the annual. | prior email delivered | $0.015 |

---

## Track E · the FAS gap, then the dental

The highest-value thread. Entry: FAS 3 on record, `Scared and typically does not cooperate`, gabapentin `Dispensed for pre-visit sedation`, owner `reports difficulty administering this medication`. The dental touch is gated behind the sedation fix on purpose.

| Day | Channel | What | Why / quoted spans (ev §7, §8) | Trigger | Cost |
|---|---|---|---|---|---|
| ~7 | Email | the pre-visit sedation fix | Name the problem: the drug is on the shelf, she will not eat it in a treat, it gets `it in her treats and refuses to consume it`. Options: open the capsule into a strong wet food or a Churu (Churu is already used with her per the record), the timing is `the night before and 2 hours prior`, and if that still fails, a short vet visit to try a different route or a gabapentin plus trazodone combo. The vet wants this solved: `For future visits, pre-medication with gabapentin is strongly recommended.` | FAS flag + Rx gabapentin dispensed | $0.002 |
| ~9 | SMS | "were you able to get the gabapentin into her last time? reply YES or NO." | a NO routes to Giga then the nurse for a real plan. This gate is what everything anaesthetic waits on. | prior email delivered | $0.015 |
| ~11 | Nurse | short tele-call | **only if she replied NO.** Work out a dosing route that actually lands before any sedated procedure is booked. | reply == NO | $6.00 |
| ~95 | Email | the dental cleaning, why it clears three things | `Dental plaque formation` plus `Grade 1/4 dental tartar` plus the deferred labs: `Recommended routine wellness lab work` `deferred until a future anesthetic procedure, such as a dental cleaning`. One anaesthetic event does the cleaning, the baseline bloodwork, and the sanitary trim for the matting. It needs her premedicated, which is why this lands after the sedation fix. In the meantime: `We recommend looking into products from the Veterinary Oral Health Council (VOHC)`, `This can include special diets, treats, or water additives.` PetfolkCare covers part of the dental. | Dental finding on file + sedation_plan resolved | $0.002 |
| ~109 | Support agent | call about the dental estimate | **only if an estimate was issued and not booked after about 10 days.** Cost, scheduling, membership coverage. Not the clinical side. Biscuit's day-34 agent call. | Estimate Issued: dental + not booked | $4.00 |

---

## Track F · fleas, the puppy, the preventive spine

| Day | Channel | What | Why / quoted spans (ev §10, §11) | Trigger | Cost |
|---|---|---|---|---|---|
| ~5 | Email | puppy introduction and flea plan | `The main health risk between them would be fleas, which the Revolution Plus will cover for Ikko3.` · `We recommend supervising their interactions closely, especially at first.` · `Make sure the puppy doesn't chase or overwhelm Ikko3,` · `give them separate spaces to retreat to.` Add: is the puppy on prevention too, so the household is covered (cross-sell, household not linked so this is a question not an assumption). | household_change + Rx Revolution active | $0.002 |
| ~Nov 2026 | SMS | Revolution Plus reorder | she got a 6-month supply in Jun 2026, so the reorder prompt lands about November. `Continue` `monthly`. | days_supply low | $0.015 |
| ~30 | Email | PetfolkCare value, retrospective | she is a member, so this is "your membership is working", not a pitch. Her June visit plus the Revolution supply, what the plan covered. | 30-day history + pfc member | $0.002 |
| Aug 1 2026 | System | the forward-booked rabies reminder fires | already in the record as `Dr. L. Marchetti rabies vx reminder` for `Aug 01, 2026`. The journey rides the existing booking, it does not invent a date. | existing booking | — |
| Nov 16 (annual −7) | SMS | confirm the forward-booked wellness on `Nov 23, 2026` | existing spine | existing booking | $0.015 |
| Nov 18 (annual −5) | Email | fear-free pre-visit for the annual | quotes `Scared and typically does not cooperate` and the FAS 3 episode, plus the gabapentin plan from Track E. Rabies gets sorted in person at this visit. | Appointment: annual + FAS flag | $0.002 |
| Nov 21 (annual −2) | SMS | gabapentin timing reminder | `the night before and 2 hours prior` | | $0.015 |
| month 12 | Push | next year's wellness forward-book | SMS fallback if no app engagement | 12 months since annual + no future appointment | $0.001 |
| month 12 + 2wks | Postcard | one card to the address on file | **only if no email, app or SMS engagement in 90 days.** Unlikely, this owner uses virtual care. | engagement gap | $0.85 |

**No vaccine-due touch fires off the text export.** Rabies due date appears three ways in the record (D-IKKO3-4). The Aug 1 reminder and the Nov 23 visit handle vaccines in person off the real booking records.

---

## Suppression rules

- Tracks C, D and E adherence touches are delayed past the anchor recheck week so they do not stack.
- Any "come in" or "schedule" nudge is held while the Jul 24 recheck loop is open.
- The puppy is `temporarily caring for an 8-week-old` per the record. If Household or a later note shows the puppy has left, Track F puppy framing and the weight-stress narrative in Track A both change. The journey does not assume the puppy is permanent.
- Track B urgent routing overrides suppression. A foreign-body concern always gets through.

## Footer content

**Data this journey leans on that the export does not carry cleanly:**
Appointment Booked and Appointment Completed events, structured vaccine records with a current flag and a real `next_due_date`, weight history as a series, BCS and FAS as coded fields over time, Rx dispensed versus filled versus refill requested, problem-list entries with a status (active, resolved, monitoring), household links, message engagement.

**Left out and why:**
- Household flea and parasite coordination with the puppy. The data does not link the household. It is a question in Track F, not an action.
- The transitional S1 vertebra. Benign incidental finding on the Dec 2025 radiographs, `should not create any issues`. One honest line in "what we are not doing", nothing more.
- A full IBD workup as its own track. That is a vet-led clinical decision. The journey surfaces the question in Tracks C and D and gates on owner interest, it does not drive a diagnosis.

**Inconsistencies caught in the record (ev §13):**
- Client and staff name bleed. Client is `Guthrie Pellow` on the header, `Guthrie Emery Yancey` in the history, and `Emery Yancey` is a Petfolk LVT who signs notes in the same file. The pet is written `Ikko3 Emery Yancey` eight times. No personal name is quoted anywhere in the journey.
- A second pet name, `Stormy`, is used for Ikko3 on the Jul 21 2026 call, including a weight figure. Not quoted. The weight story uses dated exam weights.
- Rabies due date in three forms. No overdue touch fired.
- Two clinic locations. Sandy treated as home clinic.

## Cost

**Unconditional** (everything that fires on a quiet path): about **$0.22 / year**. Roughly 6 SMS plus the Revolution reorder SMS, about 11 emails, 1 push, 2 Giga chats.

**If every gate fires** (replied 3 on the settling check, hairball rate spiked to a nurse call, a NO on the gabapentin gate, a stalled dental estimate, digital silence, the technician note after a concerning weigh-in): about **$13.60 / year**. Driven by two nurse calls, one agent call, the handwritten note and the postcard.

The spread is the point again. A cat with a solvable but stalled care plan sits mid-range. The $1.50 average describes neither number.

## Touch count

About 21 across 12 months, in the Biscuit range.
