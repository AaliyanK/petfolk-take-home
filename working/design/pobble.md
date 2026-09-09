# Journey design: Pobble

Phase 2 output. This is the plan the HTML is built from. Every quoted span cites `working/evidence/pobble.md`.
Aaliyan reviewed the evidence and approved the calls (see `working/decisions-log.md`, D-POBBLE and C-POBBLE rows).

## Patient card

**Pobble · 8y neutered male Chihuahua · Wake Forest, NC · PetfolkCare member**

Chips (facts on file, quoted where possible):
- `Pobble | 8.3 YO | Male (Neutered) | Chihuahua |`, `Currently a Member`, not insured, `No - no microchip found, owner declines`
- `Anxiety - Sep 16, 2024`, feral rescue, serotonin-syndrome history from concurrent fluoxetine and trazodone
- `Atopy - Jan 28, 2025`, Cytopoint failed, on Apoquel then quiet, currently `no meds, just simparica trio`
- `Periodontal disease, AVDC stage 3 - Jul 30, 2026`, `moderate to heavy dental calculus and gingivitis`, COHAT recommended
- `mature cataracts OU - Jul 30, 2026`, referral to `Animal Eye Care` offered
- soft cardiac finding from Sep 2024 (`Heart murmur and heart arrythmia!`), normal on the calm Jul 2026 exam
- `Heart worm positive in the past - Sep 16, 2024`, every test since negative
- lives with a second dog, Sindri, also a Petfolk patient
- pre-anaesthetic blood work booked for **Sept 28 2026**

## Anchor

Day 0 = the wellness exam on `Jul 30 2026`. Twelve months run to July 2027. The spine of the journey is getting Pobble from that visit, through the Sept 28 blood draw, to a dental under anaesthesia.

## What this is

An 8 year old feral-rescue Chihuahua with a stacked history: anxiety severe enough to destroy a wall, a serotonin-syndrome scare from being put on two anxiety drugs at once, an atopy flare that beat Cytopoint, and now stage 3 periodontal disease that needs a dental under anaesthesia. He also has mature cataracts, a soft cardiac finding from a bad-day exam two years ago, and two years of declined senior bloodwork.

The good news buried in the record: a pre-anaesthetic blood draw is already booked for Sept 28. That one appointment clears anaesthesia for the dental and finally produces fresh labs after two years. The journey's whole job is to get Pobble to that appointment in good shape, then through the dental, without tripping the anxiety or the drug-interaction history.

---

## Track A · the dental, wellness visit to COHAT (the spine)

Entry: AVDC stage 3 on the problem list + Estimate promised + PABW booked. Exit: COHAT completed (hands to the post-op mini-track) or the dental is declined.

