# Evidence file: Ikko3

**Source:** `records/z2_16MRS-16.txt` · **doc_id:** `z2:16MRS-16` · 58 pages of Petfolk records plus a 23 page attached history from a prior clinic. Record generated Jul 30 2026.
**Journey anchor date:** Jul 21 2026, the virtual care call about possible weight loss after the new puppy. An in person weight check was booked off that call for "Friday at 12:00 PM" (about Jul 24), and the record ends before that exam happens. So the record's "now" is late July 2026: a cat one month into living with a puppy, an imminent weight recheck, and rabies coming due in November.

## How to read this file

Every span below is copied straight from the source. The number is the line it sits on.

**The source wraps sentences across physical lines.** We assume Petfolk's string match normalises whitespace (`ground-rules.md`, assumption 1), so a quote may span a line wrap as long as the words are contiguous in the source. A span that crosses a wrap is given a line range like `L412-413`. Where a clean single line span exists we prefer it. `verify_quotes.py` checks both the raw form and the whitespace normalised form.

**Aaliyan's verification job:** open `records/z2_16MRS-16.txt`, go to the line number, confirm the span is character exact (allowing the wrap) and means what the journey uses it for. Pay attention to section 13, the pseudonymiser name bleed is worse in this record than in Ikko's.

---

## 1. Identity and signalment

| Span | Line | Note |
|---|---|---|
| `Ikko3 \| 2.6 YO \| Female (Spayed) \| Persian Mix` | 20 | signalment line, wraps to `\| 8.57 lb` on L21 |
| `Patient ID: PT-E3BF8D \| Feline` | 22 | |
| `a domestic longhair cat` | 1962 | the vet's own description at the Jul 2025 visit. Long coat is the mechanical driver of the hairball problem. |
| `The patient has long hair, which contributes to` | 754 | wraps to `hairballs.` on L755. Use `The patient has long hair, which contributes to hairballs.` |
| `Persian Mix` | many footer lines | breed, clean on the `Client: ... Breed:` footers |

Header weight `8.57 lb` (L21). Exam weights 7.84 to 8.57 across the record (section 9).

## 2. Household, membership, logistics

| Span | Line | Use |
|---|---|---|
| `Currently a Member` | 365, 1067, 1511, 1957 | PetfolkCare member at every recent visit |
| `Not Yet a Member` | 2320 | at the Nov 22 2024 visit. She joined between then and Nov 2025. |
| `Do you have Pet Insurance for Ikko3?` then `No` | 366-367 | not insured |
| `Ikko3 is an indoor-only cat.` | 411 | single line, the Jun 2026 wellness intake |
| `Indoor cat in an apartment building. No other` | 1568 | wraps to `pets in the household.` on L1569. This is the Nov 2025 note, before the puppy. Use `Indoor cat in an apartment building.` as the clean span. |
| `Purina dry and occasional wet food` | 355 | current diet, owner's words |
| `The client sometimes offers wet food on a spoon.` | 402 | single line. Relevant for how a Laxatone or lactulose dose gets delivered. |

## 3. Problem list (verbatim, each on its own line)

Appears identically many times (L333-339, L534-541, L672-679, L873-880, L1266-1274, L1691-1699, L2098-2105, L2465-2472).

| Span | Line |
|---|---|
| `Healthy animal - Nov 24, 2024` | 333 |
| `Acute vomiting - Dec 02, 2025` | 334 |
| `Ddx hairballs and gastritis vs FB vs primary GI (IBD flare up) > metabolic` | 335 |
| `Pica - Dec 02, 2025` | 336 |
| `Likes chewing on plants and xmas decorations` | 337 |
| `chronic intermittent loose stools - Dec 02, 2025` | 338 |
| `Dental plaque formation - Nov 11, 2025` | 339 |

## 4. Pica and foreign body (the acute-risk track)

The through line of this cat's chart. Two events on record plus a standing behaviour.

