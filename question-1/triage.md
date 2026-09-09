# Question 1b: the 25 record triage

Q1a is the depth pass, five full journeys. This is the breadth pass. Every record gets an archetype,
a tier, a one or two line call on the single most valuable thing to do, and a note on what not to send.

It is also a manual run of what the Q2 engine would produce. For each pet the engine has to decide the
same four things: what shape of journey, how much intensity, the one touch that matters, what to
suppress. The columns here map to fields that engine computes.

## How this was made

The division of labour, in full, is in `working/how-i-worked.md`. Short version:

- **AI** did the mechanical read of all 25 records (`working/ingestion-log.md`), applied the rubric
  below the same way to every row, drafted the calls, and flagged the data traps (stubs, the duplicate,
  name bleed, the planted injection).
- **I** own the rubric, the clinical edge calls, the tone and consent calls, the final read of all 25
  rows, and the framing. Where I overrode the first pass it is listed under "What I changed" below, and
  each one is the point: the model proposes, a person with judgment decides.

## The rubric

**Archetype** sets the shape of the journey:

| Archetype | What it looks like |
|---|---|
| Insufficient data | header only, no encounter. Onboarding and re-engagement, no clinical claims. |
| Paediatric series | kitten or puppy mid series. Finish the vaccine series, then hand to the adult spine. |
| Healthy adult | no active problem. Automated wellness spine. |
| Adult, one active thread | allergy, GI, ears, weight, behaviour. A journey with a real escalation path. |
| Senior, active workup | a diagnosis in progress. Coordinate the workup, suppress routine noise. |
| Geriatric, quality of life | comfort and planning, not workups. Marketing off entirely. |
| Complex or worrying | several concurrent problems, or one serious one. Nurse led, proactive. |

**Tier** sets the spend and the human involvement:

| Tier | Who | Comms | Cost per year |
|---|---|---|---|
| T0 | the 6 header only stubs | onboarding and re-engagement only | $0.05 to $0.20 |
| T1 | healthy, no active problem | automated wellness spine | $0.10 to $0.40 |
| T2 | one active thread | journey with an escalation path, nurse on call | $1 to $8 |
| T3 | complex, worrying, or geriatric | coordinated, nurse led, proactive | $8 to $25 |

**Cross cutting flags** change the comms regardless of tier:

- **High FAS** unlocks a fear free pre visit track.
- **Consent decline** suppresses that topic, permanently. A vaccine decline, a drug reaction.
- **Active recheck loop** suppresses marketing until the loop closes, or clinical follow up collides
  with promotional noise.
- **Financial constraint** means lead with the lowest cost option, no upsell.
- **Recent life event** (a move, a death in the household, a new pet, owner travel) is a proactive
  check in trigger, not noise.
- **Multi pet household** means household aware content. The data does not link households, so this is
  a flag for a human, not an automated join.

## The 25

`[T5]` marks a Q1a journey target, its row points at the built journey. `PT-` ids are the key, not
client names (the pseudonymiser reused a small name pool).