| Day | Channel | What | Why / quoted spans (ev §) | Trigger | Cost |
|---|---|---|---|---|---|
| 0 | Visit | wellness exam | bordetella given, heartworm negative, two problems newly staged: `Periodontal disease, AVDC stage 3 - Jul 30, 2026` and `mature cataracts OU - Jul 30, 2026` (§4, §1) | Encounter Completed | clinic |
| 0, eve | Email | enriched discharge summary | the two new findings in the vet's words: `moderate to heavy dental calculus and gingivitis` and `mature cataracts OU, menace wnl but limited vision, unable to examine fundus OU, no ocular discharge`. The dental plan: `I recommend a professional dental cleaning within the next 1-2 months for him.` and `please schedule` `an appointment for his pre-op bloodwork first.` | Encounter Completed | $0.002 |
| 1 | Email | the dental estimate and the sequence | the promised estimate, `I` `will email you a dental estimate.` What a COHAT for stage 3 disease involves, likely extractions, and the order of operations: `blood work should be completed 1` to 2 weeks prior and `is typically` `valid for 30 days.`, so bloodwork Sept 28, then review, then book the COHAT. PetfolkCare coverage since he is `Currently a Member`. | Estimate Issued: dental | $0.002 |
| ~7 | SMS | **the anxiety-before-bloodwork check** | "Pobble's blood draw is Sept 28. To keep that visit low-stress, is he taking his fluoxetine every day right now? reply YES, NO, or NOT SURE." The record has him refilled on fluoxetine (Dec 2025) but the Jul 30 intake said `no meds, just simparica trio` (§8 E), and the vet's own plan was to `postpone the blood draw for these tests until an effective anxiety management plan is in place` (§7). | PABW booked + Anxiety on file | $0.015 |
| ~9 | Nurse | tele-call about the anxiety plan | **only if she replied NO or NOT SURE.** A real conversation about restarting `the plan is to consider restarting fluoxetine as a monotherapy` and whether a single pre-visit dose of gabapentin (which he tolerated) is wanted for the draw itself. A nurse, not an automated refill, because of the serotonin-syndrome history: `high suspicion of serotonin syndrome from concurrent` administration, and the hard rule `Discontinue fluoxetine and continue monitoring for signs of serotonin syndrome`. | reply NO / NOT SURE | $6.00 |
| ~14 | Email | PABW prep | fasting instructions, what the panel covers, and the pre-visit calm plan: gabapentin the night before and the morning of, the dose he tolerated, explicitly not a fluoxetine plus trazodone combination. FAS history referenced without drama. | mid-August | $0.002 |
| Sept 21 | SMS | PABW reminder, −7 | the Sept 28 8:30 AM technician visit, `Pobble scheduled for a technician visit on Monday, September 28th at 8:30 AM`. Bring him fasted, give the pre-visit gabapentin. | Appointment reminder, existing | $0.015 |
| Sept 26 | SMS | gabapentin timing reminder, −2 | | | $0.015 |
| Sept 28 | System | PABW happens | branches: cleared, something flagged, or no-show (to Track B) | Encounter Completed: PABW | — |
| ~+2 | Email | PABW results | **cleared:** results explained, especially whether the two-year-old `a very minor elevation in his liver enzymes that could be strictly due to aging` (§7) is still there. Next step is booking the COHAT inside the 30-day window. **something flagged:** the nurse calls, no automated message names a finding. | Lab Result: PABW + clearance_status | $0.002 |
| ~+5 | Email | the cardiac question, for the DVM | **only if the DVM flags it.** The record's own recommendation, `Recommend dental prophylaxis & cardiac workup due to murmur heard today and his history of HW disease` (§5). Framed as "your vet may want a quick heart check before anaesthesia", not an assertion that he has heart disease. | DVM flag: pre-anaesthetic cardiac | $0.002 |
| ~+10 | Support agent | COHAT scheduling and the estimate | **only if cleared and the COHAT is not booked about 10 days later.** Cost, PetfolkCare coverage, scheduling. The 30-day bloodwork validity window is the reason to move. | cleared + COHAT not booked | $4.00 |
| COHAT day | Visit | the dental procedure | hands to the post-op mini-track below | Procedure Performed: COHAT | clinic |
| exit | System | COHAT done, or the dental is declined and the topic drops to the annual | | Procedure Completed, or decline recorded | — |

### Post-op mini-track (fires on COHAT completion)

| Day | Channel | What | Cost |
|---|---|---|---|
| 0 | Email | post-op discharge: soft food, pain meds, what the extractions were, what to watch | $0.002 |
| 2 | SMS | "how is Pobble eating, any mouth pain or pawing at his face? reply 1 to 3" | $0.015 |
| 2 | Giga | answers 1 or 2 from the discharge, a 3 goes to the nurse | $0.05 |
| 4 | Nurse | tele-advice, **only if she replied 3** | $6.00 |
| 5 | Handwritten note | card from the technician, **only if it was a hard visit for him** | $2.75 |
| 10 | Email | back to normal food, plus the home dental plan to slow re-accumulation, VOHC products, and why the anaesthesia was worth it | $0.002 |

---

## Track B · appointment-keeping safety net

