# Evidence file: Quorra

**Source:** `records/z2_2-MRS-2.txt` · **doc_id:** `z2:2-MRS-2` · 4 pages. Two Petfolk pages plus a 2 page outside lab panel attached at the end.
**Journey anchor date:** Jul 24 2026, the second-opinion consult the owner booked. The record's "now" is Jul 23 2026, the day the owner emailed and the support team booked him. There is no Petfolk physical exam anywhere in this record. Everything here is a pre-consult inquiry plus one set of outside labs.

## How to read this file

Every span below is copied straight from the source. The number is the line it sits on. Multi-line spans give a range like `L32-33`. We assume Petfolk's string match normalises whitespace (`ground-rules.md`, assumption 1). `verify_quotes.py` checks the built HTML against the source.

**This record is thin.** Most of the value is in section 9, what is not here. The journey for Quorra is a new-client onboarding plus a senior workup plus a consent conversation, not a follow-up to an encounter.

**Aaliyan's verification job:** open `records/z2_2-MRS-2.txt`, go to the line number, confirm the span is character exact and means what the journey uses it for. Pay attention to section 8, the owner's email has apostrophes mangled to colons (`he:s`, `I:m`, `yorkie-poo:s`).

---

## 1. Identity and signalment

| Span | Line | Note |
|---|---|---|
| `Quorra \| 14 YO \| Male (Neutered) \| Yorkshire` | 20 | wraps to `Terrier` on L21. Senior dog, this is the whole story. |
| `Patient ID: PT-6A2B6A \| Canine` | 22 | key on this, not the client name (see §8) |
| `DOB: [MON] [DAY], 2012` | 23 | 14 years old in 2026, consistent with the header and the lab (`Age` `14Y`, L89-90) |
| `Petfolk - Vintage Park` | 9 | the clinic. Owner and the outside lab are in Cypress, TX. |

Breed is written three ways. `Yorkshire Terrier` on the Petfolk header (L20-21), `Mixed` on the outside lab (L85-86), and the owner calls him a `yorkie-poo` (L29), a Yorkie–Poodle cross. See §8.

## 2. Why the owner made contact (Jul 23 2026)

Two customer support communications logged the same afternoon, plus the owner's forwarded email. He is coming in for a **second opinion on three things**.

| Span | Line | Use |
|---|---|---|
| `I:m basically coming in for a second opinion on teeth, vaccine questions, and` | 36 | wraps to `bronchitis.` on L37. The clean statement of intent. Clean sub-span: `a second opinion on teeth, vaccine questions, and bronchitis.` (mind the mangled `I:m`, §8) |
| `Rec'd email from PP` | 28 | the contact was owner-initiated, by email |
| `PETFOLK - VIRTUAL CARE CENTER July 23, 2026 at 3:47 pm` | 26 | the email came in the afternoon of Jul 23 |
| `PETFOLK - VIRTUAL CARE CENTER July 23, 2026 at 3:03 pm` | 45 | the phone/booking note, 44 minutes earlier |

The owner is engaged and doing their own research. That posture drives the journey's tone: responsive, coordinated, information-first, because this owner is actively comparing clinics and could bounce.

## 3. The dental

| Span | Line | Use |
|---|---|---|
| `We will be coming in tomorrow for next [UNIT] on teeth extraction/cleaning.` | 30 | `[UNIT]` is a pseudonymiser gap (probably `step` or `consult`). Clean sub-span: `on teeth extraction/cleaning.` |
| `He only has a few teeth left.` | 30-31 | wraps `He` / `only has a few teeth left.` Advanced dental disease. The `:(` after it in the source is the owner's own emoticon. |
| `P needing dental cleaning but primary` | 53-54 | wraps to `DVM requires all vx to do anesthesia, PP does not want to vx pet.` L54-55. The whole standoff in one sentence. |
| `base` `cost dental $869` | 59-60 | wraps `base` / `cost dental $869`. The quoted dental base cost. |
| `Advised this could be discussed during` | 58 | wraps to `the dental consultation.` L58-59. The titer-vs-vaccine question was deferred to the Jul 24 consult. |

## 4. The vaccine, titer and anesthesia standoff (this is a consent situation)

The owner does not want to vaccinate. The primary DVM requires vaccines to clear anesthesia for the dental. The owner asked about titers as an alternative.