| Span | Line | Use |
|---|---|---|
| `Pica - Dec 02, 2025` | 336 | problem-list entry |
| `Likes chewing on plants and xmas decorations` | 337 | problem-list entry, the behaviour in the clinic's own words |
| `P swallowed Mylar string.` | 1946 | reason for visit, Jul 29 2025 |
| `The owner witnessed her playing with a ribbon from a gift approximately 1.5 hours prior to` | 1963 | wraps to `the visit.` on L1964 |
| `ate a piece mylar/gift wrapping ribbon, about 5 inches worth` | 2261-2263 | the VCC intake wording. Multi-line, loose match. Source reads `ate a / piece mylar/gift wrapping ribbon, about 5 inches / worth`. |
| `Emesis was induced, but the suspected foreign material was not recovered.` | 2096 | single line, the outcome of the ribbon visit |
| `While` ... `radiographs showed material in the stomach, there were no definitive signs of a foreign body or obstruction.` | 2094-2095 | clean sub-span: `radiographs showed material in the stomach, there were no definitive signs of a foreign body or obstruction.` |
| `A detailed discussion was had regarding the risks of linear foreign bodies, including the potential for them` | 2108-2109 | wraps to `to anchor and cause the intestines to bunch up (plication), which is a surgical emergency.` on L2109-2110. Long multi-line quote, loose match. Sentence starts with capital `A` at the start of L2108. |
| `The owner was explicitly warned NOT to pull on a string if it is ever seen protruding from the rectum` | 2138 | single line (continues `, as this ...`). The single most important safety line in the record. |
| `It was recommended to remove` | 2140-2141 | wraps to `access to all linear items, including ribbons, strings, hair ties, and wand toys (unless under direct supervision).` on L2141. Loose match. |
| `The patient has a history of pica, having been` | 723-724 | wraps to `seen ingesting Christmas garland and pieces / of a fake plant.` L724-725. Loose. Also appears verbatim in the radiologist's case history at L2577-2578. |
| `The owner has observed these` | 725-726 | wraps to `items passing in her stool previously.` L726. Loose. |
| `chewing on plastic garland` | 1412 | single line, the Dec 2 2025 crisis call |
| `History of foreign body ingestion (ribbon) approximately 3 months prior.` | 1542 | single line, the Nov 2025 history summary |
| `The owner reports playing with wand toys with` | 1980 | wraps to `Ikko3.` L1981. Wand toys are a linear-item exposure. |

## 5. Vomiting and hairballs

| Span | Line | Use |
|---|---|---|
| `Acute vomiting - Dec 02, 2025` | 334 | problem-list entry |
| `Vomits approximately 2 times per week, which` | 1549-1551 | wraps to `is reported as a chronic issue consistent with / hairballs.` Loose. The baseline rate. |
| `Ikko3 typically` `about once a week, but the` | 1380 | `[NAME]` gap in the middle (`vomits`). Weak as a quote, use section context instead. |
| `she vomited about 5 times within an hour` | 1307 | single line, the discharge summary of the Dec 2025 crisis |
| `approximately 5 episodes of vomiting` | 1095-1096 | wraps to `within a 1-hour timeframe today.` L1096. Loose. |
| `Recommended starting Laxatone to help manage hairballs by lubricating the gastrointestinal tract.` | 1278 | single line, the plan |
| `Give 0.5 to 1 teaspoon initially to help clear any existing accumulation.` | 1280 | single line, the dosing |
| `place a small dab on her paw, which` | 628-629 | wraps to `encourages her to lick it off.` L629. Loose. The delivery trick for a cat that won't take meds. |
| `Please be mindful that giving too much can cause diarrhea.` | 629 | single line, the caution |
| `Discussed using a slow-feeder bowl to prevent rapid food ingestion, as this can trigger a vomiting` | 1286-1287 | wraps to `reflex.` L1287. Loose. |
| `Continue using her slow-feeder bowl to prevent her from eating too quickly, as this can sometimes` | 1336-1337 | wraps to `trigger vomiting.` L1337. Loose. Confirms she already has the bowl. |
| `REC getting a water fountain to encourage drinking more` | 892-893 | wraps to `often.` L893. Loose. |

## 6. Chronic intermittent loose stools

| Span | Line | Use |
|---|---|---|
| `chronic intermittent loose stools - Dec 02, 2025` | 338 | problem-list entry |
| `The owner reports a chronic history of` | 749-750 | wraps to `intermittent loose stools` L750. Loose. |
| `Diarrhea: The owner reports a chronic history of intermittent loose stools throughout Ikko3` | 749-751 | the radiologist case history repeats this at L2583-2584 as `throughout Ikko3 life, which is / not an acute change.` |
| `having to trim matted fur` | 1124-1126 | wraps to `from the perineal area due to episodes of loose / stool.` L1125-1126. Loose. The visible consequence at home. |
| `Underlying intestinal disease like IBD possible.` | 1265 | single line, the vet's differential |
| `this is something that we can discuss in more detail at a future` | 1350-1351 | wraps to `visit` L1351. Loose. The clinic itself flagged this as unfinished business. The line starts `Regarding Ikko3 chronic loose [NAME], this is something ...` at L1350. |

