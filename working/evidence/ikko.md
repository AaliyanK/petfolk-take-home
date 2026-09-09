# Evidence file: Ikko

**Source:** `records/z1_MRS-45.txt` · **doc_id:** `z1:MRS-45` · 83 pages, Oct 2025 to Jul 2026.
**Journey anchor date:** Jul 27 2026 (the sedated nail procedure) with the Jul 28 ortho follow-up email one day later. Everything before that is history the journey draws on. The record's "now" is roughly Jul 29 2026, mid crisis.

## How to read this file

Every span below is copied straight from the source. The number is the line it sits on.

**The source wraps sentences across physical lines.** We are assuming Petfolk's string match normalises whitespace (see `ground-rules.md`, assumption 1), so a quote can span a line wrap as long as the words are contiguous in the source. Where a span crosses a wrap, the line range is given as `L218-219`. Where a good single-line span exists we prefer it. The verification script checks both forms.

**Aaliyan's verification job:** open `records/z1_MRS-45.txt`, go to the line number, confirm the span is character exact (allowing the wrap) and means what the journey uses it for.

---

## 1. Identity and signalment

| Span (usable, single line) | Line | Note |
|---|---|---|
| `Ikko \| 7 YO \| Female (Spayed) \| Basset Hound` | 20 | signalment line, wraps to `Mix \| 33 lb` on L21 |
| `Patient ID: PT-F4EC30 \| Canine` | 22 | |
| `Basset Hound Mix` | 243 and many footers | breed, clean on the `Client: ... Breed:` footer lines |

Header weight is `33 lb` (L21). Exam weights range 31.4 to 36 over the record (see section 4).

## 2. Household, membership, insurance, logistics

| Span | Line | Use |
|---|---|---|
| `Currently a Member` | 1135, 1905, 2862 | PetfolkCare member at the Jul and Jun visits |
| `Not Yet a Member` | 3425 | at the Oct 26 2025 visit. She joined between Oct and Nov 2025. |
| `Odie pet insurance` | 1909 | insured. Also `Odie` alone at L3430. |
| `Lives with another dog, Rico.` | 3467 | second dog in the house, also allergic |
| `using Rico’s Trazodone prescription. Cassian` | 1051 | usable span: `using Rico’s Trazodone prescription.` Note the curly apostrophe in the source. |
| `had not previously been prescribed for Ikko. The LVT` | 1075 | usable: `had not previously been prescribed for Ikko.` Context: Trazodone was never formally on Ikko's chart. |
| `the office is approximately an hour away` | 1044 | clinic is far, owner leans on virtual care and pharmacy pickup |
| `requesting email delivery of invoice and discharge notes for Ikko for pet insurance` | 1881 | usable: `requesting email delivery of invoice and discharge notes for Ikko for pet insurance` (check it fits on one line in the file). Owner already asks for claim paperwork. |

## 3. Problem list (verbatim, each on its own line)

| Span | Line |
|---|---|
| `Recessed vulva - Oct 26, 2025` | 240 |
| `Injury of nail - Jun 23, 2026` | 241 |
| `Atopy - Oct 26, 2025` | 244 |
| `Tartar accumulation - Oct 26, 2025` | 245 |
| `Overweight - Oct 26, 2025` | 246 |
| `Chronic, displaced ungual process fracture of the right front fourth digit (P3, D4) - Jul 27, 2026` | 247 |

## 4. The nail (the acute track)

| Span | Line | Use |
|---|---|---|
| `Chronic, displaced ungual process fracture of the right front fourth digit (P3, D4).` | 561 | the diagnosis. Same phrasing as the problem-list entry at L247. |
| `if the toe continues to be painful, amputation of the affected toe would provide the most reliable and definitive resolution` | 218-219 | the ortho recommendation, from the follow-up email |
| `dogs generally adapt extremely well to the loss of a single digit and typically return to normal activity after recovery` | 220-221 | the reassurance line from the same email |
| `These include continuing antibiotics while the current infection resolves, using a soft padded bandage, or placing a splint under the paw` | 223-224 | the conservative options |
| `A decision does not need to be made today` | 653 | usable sub-span, from the discharge |
| `A culture of the discharge from the nail bed was also collected today.` | 905 | single line. Result is pending as the record ends. |
| `strict rest with no jumping, stairs, or walks` | 647 | single-line sub-span |
| `she should be carried outside for elimination` | 647 | single-line sub-span |
| `An E-collar must be worn at all times to prevent licking at the bandage` | 647-648 | the E-collar instruction |
| `return in two days for a recheck and bandage change` | 646 | single-line sub-span (the `[NAME]` before it is a pseudonymiser gap) |
| `Injury of nail - Jun 23, 2026` | 241 | onset date. The nail has been an open problem for over a month. |

