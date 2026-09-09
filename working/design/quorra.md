# Journey design: Quorra

Phase 2 output. This is the plan the HTML is built from. Every quoted span cites `working/evidence/quorra.md`.
Aaliyan reviews this before the HTML is built. The data-conflict calls behind it are in `working/evidence/quorra.md` section 8 and in `working/decisions-log.md`.

## Patient card

**Quorra · 14y neutered male Yorkshire Terrier (Yorkie cross) · Cypress, TX · Petfolk Vintage Park**

Chips (facts on file, quoted where possible):
- `Quorra | 14 YO | Male (Neutered) | Yorkshire` Terrier, senior
- new to Petfolk, first visit is the `Jul 24 2026` second-opinion consult
- `on teeth extraction/cleaning`, `He only has a few teeth left.`
- owner declines vaccines, `PP inquired about titering.`, `Advised we do require RV as well.`
- `he was diagnosed with bronchitis last week` at another clinic, owner suspects a dental cause
- outside senior panel 7/1/2026: hyperlipidemia, proteinuria, concentrated alkaline urine with sterile struvite crystals, normal renal values, `T4` `2.0` normal
- PetfolkCare membership status unknown (not in the record)

## Anchor

Day 0 = the second-opinion consult on `Jul 24 2026`. The record's "now" is Jul 23, the day the owner emailed and support booked him. There is no prior Petfolk encounter. Twelve months run to July 2027.

## What this is

A 14 year old Yorkie new to Petfolk. The owner emailed the day before a consult that covers three things at once: advanced dental disease that needs extractions under anaesthesia, a vaccine versus titer standoff that is blocking that anaesthesia, and a new bronchitis diagnosis from another vet that the owner suspects is coming from the mouth. Petfolk has no exam, no problem list and no vaccine history on file. It has the owner's email and one forwarded lab panel.

The journey is a new-client onboarding, a senior workup and a consent conversation running together. Its main job is to be coordinated enough that an owner who is actively comparing clinics makes Petfolk the primary.

---

## Track A · the consult, and making it productive

Entry: Appointment Booked (Jul 24 consult). Exit: consult completed and summarised.

| Day | Channel | What | Why / quoted spans (ev §) | Trigger | Cost |
|---|---|---|---|---|---|
| −1 (Jul 23) | Email | consult confirmation and what to bring | Booked the same afternoon the owner emailed. Bring the chest x-rays or the outside clinic's name so we can request them, the current bronchitis medication name and dose, any prior vaccine records, and Quorra's normal food. Set the frame: this is an illness consult at `$135` (§7) covering `a second opinion on teeth, vaccine questions, and bronchitis.` (§2), and the dental decision follows an oral exam. | Appointment Booked | $0.002 |
| 0 | Visit | the second-opinion consult | first Petfolk exam on record. Oral exam, listen to the chest, review the outside panel, talk through the vaccine and titer question. | Encounter Completed | clinic |
| 0, eve | Email | enriched consult summary | this owner processes by reading, so everything the DVM found and recommended goes in writing, structured by the three topics. No template conclusions, the DVM's words. | Encounter Completed | $0.002 |
| 1 | Email | records-request kickoff | **the retention move, and a clinical prerequisite.** With the owner's authorisation, request Quorra's chest x-rays and bronchitis notes from the outside clinic so anaesthesia clearance and the bronchitis question both work off one chart. | Encounter Completed + consent_to_release | $0.002 |

---

## Track B · the dental pathway

Entry: dental need confirmed at the consult + Estimate Issued. Exit: dental booked (hands to the procedure funnel) or the owner declines.