## 7. Dental and the deferred bloodwork

| Span | Line | Use |
|---|---|---|
| `Dental plaque formation - Nov 11, 2025` | 339 | problem-list entry |
| `Grade 1/4 dental tartar.` | 501 | single line, Jun 2026 oral exam |
| `Mild tartar buildup noted on the upper left teeth.` | 1656 | single line, Nov 2025 |
| `Discussed products to help reduce tartar accumulation, including dental diets and treats.` | 1724 | single line |
| `We recommend looking into products from the Veterinary Oral Health Council (VOHC) to` | 1911-1912 | wraps to `help manage tartar at home.` L1912. Loose. |
| `This can include special diets, treats, or water additives.` | 1912 | single line |
| `Recommended routine wellness lab work` `deferred until a future anesthetic procedure, such as a` | 551 | en-dash after `work`. Clean sub-span: `deferred until a future anesthetic procedure, such as a` wraps to `dental cleaning, provided the patient remains asymptomatic.` L551-552. |
| `Annual blood work was discussed and declined for today.` | 1712 | single line, Nov 2025 |
| `The owner may pursue this at a future visit.` | 1712 | single line, same block |

The dental cleaning is the pivot point. It is the event that would also clear the deferred bloodwork, and it needs anaesthesia, which needs the FAS problem handled first. One touch, three problems.

## 8. FAS and handling

FAS trend across the record: `FAS 0` Jul 2025 (L2044), `FAS 3` Nov 2025 (L1635, L1684), `FAS 1` Dec 2025 (L817, L1208), `FAS 1` Nov 2024 (L2415). The bad day was the Nov 2025 wellness visit.

| Span | Line | Use |
|---|---|---|
| `Scared and typically does not cooperate` | 360 | the Jun 2026 intake FAS descriptor |
| `FAS 3: The patient became very fearful, anxious, and aggressive during the examination. Shivering was` | 1684 | wraps to `noted.` L1685. The peak episode. Clean sub-span: `The patient became very fearful, anxious, and aggressive during the examination.` |
| `She refused treats. She became aggressive after smelling the Churu treat.` | 1685 | single line |
| `Patient is resistant to being brushed on her belly and back legs.` | 1562 | single line. Grooming at home is also a stress point. |
| `Gabapentin 100mg: Dispensed for pre-visit sedation.` | 1717 | single line, the plan. Note the `100mg` is part of the usable span; `Gabapentin: Dispensed for pre-visit sedation.` is NOT in the text. |
| `The client reports difficulty administering this medication, which was prescribed for travel,` | 406 | wraps to `as Ikko3 [NAME] it in her treats and refuses to consume it.` L407. The `[NAME]` is a pseudonymiser gap (`smells` or `finds`). Clean spans: `The client reports difficulty administering this medication, which was prescribed for travel,` and `as Ikko3` ... `it in her treats and refuses to consume it.` |
| `For future visits, pre-medication with gabapentin is strongly recommended. The owner may also` | 1732-1733 | wraps to `bring preferred treats from home.` L1733. Loose. |

So: the vet wants her pre-medicated, the drug is on the shelf, and the owner cannot get it into her. That gap is the thing a journey touch has to close.

## 9. Weight and the puppy weight-loss concern

| Span | Line | Use |
|---|---|---|
| `Weight 8.0 lb` | 2043 | Jul 2025 |
| `Weight 8.15 lb` | 1634 | Nov 2025 |
| `Weight 7.84 lb` | 814, 1204 | Dec 2025, during the GI illness. `Body Condition Score: 4` at L824 (down from 5). |
| `Weight 8.57 lb` | 478 | Jun 2026 |
| `Weight 8.26 lb` | 2414 | Nov 2024 |
| `Body Condition Score: 5` | 487, 1213, 2051, 2420 | her normal |
| `Her weight was 8.7 pounds, which is a healthy` | 618-619 | wraps to `weight for her.` L619. The Jun 2026 discharge. |
| `a new puppy was introduced into the home approximately one month ago.` | 127 | single line, the Jul 21 2026 call |
| `Advised that cats may take several months to adjust` | 156-157 | wraps to `to a new pet in the home and that subtle weight / changes should still be evaluated, as cats can hide / signs of illness.` L157-159. Loose. |
| `Recommended an examination to` | 159-160 | wraps to `assess the reported possible weight loss.` L160. Loose. |
| `Ikko3 scheduled for an appointment at the Sandy` | 166-167 | wraps to `Dr. S. Thistlewood location on Friday at 12:00 PM for evaluation of possible weight loss.` L166-167. Loose. The clean tail `on Friday at 12:00 PM for evaluation of possible weight loss.` is single line at L167. |