The record shows two prior cancellations (`Sent SMS regarding cancellation appt`, §8/§10). The Sept 28 PABW is load-bearing for the whole dental thread, so a missed one gets a firm, helpful re-book, not a passive "reschedule when you can".

| Day | Channel | What | Why | Trigger | Cost |
|---|---|---|---|---|---|
| Sept 28, same day | SMS | "we missed Pobble today, let's get his blood draw rebooked so his dental can move forward" | names the consequence: the dental cannot proceed without it, and stage 3 disease progresses while it waits | Appointment Cancelled / No-show: PABW | $0.015 |
| Sept 30 | Support agent | callback to rebook | one call, human, to find a slot that works. Not a nag sequence. | still not rebooked after 2 days | $4.00 |

---

## Track C · anxiety, the standing spine

Entry: `Anxiety - Sep 16, 2024` on the problem list. Chronic, no clean exit. Safety-framed, never marketing.

| Day | Channel | What | Why / quoted spans (ev §2) | Trigger | Cost |
|---|---|---|---|---|---|
| ~20 | Email | the anxiety plan, in writing | confirm the current plan is fluoxetine monotherapy, and the hard rule from his record: never fluoxetine and trazodone together, because of the `high suspicion of serotonin syndrome from concurrent` administration. Any new anxiety medication from any source, an ER, a boarding facility, a second vet, gets run past Petfolk first so the full list is in one place. | Anxiety on file + 20 days | $0.002 |
| when low | SMS | fluoxetine refill reminder | tied to the real prescription (Dec 2025 fill, 3 refills). One tap. | days_supply low | $0.015 |
| ~90, 180, 270 | SMS | behaviour check-in | destructive behaviour when left alone, appetite, any return of house-soiling (resolved, but a relapse marker), how he is doing with Sindri. Reply path to the nurse. | recurring | $0.015 each |
| any | Nurse | proactive check-in on a life event | **only if Vetspire shows a household change** (another move, loss of Sindri, a new pet). His anxiety and his house-soiling both tracked life events hard: `The history of urinating in specific locations` `following significant life stressors (new dog, new house) is highly suggestive of a behavioral cause`. | household_change event | $6.00 |

---

## Track D · atopy, dormant-watch

Entry: `Atopy - Jan 28, 2025`, currently quiet and off medication. No routine touches while quiet.

| Day | Channel | What | Why / quoted spans (ev §3) | Trigger | Cost |
|---|---|---|---|---|---|
| ~150 (approaching January) | SMS | "any itching, paw licking, or belly redness? reply 1 to 3" | the 2025 flare was a January one, and the oldest record lists `Seasonal Allergies`. A 2 or 3 opens the track. | Atopy on file + seasonal window | $0.015 |
| ~152 | Email or Nurse | the flare plan | a 2 gets the home-care plan (oatmeal bath, cone). A 3 gets a nurse, because a flare is a real re-decision for this dog: `Atopy, pruritic- no response to Cytopoint`, then Apoquel, then a prednisone taper. Not a refill. | reply 2 / 3 | $0.002 / $6.00 |

---

## Track E · the recurring spine

| Day | Channel | What | Why / quoted spans | Trigger | Cost |
|---|---|---|---|---|---|
| ~14 | (rider on the PABW prep email) | bring a stool sample to the Sept 28 visit | `Recommended fecal testing was deferred by the client to a future visit.` (§9). Ride the existing appointment rather than a separate ask. | fecal overdue + appointment booked | $0 |
| ~60 | Email | the cataracts | `he may be a good` `candidate for cataract surgery so that his vision improves significantly.` and the offer to `refer him to Animal Eye Care` (§8). Owner's call. Also practical support: a blind or low-vision senior does well with a stable home layout and routine. One email, no follow-up nagging. | mature cataracts on file | $0.002 |
| ~45 | Email | PetfolkCare value, retrospective | he is a member, so this is "your plan is working": the wellness visit, bordetella, the heartworm test, and what the COHAT costs with membership. | 45-day history + pfc member | $0.002 |
| ~Mar 2027 | SMS | rabies and DAPP reminder | `his Rabies and Distemper/Parvo vaccines are current` until `03/30/2027` (§9). Off the structured due date, not inferred. Handled at a visit. | vaccine due, structured feed | $0.015 |
| month 12 (~Jul 2027) | Push | annual wellness forward-book | SMS fallback if no app engagement | 12 months + no future appointment | $0.001 |
| month 12 + 2wks | Postcard | one card to the address on file | **only if no email, app or SMS engagement in 90 days.** Unlikely, this owner uses email, SMS and virtual care heavily. | engagement gap | $0.85 |