| Day | Channel | What | Why / quoted spans (ev §3, §4, §7) | Trigger | Cost |
|---|---|---|---|---|---|
| ~3 | Email | the dental plan | what the oral exam showed, what extraction under anaesthesia for a 14 year old involves, the pre-anaesthetic workup (he already has most of the bloodwork), the `base` `cost dental $869`, and the senior-anaesthesia framing: age alone is not a contraindication, here is how we de-risk it. PetfolkCare savings line **only if Vetspire shows non-member**. | Estimate Issued: dental | $0.002 |
| ~10 | Email | the vaccine and titer decision, factual | **only if the DVM's clearance requires a vaccine decision.** Presents, in order: why anaesthesia needs clearance, what the primary DVM required (`DVM requires all vx to do anesthesia`), what a titer measures and its limits, that `Advised we do require RV as well.` and rabies is often not waivable by titer, and the `$379.80 RV titer (non export)` cost. Closes: this is your decision with the DVM, here is a slot to talk it through. No benefit-of-vaccination language, no urgency, no risk framing beyond the factual clearance requirement. | clearance_requires_vaccine_decision | $0.002 |
| ~12 | Nurse | tele-call about the trade-off | **only if the owner books it from that email.** A real conversation, titer versus vaccine versus not proceeding, led by a nurse who can pull the DVM's position. | owner booked | $6.00 |
| ~24 | Support agent | call about the dental estimate | **only if the estimate is unbooked after about 14 days.** Cost, payment plan, scheduling. Not the clinical side. | Estimate Issued + not booked | $4.00 |
| exit | System | dental booked and the procedure funnel takes over, or the owner declines and the topic drops until the annual | | Procedure Booked, or decline recorded | — |

---

## Track C · the bronchitis

Entry: owner-reported bronchitis + the "is it dental" question. Exit: outside records in and the DVM opinion given, or the cough resolves.

| Day | Channel | What | Why / quoted spans (ev §5) | Trigger | Cost |
|---|---|---|---|---|---|
| ~2 | Email | bronchitis coordination | we have asked for the x-rays. In the meantime, what to watch for: worsening cough, exercise intolerance, blue or grey gums, not eating. When to call versus when to go straight to the ER. | bronchitis flag + records_requested | $0.002 |
| ~5 | SMS | "how is Quorra's breathing and cough? reply 1 to 3" | 1 is same or better. 2 is coughing more but eating and active. 3 is worse, tired, or off food. New onset in a 14 year old, so this is a real check. | bronchitis flag | $0.015 |
| ~5 | Giga | answers the reply | 1 or 2 from the coordination email. A 3 goes to the nurse. | reply received | $0.05 |
| ~7 | Nurse | tele-advice | **only if she replied 3.** | reply == 3 | $6.00 |
| ~30 | Email | the DVM's read, once the outside x-rays are in the chart | answers the owner's original worry, whether the airway and the mouth are connected and whether antibiotics are indicated, `The Dr. said he did not need antibiotics but` the owner `I have second thoughts`. From the vet, not a template. | outside_records_imported + DVM_review | $0.002 |

---

## Track D · the senior labs

Entry: the outside panel on file. Exit: rechecks done or declined. Delayed past the consult so the DVM frames the panel first.

| Day | Channel | What | Why / quoted spans (ev §6) | Trigger | Cost |
|---|---|---|---|---|---|
| ~14 | Email | the lab explainer, plain language | walks the panel: hyperlipidemia (`CHOLESTEROL` `363 (HIGH)`, `TRIGLYCERIDE` `461 (HIGH)`), what a fasted recheck clarifies, and the Yorkie-cross predisposition; the proteinuria (`Protein` `2+ (HIGH)`) and the panel's own recommendation, `Urine protein:creatinine ratio testing is recommended`; the reassuring parts, `T4` `2.0`, `HEARTWORM ANTIGEN` `NO ANTIGEN DETECTED`, `Ova & Parasite` `NONE SEEN`. What the DVM wants to recheck and when. | outside panel on file + post-consult | $0.002 |
| ~16 | SMS | "want us to set up Quorra's recheck labs? reply YES" | owner-interest gated, sets a care flag for the next visit | prior email delivered | $0.015 |
| ~120, ~240 | Email | recheck-due nudge, UPC and fasted lipids | **only if the DVM ordered them and they are not done** | recheck ordered + overdue | $0.002 each |

