# Evidence file: Pobble

**Source:** `records/z2_MRS.txt` · **doc_id:** `z2:MRS` · 104 Petfolk pages plus attached outside records (Zoetis senior panel, a Petco/Vetco visit, a North Naples Vet Hospital history). Record generated Jul 30 2026.
**Journey anchor date:** Jul 30 2026, a wellness exam with Dr. T. Underhill. Two problems were newly staged that day (`Periodontal disease, AVDC stage 3`, `mature cataracts OU`), the owner then texted asking how to book the dental, and a technician visit for pre-anaesthetic blood work was booked for **Sept 28 2026**. The live thread is getting Pobble from that wellness visit, through the Sept 28 blood draw, to a dental under anaesthesia.

## How to read this file

Every span is copied straight from the source. The number is the line it sits on. Multi-line spans get a range. We assume Petfolk's string match normalises whitespace (`ground-rules.md`, assumption 1). `verify_quotes.py` checks the built HTML against the source.

**Note the source has a 40-page duplication artifact** (a single fecal result table repeated over pages 57 to 82, lines ~2560 to 4216). It contains nothing. The real record is pages 1 to 56 and 83 to 104.

**Aaliyan's verification job:** open `records/z2_MRS.txt`, go to the line number, confirm the span is character exact and means what the journey uses it for. This record has five live threads and two soft findings, so section 8 (data issues) and section 10 (unknowns) are longer than usual.

---

## 1. Identity and household

| Span | Line | Note |
|---|---|---|
| `Pobble \| 8.3 YO \| Male (Neutered) \| Chihuahua \|` | 21 | wraps to `10.6 lb` on L22. About 8 years old, small breed. |
| `Patient ID: PT-306BA7 \| Canine` | 23 | key on this |
| `Currently a Member` | 256, 2065, 4234 | PetfolkCare member at the recent visits |
| `Not Yet a Member` | 4716 | at the first visit, Sep 16 2024. Joined shortly after. |
| `No - no microchip found, owner declines` | 309 | no microchip, owner has declined it |
| `He was feral for the first year of his life.` | 1085 | rescue, feral origin. Also `feral prior to us adopting him` (L4701). This is the root of the anxiety. |
| `We just lost our other dog a month ago and a week ago we moved to the area.` | 4698 | the Sep 2024 stress stack: a death and a move together |
| `I will see you soon with Sindri!` | 1035 | the other dog in the household is **Sindri**, also a Petfolk patient. Loose match. |
| `The other dog is now on medication and` | 271 | wraps to `doing well.` L272. Sindri is medicated and stable. |

Household history, for context (not all single-quote clean): the family moved more than once (`The family moved from South Carolina a few months ago (June).` L1125-1126, versus `recently moved from South FL` L4742 and prior records from Naples FL, see §8). The other dog died around Aug 2024. A new dog, Sindri, was brought in around Oct 2024 partly to help Pobble (`O is getting new dog and feels it will help Pobble anxiety`, L2522).

## 2. Anxiety (the spine of this record)

Problem list: `Anxiety - Sep 16, 2024` (L475). Present at every visit. `Nervous and resists meeting new people` is the standing intake descriptor (L251 and many). FAS ranges 1 to 2 across visits.

| Span | Line | Use |
|---|---|---|
| `The client reports that Pobble is a "really nervous dog."` | 287 | the owner's framing at the Jul 30 2026 visit |
| `he destroyed a wall and removed the` | 4747 | wraps to `paint.` L4748. Separation distress at the first visit. Loose. |
| `FAS 2 (0-5)` then `1, nervous but sweet` | 422, 466 | the Jul 30 2026 fear score and assessment |

### The serotonin-syndrome history (critical)

At the **first visit, Sep 16 2024**, Pobble was prescribed **both** Trazodone 50mg (0.5 tab q12h, L4999-5000) **and** Fluoxetine 10mg (0.5 tab daily, L5012-5013) at the same time.

| Span | Line | Use |
|---|---|---|
| `He has` `had previous adverse reactions to anxiety medications (fluoxetine and trazodone), which were` `administered concurrently.` | 1084-1087 | the recap, from the Aug 2025 visit. Loose. |
| `high suspicion of serotonin syndrome from concurrent` `administration.` | 1314-1315 | the working explanation. Loose. |
| `Discontinue fluoxetine and continue monitoring for signs of serotonin syndrome` | 4461 | the Sep 24 2024 plan, after Pobble presented panting, shaking, vomiting, unable to settle |
| `P is doing much better on only Gaba. O is getting new dog and feels it will help Pobble anxiety` | 2522 | Oct 2024, owner declined a Trazodone refill, Pobble stable on gabapentin alone |
| `the plan is to consider restarting fluoxetine as a monotherapy` | 1332 | Aug 2025, gated on a normal urinalysis. The UA came back normal and fluoxetine was restarted (Dr. T. Underhill, Aug 24 2025). |

