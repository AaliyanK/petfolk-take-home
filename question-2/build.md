# Question 2: how to build the thing that decides

Q1 produced two things: a method for turning one medical record into a year of communication
(`working/how-i-build-a-journey.md`), and a rubric for classifying any record in one pass
(`question-1/triage.md`). Together those are the thing that decides. This is how it runs automatically
across 42 clinics today and 100 in two years, on the stack as it is.

## Where we are today

Every message Petfolk sends is logged into the chart by the same webhook that will carry the new
layer, so one record, Pengo3 (`dl_MRS-_4_`), is a four year transcript of the entire current program.
It is all logistics:

- appointment confirmations, "Press 1 to confirm 2 to reschedule 3 to cancel", and
  "appointments not confirmed 24 hours prior to the appointment time will be canceled."
- a post visit note, "We just wanted to check in on Pengo3 after your visit yesterday."
- a vaccine reminder, "Received an email about their alive + active pets having a Rabies, Lepto,
  DAPP, Bordetella, FVRCP, or FeLV vaccine due in 60 days ... Next email in 15 days if still not
  compliant."
- marketing, "local events and exclusive offers in the Charlotte area", "refer a friend and gift
  them $50 off their first appointment."

Nothing about Pengo3's stalled dental, his arthritis, or the senior blood panel he has declined three
years running. The clinical detail never leaves the chart. That is what the new layer sends.

## The architecture

The new layer is one service between Segment and Braze. It does not replace anything. The
transactional spine already runs across all 42 clinics and already reads structured Vetspire data, so
adding a clinic is a config flag, not an integration.

```
Vetspire              vet finishes an encounter, an event is emitted
     │
     ▼
Segment               normalises and routes the event
     │
     ▼
Decisioning service   the new layer, one service between Segment and Braze
     │
     │   1  classify      archetype + tier              (the Q1b rubric)
     │   2  select        one journey template          (the Q1a method)
     │   3  guardrail     consent, suppression, chart budget,
     │                    string match every quoted span at send time
     │
     ├──  cannot fill a slot safely  ──►  task to the clinic   (fail closed)
     │
     ▼
Braze                 journey logic fires, sends Email / SMS / Push
     │
     ├──────────────────►  pet parent receives the message
     │
     └──(webhook)───────►  a copy is written into the Vetspire chart,
                           so it becomes part of the medical record


Templates             a clinician approves each one once, then it can be selected


Pet parent hits reply
     │
     ▼
Giga                  answers from the same context the message was built from
     │
     ├──  clinical  ──────────►  Gladly, nurse queue
     └──  cost or scheduling  ─►  Gladly, agent queue
```

The classify and select steps are the Q1b rubric and the Q1a method run as config. The guardrail is
the ground rules run as code. Nothing sends unless every quoted span matches a field in that pet's own
record, and anything the template cannot fill safely fails closed to a task rather than a guess.

## Method to machine

The manual pipeline maps almost one to one onto components.

| Manual step (Q1a) | Runs as |
|---|---|
| Set the anchor, inventory trigger candidates | a Vetspire event arrives via Segment, with the pet's problem list, meds, vaccine dates, FAS, membership, consent as attributes |
| Sort into tracks, touches, left out | the classifier picks an archetype and tier, which selects one pre authored journey template |
| The six decisions per touch | baked into the template: trigger, channel, gate, timing, and copy with named slots (next section) |
| Run every touch through the ground rules | the guardrail layer, below |
| The recurring spine | one standing always on journey, identical for every pet, additive |
| The footer, the sanity pass | monitoring: cost per tier, touch counts, escalation rates, a sampled human audit |

The model drafts templates and tunes the classifier. It never writes a live message. A live send is a
template plus that pet's data, deterministic, with no model in the path.

## What a template is

A template is the pre-authored unit that replaces hand-building a journey per pet. Five parts.

| Part | What it is |
|---|---|
| Entry rules | which pets it runs for: an archetype, a tier, and conditions. "Cat, healthy adult, T2, with a dental finding on the problem list." |
| Structure | the tracks and touches from Q1a. Each touch has a trigger event, a channel, a gate, and a day offset. |
| Copy | the message wording. Fixed, approved, not generated. |
| Slots | named blanks in the copy, filled at send time from the pet's record. |
| Field map | which Vetspire field feeds which slot. |