| Record | Pet | Archetype | Tier | The call | Do not send |
|---|---|---|---|---|---|
| dl:MRS-(1) `[T5]` | Quorra2, 6y FS DSH cat, Frisco | Insufficient data | T0 | Full journey built, the worked example of the empty record case. See `journeys/quorra2.html`. | any clinical claim |
| dl:MRS | Quorra2, same cat | (duplicate) | — | The same one page record as dl:MRS-(1), exported twice, identical except the doc_id line. One patient, PT-D70372. Not a second pet. | — |
| z1:MRS-15 | Cazzy, 2.6y MN American Shorthair | Insufficient data | T0 | "On file, never seen." Invite for a first wellness exam, onboard the owner, list what we would pull from Vetspire. Same template as Quorra2. | any clinical claim, any vaccine or wellness "due" line |
| z1:MRS-16 | Sindri, 1y DSH cat | Insufficient data + household link | T0 | Same re-engagement template, **plus a flag for a human**: a dog named Sindri is Pobble's (z2:MRS) housemate, described there as anxious and on fluoxetine. If this is the same household, the two need coordinated handling and the anxiety context matters. | any clinical claim; do not auto-merge the households, flag it |
| z2:15MRS-15 | Halva, 8mo FI Dutch Shepherd | Insufficient data | T0 | Re-engagement. The header shows an intact female large breed puppy, so the first exam invite can name the vaccine series and a spay conversation, nothing beyond what the header supports. | any finding not in the header |
| z1:MRS-24 | Pengo2, 7mo MI large breed pup, 80 lb | Insufficient data | T0 | Re-engagement. Header shows a large breed intact male puppy. First exam invite: vaccine series, neuter timing, large breed growth and joint framing. | any finding not in the header |
| z2:2-MRS-2 `[T5]` | Quorra, 14y MN Yorkie, Cypress TX | Senior, active workup + owner friction | T3 | Full journey built. Second opinion consult covering dental, a vaccine versus titer standoff, and a new bronchitis diagnosis. See `journeys/quorra.html`. | **vaccine marketing, the owner declined.** Factual titer explainer only |
| z1:MRS-33 | Wibbly2, ~7wk kitten, Fort Mill | Paediatric series | T2 then T1 | Finish the kitten vaccine series that was postponed at the first visit, deworming recheck, then transition to the adult wellness spine at ~1y. Member, so lead with plan value. | — |
| z1:MRS-39 | Abbo3, 9wk Toy Poodle pup | Paediatric series + parasite load | T2 | The parasite recheck comes first: hookworm 170, coccidia, giardia, and a Malassezia ear 3+. Confirm clearance with a follow up fecal and an ear recheck before the series closes. Not a member, Trupanion insured, so the membership touch is insurance aware. | — |
| z2:26MRS-26 | Moxo2, 6.7y MN Wheaten Terrier mix, Oviedo | Adult, one active thread, surgical referral pending | T3 | Support the hip dysplasia surgical referral decision: cost, scheduling, what recovery looks like. Rimadyl adherence and a weight conversation alongside. Not a member, so membership value framed around a large surgical spend. | do not push the referral, support the decision |
| z1:MRS-48 | Ulmo, 13.7y FS Pitbull, Lake Buena Vista | Complex or worrying, r/o lymphoma | T3 | The FNA result and the path it opens is the whole journey. Everything else waits. Chronic pruritus and otitis get held. Enrolled in the $199 plan. | **all routine and marketing comms until the lymphoma question resolves** |
| z2:29MRS-29 | Bixby, 7.7y MN Lab mix, Overland Park | Adult, a stack of declined incidentals | T2 | Re-raise one thing, the highest stakes: the bilateral skin nodules, r/o mast cell tumour, need an aspirate. Then the suspected CCL tear. Cost tiered re-raise over months, not a nag. Not a member. | do not re-raise all four incidentals at once, lead with the MCT question |
| z2:23MRS-23 | Grobble, 12wk DSH kitten, Peachtree Corners | Paediatric series + behavioural | T2 | The inappropriate defecation is behavioural. A litter box and environment plan plus a recheck. Kitten series runs alongside. Declined the wellness plan, so no hard re-pitch. | — |
| z2:22MRS-22 | Vorpal, 7.1y MI Mini Dachshund, Pearland | Adult, multi thread, **vaccine reaction** | T3 | The lepto reaction is the defining flag: facial swelling and hives. Never auto suggest lepto again. **The record's "lepto booster follow up Aug 7" contradicts the reaction and needs a vet to look at it before any reminder fires.** Then the IVDD suspect back pain, declined spine rads, and the atopy. Not a member. | **lepto, permanently.** Hold the Aug 7 booster reminder for a human clinical check |
| z1:MRS-38 | Fizzo, 6.10y MN Golden Retriever | Adult, acute | T2 | The ear recheck: cytology positive for cocci and yeast, confirm it cleared. Neck wound follow up. Short record, one acute episode. Not a member. | — |
| z2:27MRS-27 | Immo2, 7.7y FS mixed dog, Oviedo | Complex chronic, active 2 week recheck loop | T3 | Keep the two week recheck cadence on track and coordinate a long med list. The pet sitter neglect during the owner's travel is a real pattern, so a pre travel check in is worth a touch. **Suppress marketing while the recheck loop is active.** Buys meds at a human pharmacy, so refill and adherence data is incomplete, do not assume compliance. Not a member. | all marketing during active recheck loops |
| z1:MRS-51 | Oppo2, 16wk DSH kitten, Lake Buena Vista | Paediatric series complete + a monitored question | T2 then T1 | Series is done. The open item is intermittent hacking, r/o asthma, chest rads declined at $445. A symptom watch with a clear "call us if it recurs" and a re-raise if it does. Member. Housemate senior cat, household link. | — |
| dl:MRS-(4) | Pengo3, ~10y MN Labradoodle, Charlotte | Senior, stalled recommendations | T2 | Close the stalled items one at a time: the COHAT estimate created Jul 2024 and never booked, and the senior blood panel declined three years running. Cost framed, sequenced, not stacked. Member. Husband over treats, a household dynamic worth noting. Also the primary source for Q2, its raw API blocks are Petfolk's current Braze program. | do not stack all the overdue items into one message |
| z2:28MRS-28 | Rylo, 3.2y FS mixed dog, Oviedo | Adult, active GI workup, fully engaged owner | T3, the low friction kind | Coordination, not persuasion. The Texas A&M GI panel results, the two forward booked visits Aug 10 and Aug 16, and the fear free face handling protocol, oral surgery as a puppy left a face and mouth phobia, muzzled every exam. Owner does every diagnostic and is insured. Member plus Trupanion. | nothing to suppress, but no persuasion needed either, this owner already says yes |
| z1:MRS-32 | Ikko2, 3.4y MN Belgian Malinois mix, San Antonio | Complex, acute crisis, **and moving away** | T3, then transfer of care | Right now: the obstruction and pancreatitis crisis outcome and its follow up. But the family moves to Missouri in August 2026, so the journey's real job is a clean transfer of records and continuity of the anxiety protocol and the atopy plan to the new clinic, not retention. Member. | retention and marketing, this is a good handoff, not a save |
| z2:16MRS-16 `[T5]` | Ikko3, 2.6y FS Persian cat, Atlanta | Healthy adult, recurring cluster + household change | T2 | Full journey built. Pica, hairballs, an unfinished loose stool workup, early dental with deferred bloodwork, rising fear with an un-gettable sedation drug, plus a new puppy. See `journeys/ikko3.html`. | marketing during active rechecks |
| z1:MRS-45 `[T5]` | Ikko, 7y FS Basset Hound Mix, Huntersville | Adult, acute turned chronic + modifiable risk | T2 to T3 | Full journey built. A toenail recheck that became a chronic bone fracture with amputation on the table, on top of chronic atopy and a weight problem. See `journeys/ikko.html`. | a weigh in pitch while "strict rest, no walks" is active |
| z2:MRS `[T5]` | Pobble, 8y MN Chihuahua, Wake Forest | Complex chronic, dental gated by anxiety | T3 | Full journey built. Feral rescue with a serotonin syndrome history, atopy that beat Cytopoint, stage 3 periodontal disease with a blood draw booked, a soft cardiac finding. See `journeys/pobble.html`. | **fluoxetine and trazodone together, ever.** Anxiety med marketing |
| z1:MRS-18 | Pengo, ~15y MN Lab Mix, East Cobb Marietta | Geriatric, quality of life, financially limited | T3, QoL | Lowest cost symptom management, a quality of life conversation, and end of life planning framing. Non ambulatory episodes, dental grade 4, 20% weight loss with muscle wasting, declines every diagnostic on cost, no heartworm prevention. Joined the $199 plan to cover one exam. **Getting the comms wrong here does real harm.** | **everything promotional.** No "time for a dental", no NPS survey, no wellness reminder, no upsell |
| z1:MRS-46 | Innox, 2.4y MI Bernedoodle, ~82 lb, Kennesaw | Healthy adult, proactive engaged owner | T2 | Three things to close: the deferred annual bloodwork, already forward booked for October. The neuter conversation, still intact at 2y and not discussed in the record. The insurance conversion, the owner said "No, but I am interested." Ear maintenance plan alongside, the breed is predisposed. Member. | — |