Visit sequence for the nail, for the timeline (dates as they appear in the file): first seen `Jun 23, 2026` (L241), recheck `July 2, 2026` (L1431), recheck `July 13, 2026` (L1117), sedated procedure `July 27, 2026` (L311), ortho follow-up email `Jul 28` (L212).

## 5. Weight (the spine track)

| Span (usable) | Line | Use |
|---|---|---|
| `Body Condition Score: 8` | 507, 1351, 1616, 2089 | current BCS |
| `ideal weight ~27lbs` | 1617, 2090 | vet's stated target |
| `6.5-7 - ideal weight ~27lbs` | 3089, 3632 | earlier note, BCS was 6.5 to 7 in Oct/Nov 2025 |
| `Overweight - ideal weight ~27lbs` | 3683 | on the Oct 26 2025 DDx list |
| `Discussed the weight loss plan and the associated health risks of being overweight, including an increased risk for diabetes and ligament tears` | 1420-1421 | the health framing, in the vet's words |
| `Advised reducing her current food volume by a quarter of a cup daily.` | 1421 | single line, the concrete instruction |
| `Discussed that low-sodium green beans can be used as a low-calorie supplement to help with satiety.` | 1422 | single line |
| `Recommended reducing or eliminating high-calorie treats and table scraps, including the cheese used for medication administration.` | 1423-1424 | the treats-and-cheese line. She is on multiple meds hidden in cheese, so this is a real calorie source. |
| `The owner reports giving cheese to help with medication administration.` | 1173 | verify. Confirms the cheese-for-pills habit from the owner's side. |

Exam weights across the record: `Weight 32 lb` (L3624, Oct 2025), `Weight 31.4 lb` (L3081, Nov 2025), `Weight 36 lb` (L2498, Mar 2026), `Weight 35.8 lb` (L2082, Jun 2026), `Weight 35 lb` (L1607, Jul 2), `Weight 33.4 lb` (L500, Jul 27). She gained through the winter, then came back down. Verify each of these line numbers.

## 6. Atopy (a track)

| Span (usable) | Line | Use |
|---|---|---|
| `Ikko is having skin allergies since we moved to NC.` | 3406 | owner's own words, single line, the Oct 26 2025 reason for visit |
| `consistent with a flare-up of environmental allergies, which is common after relocating to a new geographic area` | 3136-3137 | the DDx framing |
| `A secondary bacterial infection is suspected.` | 3137 | single-line sub-span |
| `A known food allergy (chicken) is also part of the history.` | 3137-3138 | the food-allergy note in the DDx |
| `We know she is allergic to chicken.` | 3412-3413 | owner's phrasing |
| `Recently relocated to North Carolina from the Poconos, with exposure to new grass and plants.` | 3468-3469 | the move and the trigger |
| `Please give 1 tablet by mouth every 12 hours for two weeks. Then 1 tablet by mouth once every 24 hours to relieve itching long term.` | 2787-2788 | the Apoquel sig |
| `DO NOT skip doses, itching will return.` | 2788 | single line, the adherence hook |
| `Cytopoint 40 mg (Declined)` | 3205 | she declined Cytopoint. Also `Apoquel 5.4mg Oral Tablet (Declined)` L3217, `Simparica Trio Chewable Tablets for Dogs 22.1 to 44 Pounds, Teal Label (Declined)` L3229. |

She elected Apoquel at the Nov 20 2025 visit after declining Cytopoint twice.

## 7. Dental (a light track or a single touch)

| Span (usable) | Line | Use |
|---|---|---|
| `Discolored 203 tooth.` | 1632, 2106, 3102, 3646 | clean sub-span (line continues `mild tartar in caudal maxillary`) |
| `discussed sending estimates for dental cleaning and extraction of 202` | 2604 | whole line. The estimate was discussed, never booked in the record. |
| `Tartar accumulation - Oct 26, 2025` | 245 | problem-list entry |
| `mild gingivitis` | 1634 | usable sub-span |

## 8. FAS and handling