| Span | Line | Use |
|---|---|---|
| `primary` `DVM requires all vx to do anesthesia, PP does not` `want to vx pet.` | 53-55 | the requirement and the refusal |
| `Advised we do require RV as well.` | 55 | Petfolk also requires rabies (`RV`). Rabies is often legally non-waivable regardless of titer. |
| `PP inquired about titering.` | 56 | the owner raised titers first, not us |
| `Discussed we are able` `to offer titering, advised it would be DVM discretion if we were able to accept a titer in leu of the` `vaccine.` | 56-58 | Petfolk can run titers, but whether a titer substitutes for a vaccine for anesthesia clearance is the DVM's call. `leu` is a typo for `lieu` in the source. |
| `$379.80 RV titer (non export)` | 60 | quoted cost of a rabies titer. `non export` likely means it cannot be used for an interstate or international health certificate. |

**This governs the journey.** Under `ground-rules.md` rule 10, consent is real and a decline is respected. No vaccine marketing touch ever fires for Quorra. The only vaccine communication is a factual explanation of why anesthesia needs clearance and what the titer option is and does not do, with the decision left to the owner and the DVM.

## 5. The bronchitis

| Span | Line | Use |
|---|---|---|
| `I also have xrays I am waiting on because he was diagnosed with bronchitis last` | 32 | wraps to `week and is currently on [UNIT].` L32-33. Diagnosed by another vet about a week before, mid July 2026. `[UNIT]` is the medication, redacted, we do not know what he is on. Clean sub-span: `he was diagnosed with bronchitis last week`. |
| `The Dr. said he did not need antibiotics but` | 33-35 | wraps to `I have second thoughts about that as I read that the bronchitis could possibly / be caused by bacteria from his mouth.` The owner's specific worry: that the dental disease is seeding the airway. |
| `(he:s never had bronchitis before).` | 35 | new onset. Mangled apostrophe, §8. |

The owner wants Petfolk to weigh in on whether the bronchitis is dental in origin and whether antibiotics are warranted. That is a DVM judgement at the consult, not something a message answers.

## 6. The outside lab panel (7/1/2026)

Run at `[NAME] Animal Hospital`, Cypress TX, ordered by `Dr. E. Fairchild, DVM`. A full senior panel. The owner forwarded it. What matters:

| Finding | Span | Line |
|---|---|---|
| Hyperlipidemia | `CHOLESTEROL` `363 (HIGH)` (ref `92-324`) and `TRIGLYCERIDE` `461 (HIGH)` (ref `29-291`) | 181-188 |
| Lipemic sample | `Hemolysis 2+, , Lipemia 2+ No significant interference.` | 204 |
| Borderline azotemia ratio | `BUN/CREAT RATIO` `28 (HIGH)` (ref `4-27`). Creatinine `1.0` and `SDMA` `11.1` are both in range. | 145-147 |
| Proteinuria | `Protein` `2+ (HIGH)` on urinalysis, with `Urine protein:creatinine ratio testing is recommended (if the sediment is inactive) to help determine the clinical significance of` `proteinuria.` | 321-325 |
| Concentrated, alkaline urine | `Specific Gravity` `1.051 (HIGH)` (ref `1.015-1.050`), `pH` `8.0 (HIGH)` (ref `5.5-7.0`) | 315-320 |
| Struvite crystals, no infection | `Struvite (Triple P04) Crystals` `4-10` HPF, but `Bacteria` `NONE SEEN` and WBC `0-1` | 350-356 |
| Thyroid | `T4` `2.0` (ref `0.8-3.5`), mid range. The lab's interpretive note: `Diagnosis of canine hypothyroidism: for dogs with consistent clinical / signs and without non-thyroidal illness, a low-to-low normal T4 / concentration (e.g., <1.0 ug/dL) could support hypothyroidism.` | 282-288 |
| Pancreatitis screen | `PrecisionPSL` `58` (in range), with `Pancreatitis is unlikely, but a normal PrecisionPSL result does not completely exclude pancreatitis as a cause for gastrointestinal / signs.` | 193-198 |
| Parasites clear | `Ova & Parasite` `NONE SEEN` (L302-303) and `HEARTWORM ANTIGEN` `NO ANTIGEN DETECTED` (L368-369) | 302, 368 |
| CBC | unremarkable. `WBC` `10.1` in range, no left shift. Argues against, but does not rule out, an active bacterial process driving the bronchitis. | 210-241 |

The picture: a 14 year old with hyperlipidemia, borderline proteinuria and a concentrated alkaline urine with sterile struvite crystals, normal renal values and a normal T4, negative for heartworm and intestinal parasites. Nothing here is an emergency. Several things want a recheck. The DVM frames all of it at the consult, the journey supports the rechecks after.

## 7. Costs quoted (Jul 23 support note)