The weight number the owner quotes on that call (`around 8 pounds`) is attributed in the source to a bled-in name, see section 13. The real exam weights above are what the journey should lean on.

## 10. Fleas, preventives, and the puppy flea risk

| Span | Line | Use |
|---|---|---|
| `Revolution Plus for Cats 5.6 to 11 Pounds, Orange Label` | 79, 445, 580, and many | current parasite prevention, dispensed 6 month supply Jun 2026 |
| `The client will be temporarily caring for an 8-week-old` | 412-413 | wraps to `Golden Retriever puppy. The potential for interactions and the risk of flea transmission were discussed.` L413. |
| `The potential for interactions and the risk of flea transmission were discussed.` | 413 | single line |
| `The risk of flea transmission` | 568-569 | wraps to `was highlighted as the primary health concern.` L569. Loose. |
| `The main health risk between them would be fleas, which the Revolution Plus will cover for Ikko3.` | 630 | single line, the discharge |
| `Advised supervising interactions to prevent chasing and to monitor for any signs of aggression.` | 568 | single line |
| `We recommend supervising` | 630-631 | wraps to `their interactions closely, especially at first.` L631. Loose. |
| `Make sure the puppy doesn't chase or overwhelm Ikko3,` | 631 | single line, straight apostrophe in source |
| `give them separate spaces to retreat to.` | 632 | single line |
| `This will help ensure a safe and positive introduction for` | 632 | wraps to `both of them.` L633 |
| `Continue` `monthly for a minimum of 3 months to break the flea life cycle.` | 1336 | Nov 2025. Clean tail: `monthly for a minimum of 3 months to break the flea life cycle.` wraps L1336. |
| `Recommended using a flea comb for monitoring instead of bathing to reduce stress.` | 1730 | single line. Ties flea care back to the FAS problem, no bathing. |

Deworming history: Drontal dispensed Nov 2025 (`$46`), owner could not administer it (`could not administer Drontal and it went to waste`, L1453), replaced with Profender topical Nov 2025. Another "can't pill the cat" data point.

## 11. Vaccines and forward bookings

| Span | Line | Use |
|---|---|---|
| `The FVRCP vaccine is current until 2028.` | 394 | single line |
| `The Rabies vaccine is due in November 2026.` | 395 | single line |
| `Advised that the patient is due for her Rabies vaccine in November 2026.` | 576 | single line, the discharge |
| `Administered the Feline Leukemia (FeLV) vaccine booster.` | 555 | single line, Jun 2026. Next due `Jun 19, 2027` (L50, L609). |
| `Nov 11, 2026` | 61, 1848 | rabies next due date on the immunization table (given Nov 11 2025, PureVax 1 yr) |
| `FORWARD OndiKED ROUTINE WELLNESS` | 173 | forward-booked routine wellness. `OndiKED` is a pseudonymiser artifact for `BOOKED`. |
| `Nov 23, 2026 \| 8:00 am` | 172 | the forward-booked routine wellness date |
| `Dr. L. Marchetti rabies vx reminder` | 174 | forward-booked rabies reminder |
| `Aug 01, 2026 \| 8:30 am` | 175 | the rabies reminder / wellness date |

Note the two different rabies "due" signals: text says `November 2026` (L395, L576), the immunization table says `Nov 11, 2026` (L61), and there is a booked reminder for `Aug 01, 2026`. See section 13 D.

## 12. Transitional vertebra (incidental, do not build a track on it)

| Span | Line | Use |
|---|---|---|
| `Transitional S1 vertebra` | 2622 | the radiologist's conclusion, Dec 2025 |
| `is called transitional vertebrae and is a congenital abnormality but should not create any` | 667-668 | wraps to `issues.` L668. Loose. The staff explanation to the owner. |
| `The S1 vertebra is transitional, with a persistent intervertebral disc between S1 and S2.` | 2616 | the full radiology line |

This is a benign incidental finding. It gets one honest line in the "what we are not doing" part of the footer, nothing more. It is here so a reviewer sees we read the radiology report and chose not to act on it.

## 13. Data issues caught, and what we decided