| Span (usable) | Line | Use |
|---|---|---|
| `Nervous and resists meeting new people` | 1129, 1900, 2857, 3419 | the intake FAS descriptor, appears at every visit |
| `1 - whale eye but was sweet for` | 555, 1373 | FAS 1, usable: `whale eye but was sweet` |
| `2 - avoidant and trying to flee, just very nervous girl, no aggression seen. Did not accept treats, prefers` | 3676 | usable: `avoidant and trying to flee, just very nervous girl, no aggression seen. Did not accept treats` |
| `female veterinarians.` | 3478 | weak alone. "The owner notes that Ikko has a preference for / female veterinarians." wraps L3477 to L3478. Use as design context, not a quote. |
| `Trazodone 2 hrs prior to visit` | 344 | pre-visit protocol, whole line |
| `Trazodone 100mg given prior to today's appointment` | 1127 | whole line |

## 9. Vaccines and preventives

| Span (usable) | Line | Use |
|---|---|---|
| `NEXT DUE DATE` then `Mar 26, 2027` | 2557, 2575 | Lepto next due Mar 26 2027 |
| `Mar 26, 2027` | 2584, 2594 | Lyme and Bordetella intranasal next due Mar 26 2027 |
| `Mar 26, 2029` | 2566 | DA2LPP next due, this looks wrong for a lepto combo (see inconsistencies) |
| `Nov 20, 2026` | 76 | Bordetella injectable (given Nov 20 2025) next due |
| `HWT due 3/28/27` | 2409 | heartworm test due date, whole line |
| `Simparica Trio Chewable Tablets for Dogs 22.1 to 44 Pounds, Teal Label` | 2520 | current parasite prevention |
| `Credelio Quattro for Dogs, 25.1-50 lbs, 1 Tablets` | 2723 | earlier parasite prevention, lots of Chewy refill back-and-forth |
| `FORWARD OndiKED ROUTINE WELLNESS` | 250 | forward-booked annual |
| `Nov 19, 2026 \| 1:30 pm` | 249 | the forward-booked annual date |

## 10. Data inconsistencies caught, and what we decided

**A. Left versus right paw.** The radiograph block at L584 to L585 reads `LEFT MANUS` and `left front digit four`. Every other reference in the file, the diagnosis at L561, the problem list at L247, the DDx, and the discharge, says **right front digit 4**.
**Decision:** clinic template error in the one radiograph block. We quote the right-front phrasing, which is consistent everywhere else. We note this in the journey footer as a caught inconsistency.

**B. Two bordetella entries with different due dates.** The header lists bordetella injectable given Nov 20 2025, next due `Nov 20, 2026` (L76), and bordetella intranasal given Mar 26 2026, next due `Mar 26, 2027` (L2594). A naive read of the export would flag her as due in November.
**Decision:** we do not fire a bordetella-due touch off the text export at all. Under rule 5 (no API), the export does not tell us reliably which vaccine record is live, and a wrong "your dog is overdue" message becomes part of the chart. The journey's vaccine touches depend on a structured Vetspire feed with a current-record flag, and we list that as a required field. We say this plainly in the journey footer.

**C. Nail onset date.** The problem list entry reads `Injury of nail - Jun 23, 2026` (L241). A later support note refers to Ikko being `previously seen on 07/03/2026 for a broken nail` (around L1161).
**Decision:** use `Jun 23, 2026`. The problem list is Vetspire's own dated field, the support note is a staff member's recollection, and the June date is consistent with the first physical exam in the file being June 23. We note the discrepancy in the footer so a reviewer sees we caught it.

## 11. Unknowns the journey has to branch on

- The **nail culture result** (pending as the record ends). Drives whether the antibiotic changes.
- The **amputation decision** (splint versus surgical repair versus amputation). Owner's call, ortho input pending.
- The **2-day recheck outcome** (bandage change, is the wound healing).
- Whether the **atopy is currently active** (flare reported Jun 2026, no exam confirming its state at the record's end).

## 12. Data we would ask Vetspire for

- Structured vaccine records with a "current" flag, so the two bordetella entries resolve cleanly.
- `next_due_date` per vaccine as a queryable field.
- Weight history as a series, so a "gained over winter" trend is detectable.
- BCS as a coded field, not free text.
- Appointment Booked and Estimate Issued events (the dental estimate, the 2-day recheck).
- Household links, to know Rico is in the same house and on overlapping meds.
- Message engagement (opens, clicks, replies) to gate the postcard fallback.