| Span | Line | Note |
|---|---|---|
| `Quoted $99 exam, base` `cost dental $869, $379.80 RV titer (non export)` | 59-60 | the first quote |
| `I accidentally misquoted` `and exam would be considered illness $135` | 61-62 | corrected. The consult is billed as an illness exam at `$135`, not a `$99` wellness exam. |

Use `$135` for the consult and `$869` for the dental base. The `$99` figure was retracted in the same note.

## 8. Data issues caught, and what we decided

**A. Owner email apostrophes are mangled to colons.** `yorkie-poo:s` (L29), `he:s never had bronchitis before` (L35), `I:m basically coming in` (L36). The pseudonymiser or the OCR replaced `'` with `:` in the forwarded email block.
**Decision:** the string match needs the colon form to pass, but a highlighted quote reading `he:s never had bronchitis before` looks broken in a customer-facing document. Where the journey quotes the owner, it uses fragments that do not contain the mangled contraction, for example `He only has a few teeth left.` and `a second opinion on teeth, vaccine questions, and bronchitis.` Logged in the footer.

**B. Breed conflict.** `Yorkshire Terrier` (Petfolk header), `Mixed` (outside lab), `yorkie-poo` (owner).
**Decision:** use the Petfolk header phrasing where a breed is shown, and describe him as a Yorkie cross in prose. The journey does not hinge on breed. Yorkies and their crosses are predisposed to hyperlipidemia, which is worth a line in the lab-explainer touch. Noted in the footer.

**C. Client name is reused across the corpus.** `Guthrie Pellow` here is a different household from `Guthrie Pellow` on Ikko3 and on other records. Same pseudonym, different people.
**Decision:** key on Patient ID `PT-6A2B6A`, never the client name. This is the standing rule (O2), noted here because Quorra is a clean example of it.

**D. The `$99` vs `$135` exam quote.** Not really a conflict, the staff member corrected themselves in the same note.
**Decision:** use `$135`. Noted so a reviewer sees we read to the end of the note.

## 9. What is NOT in this record

This is the important section for Quorra. The journey has to be honest about how little Petfolk has on file.

- **No Petfolk physical exam.** No vitals, no weight, no body condition score, no dental score, no exam findings. The Jul 24 consult would be the first.
- **No problem list.** Nothing in Vetspire's structured problem field.
- **No Petfolk vaccine history.** We do not know what he has ever had or when anything is due. The vaccine conversation is entirely driven by the primary DVM's anesthesia requirement, which is described secondhand in a support note.
- **The bronchitis diagnosis, the chest x-rays and the current medication are all at the outside clinic.** Petfolk has the owner's description and nothing else. `xrays I am waiting on` (L32) were not yet available to anyone when this record was generated.
- **The dental grading is the owner's description**, `He only has a few teeth left.` No Petfolk oral exam or dental radiographs.
- **The lab panel is outside work**, forwarded by the owner, not ordered or interpreted by Petfolk.
- **No membership status.** Nothing says whether this owner is a PetfolkCare member. The journey cannot assume it.

## 10. Unknowns the journey has to branch on

- **The Jul 24 consult outcome.** Does the DVM proceed toward the dental, accept a titer, require the vaccines, want the bronchitis worked up first. Everything downstream forks here.
- **Whether the bronchitis is stable or worsening.** New onset in a 14 year old. The journey needs a symptom check and an escalation path, but cannot presume a cause.
- **Whether the owner will vaccinate, titer, or decline and forgo the dental.** Their call. The journey gives the information and stops.
- **Membership status.** If they are not a member, a PetfolkCare value touch is relevant given the $869 dental. If they are, it is reassurance, not a pitch.
- **The proteinuria and lipids.** Do they get rechecked, does a UPC get run, is there an underlying endocrine driver. DVM-led.
- **Is the owner staying with Petfolk or the outside clinic**, or splitting care between them. The record shows active comparison.

## 11. Data we would ask Vetspire, or the outside clinic, for

- Any Petfolk vaccine history and current due dates as structured fields, so the vaccine conversation is grounded.
- The outside clinic's bronchitis notes, chest radiographs and the current medication, imported into the Vetspire chart (this is also the single highest-value retention action for this owner).
- A Petfolk oral exam and dental radiograph grading, once the consult happens.
- Weight, body condition and a baseline exam from the consult.
- PetfolkCare membership status.
- Appointment Booked and Appointment Completed events for the Jul 24 consult and anything that follows.
- Estimate Issued for the dental, so the agent follow-up only fires if it stalls.
- Lab Result events, so a UPC or a fasted lipid recheck can be tracked rather than guessed.