**A. Client name is not reliable and bleeds into the notes.** The client is `Guthrie Pellow` on the header (L14) but `Guthrie Emery Yancey` throughout the attached prior-clinic history (L2635, L3027, L3298). `Emery Yancey` is also a Petfolk LVT who signs notes in this same file (L1025, L1034). The pet is repeatedly written as `Ikko3 Emery Yancey` (L378, L2185, L2535, L2575). The staff first name has been pasted onto the pet as a surname.
**Decision:** never quote a personal name as a pet fact. Journey copy addresses the owner generically. We key on the patient ID `PT-E3BF8D`, not the client name (rule 11). Logged in the footer as a caught issue.

**B. A second pet name, "Stormy", is used for Ikko3 in the Jul 21 2026 call.** That note reads `Stormy's normal weight is around 8 pounds`, `Reviewed Stormy's history`, `bring Stormy in` (L128, L153, L164), all clearly about Ikko3, in the same paragraph that names Ikko3 directly. Same artifact class as A: a wrong name substituted by the pseudonymiser.
**Decision:** we do not quote `Stormy` or the `around 8 pounds` figure attributed to that name. The weight story in the journey uses the dated exam weights in section 9, which are unambiguous. Logged in the footer.

**C. Two clinic locations.** Most visits are at `Sandy Dr. S. Thistlewood`. The Jul 29 2025 ribbon visit is at `PETFOLK - EAST COBB MARIETTA` (L1943).
**Decision:** treat the Sandy location as home clinic (it is the site of every 2026 encounter and both forward bookings). No action needed, noted so a reviewer knows we saw it.

**D. Rabies due date has three forms.** Free text says `due in November 2026` (L395, L576). The immunization table says `Nov 11, 2026` (L61). There is a booked staff reminder for `Aug 01, 2026` (L175) and a routine wellness for `Nov 23, 2026` (L172).
**Decision:** consistent with the Ikko call (`ground-rules.md` rule 5), we do not fire a "rabies overdue" message off the text export. The vaccine reminder touch runs off a structured Vetspire feed with a real `next_due_date` field and the booked-appointment events, which we list in section 15. The journey can safely reference the *booked* Aug 1 and Nov 23 appointments because those are explicit appointment records, not inferred dates.

**E. Owner age of pet drifts.** Header `2.6 YO` (L20). Dec 2025 notes say `1-year 11-month-old` (L718, L1094). Radiology report says `Age 1yr` (L2589). DOB is given as both `[MON] [DAY], 2024` (L23) and `1/1/2024` (L2658).
**Decision:** low stakes. Journey never states an age. Use `2.6 YO` only if a signalment chip is needed, matching the Biscuit format which quotes the header line verbatim.

## 14. Unknowns the journey has to branch on

- **The Jul 24 weight recheck outcome.** Did she actually lose weight, is it the puppy stress or something medical. The record ends before this exam. The journey's weight track has to branch on the exam result.
- **Whether the pica is currently active.** No FB event since Dec 2025, but the behaviour is a standing problem. The acute-risk track is a permanent low-cost safety net, not a timed campaign.
- **Whether the owner ever gets gabapentin into her.** Everything downstream (dental cleaning, therefore the deferred bloodwork) waits on this.
- **Puppy status.** "Temporarily caring for" (L412). If the puppy leaves, the flea-risk and stress framing changes. The journey should not assume the puppy is permanent.
- **Loose-stool workup.** The clinic said "discuss at a future visit" (L1350-1351) and never did. Is the owner interested in pursuing it.

## 15. Data we would ask Vetspire for

- Structured vaccine records with a `current` flag and a queryable `next_due_date`, so the three rabies date forms in section 13 D resolve to one.
- Appointment Booked and Appointment Completed events, so the journey can react to the Jul 24 recheck, the Aug 1 rabies visit, and the Nov 23 wellness rather than guessing from text.
- Weight history as a series, so "lighter than her Jun exam" is a computed fact, not a quote from a bled-in name.
- BCS and FAS as coded fields over time, not free text, so the 0 to 3 to 1 FAS trend is machine readable.
- Medication dispensed vs medication filled vs refill requested, so "dispensed gabapentin, never successfully given" is detectable.
- Household links, to confirm the puppy is in the same home and whether it is a Petfolk patient (flea-prevention cross-sell, coordinated visit).
- Problem-list entries with a status (active, resolved, monitoring), so "chronic loose stools, never worked up" surfaces on its own.
- Message engagement (opens, clicks, replies) to gate any fallback to a more expensive channel.