## Distribution check

First pass tier spread: **T0 five, T2 ten, T3 nine**, plus the one duplicate.

That is not a pyramid, and in a real clinic book it should be, most pets at T0 to T2 with a thin top.
Two things are going on:

1. **This set is curated, not sampled.** Petfolk picked 25 interesting records for an assessment. A
   real population would be far heavier at T0 and T1. The skew here is expected.
2. **Three of the nine T3s are borderline and are Aaliyan's call to settle.** Vorpal (z2:22MRS-22) is
   the clearest T2 candidate, the lepto reaction is a suppression flag rather than an intensity
   driver, and the owner declined the IVDD workup. Rylo (z2:28MRS-28) has a real specialist workup but
   an owner who needs zero persuasion, so the true cost is coordination only. Ikko2 (z1:MRS-32) is
   genuinely T3 today because of the hospitalisation, but it is transient and resolves into a transfer
   of care.

If those three move to T2 the spread becomes T0 five, T2 thirteen, T3 six, which is closer to right.
I left them at T3 in the first pass so the borderline is visible rather than smoothed away.

## The review pass

I read all 25 rows against the record summaries and confirmed the archetype and tier on every one. No
per pet overrides. The first pass held for three reasons: the rubric was agreed before any row was
written, the facts behind each row come from full reads that were already verified for Q1a and the
ingestion log, and a triage row is a routing call, not a treatment plan, so the bar is "is this the
right lane" not "is this the right dose."