Fluoxetine was refilled again **Dec 12 2025** (#60, 3 refills through Dec 2026, L108-113). See §8 E for why its current status is unclear.

## 3. Atopy

Problem list: `Atopy - Jan 28, 2025` (L477).

| Span | Line | Use |
|---|---|---|
| `The owner is interested in the Cytopoint injection at` `this time.` | 4283-4284 | Dec 31 2024, owner chose Cytopoint over Apoquel |
| `Atopy, pruritic- no response to Cytopoint` | 1739 | Jan 24 2025 recheck, Cytopoint failed |
| `Discussed switching from Cytopoint to Apoquel.` | 1747 | Jan 24 2025, switched to Apoquel BID then SID, plus a medicated mousse and a prednisone taper |

After Jan 2025 the record has **no further atopy mention**. The Jul 30 2026 skin exam is normal (`skin and coat appear healthy, no ectoparasites`, L451). The Apoquel prescription (Jan 24 2025, 2 refills through Jan 2026, L140-143) has lapsed. The Jul 30 2026 intake says `no meds, just simparica trio` (L249). So the atopy is currently quiet and Pobble appears to be off allergy medication, though the record does not confirm this. The oldest outside record (2023) lists `Seasonal Allergies` (L5757), and the 2025 flare was a January one, so a seasonal pattern is plausible.

## 4. Periodontal disease, AVDC stage 3 (the live thread)

Problem list: `Periodontal disease, AVDC stage 3 - Jul 30, 2026` (L478). Dental score progression: 1 (Sep 2024, Dec 2024, Jan 2025) to 2 (Aug 2025) to `Dental Score 3 (0-4)` (L424, Jul 30 2026).

| Span | Line | Use |
|---|---|---|
| `moderate to heavy dental calculus and gingivitis` | 440 | the Jul 30 2026 oral exam |
| `I recommend a professional dental cleaning within the next 1-2 months for him.` | 597 | the recommendation |
| `I` `will email you a dental estimate.` | 597-598 | an estimate was promised. Loose. |
| `please schedule` `an appointment for his pre-op bloodwork first.` | 598-599 | the sequence: bloodwork clears anaesthesia, then the dental books |
| `blood work should be completed 1` | 213 | wraps to `2 weeks prior to the dental procedure` and `is typically valid for 30 days.` (L213-215). The timing window. |
| `Pobble scheduled for a technician visit on Monday, September 28th at 8:30 AM at our [NAME] location` | 232 | wraps to `for his pre-anesthetic blood work.` L233. The booked appointment. |
| `PABW for COHAT` | 235, 237, and many | the follow-up label. PABW = pre-anaesthetic blood work, COHAT = comprehensive oral health assessment and treatment. |

**The Sept 28 blood draw is the pivot of the whole journey.** It clears anaesthesia for the dental and it finally produces fresh labs after two years of declines (§7).

## 5. The cardiac question (a soft finding, not on the problem list)

| Span | Line | Use |
|---|---|---|
| `Heart murmur and heart arrythmia!` | 4911 | Sep 16 2024 exam |
| `Difficult to assess murmur due to arrhythmia and` `constant shaking.` | 4419-4420 | Sep 24 2024 exam. Both times the finding was confounded by extreme tremor, and the second time by an active drug reaction. |
| `there had been indications of a heart murmur in the past but I reviewed medical records and` `nothing was noted` | 4941-4942 | the vet could not corroborate it historically |
| `a cardiology referral, ECG, echocardiogram` | 4944 | what was floated. The line reads `At some point, Pobble would [NAME] from a cardiology referral, ECG, echocardiogram` (L4944), the `[NAME]` is a pseudonymiser gap for `benefit`. |
| `Recommend dental prophylaxis & cardiac workup due to murmur heard today and his history of HW disease` | 4960 | the Sep 2024 plan tied the cardiac workup to the dental and to the heartworm history |
| `Normal rate and rhythm. No murmurs or arrhythmias auscultated, pulses strong and synchronous.` | 444 | **the Jul 30 2026 exam, when Pobble was calmer, found the heart normal** |

So: a murmur and arrhythmia were noted twice in Sep 2024 under extreme stress and a drug reaction, never confirmed since, and the most recent exam was normal. The journey does not assert Pobble has heart disease. It flags the record's own open recommendation as something for the DVM to weigh at the pre-anaesthetic stage, since it bears on anaesthesia safety.

## 6. Heartworm history

| Span | Line | Use |
|---|---|---|
| `Heart worm positive in the past - Sep 16, 2024` | 476 | problem-list entry |
| `hx of HW dz prior to adoption` | 4749 | before the current owner had him |

Every heartworm test on record since is negative: Flex4 negative x4 (Sep 2024, L4976-4979), and `Heartworm antigen test: Negative.` at the Jul 30 2026 visit (L483). He is on Simparica Trio year-round. The relevance is that a past-HW-positive dog with possible cardiac changes is exactly the profile where a pre-anaesthetic cardiac look is reasonable.

## 7. Senior bloodwork, the recurring decline

A full senior panel **was** run once, Sep 16 to 17 2024 (Zoetis, attached L5186 onward). Findings:

| Span | Line | Meaning |
|---|---|---|
| `ALT` `155` `U/L` `HIGH` `17 - 115` | 5292-5296 | mildly elevated liver enzyme |
| `AST` `133` `U/L` `HIGH` `11 - 46` | 5297-5301 | mildly elevated liver enzyme |
| `TT4 concentrations => 2.0 µg/dL make hypothyroidism highly unlikely.` | 5380 | T4 was 2.5, so not hypothyroid |

Creatinine, BUN, SDMA, cholesterol, glucose and CBC were all normal. The follow-up:

| Span | Line | Use |
|---|---|---|
| `a very minor elevation in his liver enzymes that could be strictly due to aging` | 4656 | the vet's SMS read on the result |
| `start him on a liver protectant called Denamarin once daily 1 hour before` `breakfast then recheck a liver panel in 1 month` | 4656-4657 | Denamarin and a recheck were offered. No record either happened. Loose. |

Since then, senior bloodwork has been **declined or deferred every time**:

| Span | Line | When |
|---|---|---|
| `recommended to` `postpone the blood draw for these tests until an effective anxiety management plan is in place to` `make the visit less stressful for Pobble.` | 1341-1343 | Aug 2025. The vet's own reason for the delay. |
| `Recommended wellness blood work was declined by the client.` | 489 | Jul 30 2026 |
| `Recommended fecal testing was deferred by the client to a future visit.` | 490 | Jul 30 2026 |
| `Recommended urinalysis was deferred by the client.` | 491 | Jul 30 2026 |

**The Sept 28 PABW breaks this logjam.** It is bloodwork the owner has already agreed to, and it will show whether the 2-year-old liver enzyme elevation has resolved or progressed.

## 8. Data issues caught, and what we decided

**A. Breed written three ways.** `Chihuahua` (Petfolk header and footers), `Chihuahua - Mixed` (Petco, L5603), `Rat Terrier` (one North Naples historical record, L5741).
**Decision:** use `Chihuahua`. The journey does not hinge on breed. Noted in the footer.

**B. Where the family moved from.** `South Carolina` in the Aug 2025 note (L1125), `South FL` and Naples FL elsewhere (L4742, outside records). Possibly two separate moves, possibly a transcription error.
**Decision:** the journey does not need the origin. It needs the pattern: multiple moves plus the loss of the other dog plus a new dog, a documented stress stack behind the anxiety and the behavioural urination. Noted.

**C. Pet name bleed.** `Toby` is used for Pobble in the Sep 2024 intake free text (`Toby who was already a very nervous rescue`, L4700). Attachment titles read `Pobble Bodhi` (client surname appended).
**Decision:** no personal or alternate name is quoted in the journey. Keyed on Patient ID `PT-306BA7`. Client name `Bodhi Skarn` is consistent throughout this record, unlike Ikko3 and Quorra.

**D. Staff-name bleed into fixed fields.** `Color: Reevo Vanhorn` (L24), `Skin/Coat/Blake Ziegler` (L5637). Standard pseudonymiser artifact, no colour is quoted.

**E. Fluoxetine status is unclear, and it matters.** The medication list shows fluoxetine active (refilled Dec 12 2025, 3 refills through Dec 2026). The Jul 30 2026 intake says `no meds, just simparica trio` (L249). FAS that day was 2.
**Decision:** the journey does not assume Pobble is on or off fluoxetine. It surfaces the question, because the vet's own plan ties the stressful blood draw to `an effective anxiety management plan is in place` (L1341-1343), and the PABW is now booked for Sept 28. If Pobble is off his anxiety medication, that is a conversation to have before the blood draw, not after. This is the single most important branch in the journey. Logged as a decision.

**F. The cardiac finding is soft and confounded.** Heard twice in Sep 2024 during extreme tremor and a drug reaction, never confirmed, `Cardiovascular: Normal` on Jul 30 2026.
**Decision:** the journey does not state Pobble has heart disease. It notes the record's own open recommendation (`cardiac workup due to murmur heard today and his history of HW disease`, L4960) as a question for the DVM at the pre-anaesthetic stage. Vet-led, not message-driven.

**G. Weight trend.** 12.8 lb (Sep 2024) to 11.6 (Jan and Aug 2025) to 10.6 (Jul 2026). BCS went from 4 to 5 (ideal) over the same period.
**Decision:** low stakes on its own. He was underweight from not eating during the 2024 anxiety crisis and is now at ideal weight. But a senior who has lost about 2 lb over two years, with an un-worked-up polydipsia flag from Aug 2025 and two-year-old labs, is a good reason for the PABW to be a full panel, not just a pre-anaesthetic minimum. Noted.

## 9. Vaccines and preventives

| Span | Line | Use |
|---|---|---|
| `Bordetella vaccine administered.` | 485 | given Jul 30 2026, next due Jul 30 2027 |
| `his Rabies and Distemper/Parvo vaccines are current` | 604 | historical, dated Mar 30 2024, current until `03/30/2027` (L494) |
| `The Leptospirosis vaccine was not administered.` | 492 | lepto declined again Jul 30 2026, has never been given |

On Jul 30 2026 the owner declined the rabies and DA2LPP boosters that were *offered* as coming due (intake reason `prev care- offer vaccines coming due as well`, L244). Nothing is actually overdue. Rabies and DAPP fall due `03/30/2027`, inside the journey window. No "overdue" touch fires off this export (consistent with the Ikko and Ikko3 calls).

Fecal testing has been deferred repeatedly (Sep 2024, Aug 2025, Jul 2026), each time with the owner saying they will bring a sample.

## 10. Unknowns the journey has to branch on

- **Is Pobble currently on fluoxetine?** (§8 E) Drives whether the anxiety is "managed" ahead of the Sept 28 blood draw.
- **Will the owner keep the Sept 28 PABW appointment?** The record shows two prior cancellations (`Sent SMS regarding cancellation appt`, L1507 and L1877). This appointment is load-bearing for the whole dental thread.
- **The PABW results.** Whether the 2-year-old ALT and AST elevation has resolved or progressed. Drives anaesthesia clearance and whether the dental proceeds on schedule.
- **The cardiac question.** Does the DVM want an ECG or echo before clearing anaesthesia.
- **The dental estimate.** Promised, not yet in the record. A COHAT with stage 3 periodontal disease and likely extractions is a four-figure estimate that could stall.
- **Cataract surgery referral.** Offered (`refer him to Animal Eye Care`, L601), owner's call, not pursued in the record.
- **Atopy.** Currently quiet, off medication. Whether it flares again, and whether seasonally (the 2025 flare was January).
- **Fecal.** Perpetually deferred.
- **The polydipsia flag** from Aug 2025 (`possible increase in thirst`). Never worked up because the labs were never done.

## 11. Data we would ask Vetspire for

- **Current medication status with a real active/inactive flag.** The fluoxetine ambiguity is the clearest example in the whole corpus of why a text export is not enough.
- Appointment Booked, Completed and **Cancelled** events, so the journey can react to the Sept 28 PABW and to a cancellation the way the record shows this owner has cancelled before.
- Estimate Issued for the dental, so the agent follow-up only fires if it stalls.
- Lab Result events for the PABW, to gate the COHAT scheduling on a real clearance.
- FAS as a coded field over time.
- Problem-list entries with a status, so `Atopy` reads as monitoring, not active.
- Weight as a series, so the two-year downward trend is a computed fact.
- Referral Made events (Animal Eye Care).
- Household links. Sindri is in the same home, is a Petfolk patient, had urinary issues, and is `now on medication`. The two dogs' behaviour problems are entangled.