---

## Track E · the senior wellness spine

| Day | Channel | What | Why / quoted spans | Trigger | Cost |
|---|---|---|---|---|---|
| ~30 | Email | membership | **if non-member:** framed around the `$869` dental and the recheck cadence a 14 year old needs, not a hard pitch. **if member:** "your plan covers X" reassurance. | pfc_status resolved | $0.002 |
| ~45 | Email | new-to-Petfolk welcome | how to reach us, virtual care, the after-hours path, and that a reply lands with a real person. Not salesy. | new client + 45 days | $0.002 |
| ~90, ~180, ~270 | SMS | senior check-in | weight, appetite, energy, cough, mobility, any new lumps. Light touch, reply path to the nurse. | recurring, senior | $0.015 each |
| ~180 | Email | mid-year senior summary | what Petfolk has done, what is monitored, what is next | 180-day history | $0.002 |
| ~300 | Email | quality-of-life awareness | **off by default. Only fires if the quarterly checks show a decline signal.** Third-and-gentlest register. | decline signal | $0.002 |
| month 12 | Push | annual senior wellness forward-book | SMS fallback if no app engagement | 12 months + no future appointment | $0.001 |
| month 12 + 2wks | Postcard | one card to the address on file | **only if no email, app or SMS engagement in 90 days.** Very unlikely, this owner is email-first. | engagement gap | $0.85 |

---

## Suppression rules

- **No vaccine marketing, ever.** The only vaccine touch is the factual titer explainer in Track B, and it only fires if the DVM's clearance actually requires the decision. `ground-rules.md` rule 10.
- Tracks D and E are held until after the consult so the DVM frames the labs and the plan first.
- The quality-of-life touch is off unless a quarterly check shows a decline.
- If the owner declines the dental, Track B exits quietly. The topic returns once, at the annual, not before.
- Track C urgent routing overrides suppression.

## Footer content

**What the record does not carry, and what we would ask for:**
Almost everything structured. A Petfolk vaccine history and due dates, a problem list, any exam with weight and body condition, PetfolkCare membership status, the outside clinic's bronchitis notes and chest radiographs and current medication, Estimate Issued, Appointment Booked and Completed events, and Lab Result events. This journey is largely a list of what Petfolk would need to pull in.

**Left out and why:**
- Any vaccine encouragement. The owner has declined, and consent is real (rule 10). The journey gives information and stops.
- A stated cause for the bronchitis. Not ours to state, it is a DVM judgement at the consult.
- Assuming membership either way. It is not in the record, so the membership touch branches on the real status.

**Inconsistencies caught in the record (ev §8):**
- The owner's forwarded email has apostrophes mangled to colons, `he:s`, `I:m`, `yorkie-poo:s`. The journey quotes fragments that avoid the mangled contractions.
- Breed is written three ways, `Yorkshire Terrier` on the Petfolk header, `Mixed` on the outside lab, `yorkie-poo` by the owner. Used the header, described him as a Yorkie cross in prose.
- The client name `Guthrie Pellow` is reused across the corpus for different households. Keyed on Patient ID `PT-6A2B6A`.
- The `$99` exam quote was retracted to `$135` in the same support note. Used `$135`.

## Cost

**Unconditional** (everything that fires on a quiet path): about **$0.18 / year**. This owner is email-heavy: roughly 13 emails, 6 SMS, 1 push, 1 to 2 Giga chats.

**If every gate fires** (a bronchitis escalation, a titer nurse call, a senior-lab nurse call, a stalled dental estimate, digital silence): about **$21 / year**. Driven by two or three nurse calls, one agent call and the records coordination.

A 14 year old with three active problems and an owner who is comparing clinics belongs at the high end. The $1.50 average describes neither number.

## Touch count

About 22 across 12 months, in the Biscuit range.