A slot is one of two kinds. A **data slot** (pet name, appointment date, membership status) fills from
a field as plain text. A **verbatim quote slot** (the vet's own words about the teeth) fills only from
one named field in that pet's record, and the string match gate then checks the filled text actually
appears in that field. If the field is empty or the match fails, nothing sends.

The first template to go live, discharge summary enrichment, looks like this:

```
template: discharge_enrichment_v1
entry:    any Encounter Completed
touch:    day 0, evening · email
gate:     clinical consent on file · pet not in a suppressed state

copy:
  "We saw {pet_name} today. Here is what the vet found and what happens next.

   {diagnosis_quote}

   {plan_quote}

   {home_care_quote}

   Reply to this email and a real person will get back to you."

field map:
  pet_name         <- patient.name                     (data slot)
  diagnosis_quote  <- encounter.assessment_text         (verbatim, string matched)
  plan_quote       <- encounter.plan_text               (verbatim, string matched)
  home_care_quote  <- encounter.discharge_instructions  (verbatim, string matched)
```

A clinician reads that once. They are approving the frame and the field map, that the diagnosis comes
from `assessment_text` and not from some free text note that might name the wrong pet. Every send is
that frame plus three spans lifted straight from the chart. Nothing is written live.

The five Q1a journeys are five template instances, one per archetype. Ikko's journey is the "dog,
acute turned chronic, T2 to T3" template filled with Ikko's data.

## The one hard part: review without a review board

Every send becomes the medical record and no one signs off on clinical content today. You cannot
review every message, there are millions. You can review a few hundred templates, once each, and
because a template is deterministic, reviewing it once tells you what every send from it will look
like. The only thing that varies per pet is which field values get slotted in, and the field map plus
the string match gate box that in.

So review moves to the template level. A clinician approves each **template** once. The verbatim quote
slots are checked at send time by the same string match used in Q1
(`working/scripts/verify_quotes.py`), now a runtime gate: if a quoted span does not match a field in
that pet's record, the message does not go. Anything the template cannot fill safely **fails closed**
to a task for the clinic, it does not send a guess. On top of that, a sampled audit of live sends and
a kill switch per journey type per clinic.

This needs a role that does not exist today: a clinical communications owner who approves templates,
runs the audit, and holds the kill switch. Name it, staff it before go live.

## The reply path

Every send carries a reference to the context it was built from. Giga reads that context on a reply
and answers from the same source the message used, or routes: clinical to the nurse queue, cost and
scheduling to the agent queue, the two queues never cross. Support inbound is dominated by
appointments, prices, records and balances and medical questions barely register today, so any
template that would generate medical replies Giga cannot answer is not approved.

## Rollout, 42 to 100

| Phase | What | Gate to the next phase |
|---|---|---|
| Shadow | the service computes the decision for every eligible pet, sends nothing, logs what it would have sent | a human agrees with the call on a sampled set |
| One journey type | discharge summary enrichment goes live at a handful of low risk clinics. Lowest clinical risk, highest owner value, it is mostly quoting the vet | audit clean, reply volume within the nurse queue's capacity |
| Expand | one journey type at a time, clinics in waves | per journey and per clinic flags stay, so anything can be switched off in seconds |

New clinics inherit the whole thing on day one because it is event driven off Vetspire, which they
already run.

## The budget

$1.50 per patient per year is fine as a population planning number and wrong as a per pet rule,
because it does not let the system spend $12 on Pobble and 10 cents on a healthy cat. Spend by the
Q1b tiers (`question-1/triage.md`): T0 and T1 cost cents, T2 a few dollars, T3 eight to twenty five.
Most pets are T0 to T2, so the money concentrates on the T2 and T3 minority and the blended average
still lands near $1.50. The difference is that every pet's number is now defensible.

## What we would need, and the risks

- **Data.** Every field the Q1 journey footers list as missing (structured vaccine next due dates,
  message engagement, channel preference, membership status, weight and BCS history, Appointment
  Booked and Estimate Issued events, household links). Almost all of these are export limitations, not
  system limitations. The service subscribes to them from Segment.
- **Org.** The clinical communications owner role. Without it, templates ship unreviewed and the
  chart pollution risk is real.
- **Risks.** A template that reads the wrong field and quotes it confidently. The string match gate
  catches a fabricated quote, not a real quote pulled from the wrong slot, so slot mapping is part of
  template review. A reply spike that swamps the nurse queue, mitigated by the shadow phase capacity
  check and the kill switch. Consent drift as templates multiply, mitigated by the guardrail checking
  consent on every send regardless of template.

## Where AI did the work, where a human decided

AI assembled the current state picture from the Pengo3 blocks, mapped the manual steps to components,
and drafts the templates and the classifier. The calls it could not make: review moves to the
template level, the system fails closed, and a clinical communications owner role has to be created
and staffed. Those are the load bearing decisions in this document and they are human ones.

The prompts, scripts and notes behind the whole submission are in `working/`: `prompts.md` (the
session log), `scripts/verify_quotes.py` (the string match gate, which this design promotes to a
runtime check), `how-i-worked.md` and `decisions-log.md` (the narrative and every judgment call),
`model-corrections.md` (where the model was wrong and it was caught).