Lepto has never been given and was declined again on Jul 30 2026. It is not re-pushed. If the DVM wants it raised, that is one factual line at the annual about tick and lepto exposure, owner's decision.

---

## Suppression rules

- Track A, the dental spine, is the priority. Tracks D and E are timed around it.
- **No anxiety-medication marketing.** Track C is safety-framed only. Refill reminders are tied to a real prescription.
- The cardiac touch fires only if the DVM flags it. The journey never initiates "your dog might have heart disease".
- The cataract touch is one email, no nagging.
- If the dental is declined, Track A exits. The topic returns once at the annual with the AVDC stage noted.
- Track A's post-op mini-track and Track B's re-book override suppression.

## Footer content

**What the record does not carry, and what we would ask Vetspire for:**
Current medication status with a real active or inactive flag, the fluoxetine ambiguity is the clearest case in the whole set. Appointment Booked, Completed and Cancelled events, so the journey can react to the Sept 28 blood draw and to a cancellation the way this owner has cancelled before. Estimate Issued for the dental. Lab Result events for the PABW, to gate the COHAT on a real clearance. FAS as a coded field over time. Problem-list entries with a status, so `Atopy` reads as monitoring. Weight as a series. Referral Made events. Household links, since Sindri is in the same home, is a Petfolk patient, and the two dogs' behaviour problems are entangled.

**Left out and why:**
- Asserting a cardiac diagnosis. The finding is soft, was confounded by tremor and a drug reaction, and was normal on the calm exam. The journey raises the record's own question for the DVM and stops.
- Pushing fluoxetine as marketing, or assuming its current status. The journey surfaces the question and routes to a nurse.
- A full behavioural-training program. That is a vet or behaviourist referral. The journey supports it, it does not run it.
- Working up the polydipsia flag directly. The Sept 28 panel will speak to it.

**Inconsistencies caught in the record (ev §8):**
- Breed written three ways, `Chihuahua` on the Petfolk header, `Chihuahua - Mixed` on one outside record, `Rat Terrier` on another. Used the header.
- The family's move origin is given as both South Carolina and South Florida. The journey uses the pattern, not the origin.
- `Toby` is used for Pobble in one intake's free text. No alternate or personal name is quoted. Keyed on Patient ID `PT-306BA7`.
- The medication list shows fluoxetine active while the Jul 30 2026 intake says `no meds, just simparica trio`. Treated as an open question, not resolved by the journey.
- The murmur and arrhythmia were heard twice in Sep 2024 under extreme tremor and an active drug reaction, and the heart was `Normal rate and rhythm` on the calm Jul 2026 exam.

## Cost

**Unconditional** (everything that fires on a quiet path): about **$0.28 / year**. Heavy on SMS around the Sept 28 blood draw plus quarterly behaviour checks, roughly 10 emails, 1 push, 2 Giga chats.

**If every gate fires** (an anxiety-plan nurse call, a PABW result flag, the cardiac question, a stalled dental estimate, a missed appointment re-book, an atopy flare, the post-op nurse call and note): about **$24 / year**. Driven by three or four nurse calls, two agent calls, and the handwritten note.

A feral-rescue senior with a stalled stage 3 dental, a drug-interaction history, and an anxiety problem that gates the whole plan belongs near the top of the range. The $1.50 average describes neither number.

## Touch count

About 24 across 12 months, plus the six-touch post-op mini-track if the COHAT happens. In the Biscuit range.