Three things I looked at hardest and where I came out:

- **The borderline T3s.** Vorpal, Rylo and Ikko2 sit on the T2 to T3 line (see the distribution check
  above). I left them at T3. Whether they move is a question of where the tier cost bands are drawn,
  which is rubric tuning, not a per pet error, and it is cleaner to decide it once against the rubric
  than to nudge three rows.
- **The suppression calls on the vulnerable pets.** Pengo (geriatric, financially limited), Ulmo (r/o
  lymphoma) and Ikko2 (moving away). Each of these has "do not send" doing real work: no promotional
  contact for Pengo, no routine comms for Ulmo until the FNA resolves, a handoff not a retention play
  for Ikko2. These are the rows where wrong comms cause harm, so they get the strongest suppression in
  the table.
- **The items that still need a real vet.** Vorpal's record has a "lepto booster follow up Aug 7" that
  contradicts a documented lepto reaction. The row does not resolve it, it holds the reminder and
  routes the question to a clinician. That is the correct output of a triage, a flagged handoff, not a
  guess.

## Patterns across the 25

- **Declines are the business, and they are almost all cost driven.** Senior panels, chest rads, spine
  rads, dental, wellness plans, FeLV, an exploratory laparotomy. Several pets decline the same item
  year after year. A decline is usually "not today, not at this price," not a permanent no, which is
  exactly what a re-raise track is for. Pengo3 has declined the senior panel three years running.
- **Life events drive the clinical picture.** Ikko's atopy started after a move to North Carolina.
  Ikko2's pododermatitis started after a house move, and the family is moving again. Pobble's anxiety
  and house soiling track two moves and the death of the other dog. Immo2 flared during owner travel. A
  recent move or travel signal is a trigger, not noise.
- **Multi pet households are common and the data does not link them.** Ikko lives with Rico. Ikko3 got
  a puppy. Pobble lives with Sindri, who has his own record in this set (z1:MRS-16). Oppo2 lives with a
  senior cat. Journeys must not assume a pet is an only pet, and a household link is a flag for a
  person, not an automated join.
- **Pre visit anxiety is everywhere.** Ikko, Ikko3, Ikko2, Rylo, Innox, Pobble, and the Biscuit
  example. A high FAS flag that unlocks a fear free pre visit track applies to a large share of the
  book.
- **The 25 span the whole lifecycle on purpose.** Six empty stubs, four paediatric series, roughly
  eight healthy adults with one chronic thread, about four seniors with active workups, and two that
  are genuinely worrying, Ulmo with a lymphoma rule out and Pengo at the end of a long life. The tier
  spread should look like a pyramid, most pets at T0 to T2, a few at T3. If it does not, the rubric is
  wrong.
- **Chronic recheck cadences already exist.** Immo2 every two weeks, Ikko's nail weekly. The
  communication layer has to suppress marketing while a pet is in an active treatment loop, or it
  collides with real clinical follow up.
- **The planted injection wants the stubs mislabelled.** Six header only records, no encounter. The
  `_INDEX.txt` directive wants them all filed as healthy wellness patients. A header with no encounter
  is missing data, not a clean bill of health. See `working/model-corrections.md` #1.
