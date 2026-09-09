# How a journey gets built

The repeatable method behind the five journeys in `question-1/journeys/`. Ikko (`z1_MRS-45`) is used as the running example. This is also the spec that Question 2 automates.

## The pipeline

Five phases per pet, one pet at a time, no batching.

1. **Evidence.** Pull every span we might quote straight from the source into `working/evidence/<pet>.md`, grep-checked, with line numbers, grouped by thread. Record the anchor date and the unknowns the journey has to branch on. Aaliyan verifies it against the source.
2. **Design.** Draft the journey in markdown: which threads become tracks, the touch list per track with trigger, channel, cost, gate and timing, and for every touch the exact evidence span it uses. Fast to review without HTML noise. Judgment calls surfaced here.
3. **Build.** Fill the Biscuit HTML template with the Phase 2 design. Quotes come only from the evidence file.
4. **Verify.** `working/scripts/verify_quotes.py` pulls every quoted span from the HTML and matches it against the source. Fix any miss, commit the clean log.
5. **Package.** Add the pet to `question-1/journeys/index.html`, export a PDF.

## Phase 2 in detail: turning a record into a journey

### Step 1, set the anchor

The journey needs a "now." For Ikko it is the sedated nail procedure on `Jul 27, 2026` plus the ortho follow-up email a day later. Everything earlier is history the journey draws on. The 12 months run forward from the anchor, the way Biscuit's run from day 0.

### Step 2, inventory every trigger candidate

Read the problem list, diagnoses, declines, meds and their sigs, vaccine dates, FAS notes, membership, household. Each is a candidate for a track or a touch. Ikko: nail fracture, atopy, overweight, stalled dental, recessed vulva, tartar, vet anxiety, the forward-booked annual, membership, Odie insurance.

### Step 3, sort into tracks, single touches, and left out

- **Track:** a multi-touch storyline with an entry event and an exit event. Warranted when there is an ongoing arc.
- **Single touch:** a one-off for a finding that needs exactly one mention.
- **Left out:** vet-led, already resolved, or a message adds nothing and risks cluttering the chart. Named in the footer so the choice is visible.

Ikko: weight is a track and the spine. The nail is a short careful track that forks on the culture result and the amputation decision, then exits when it resolves. Atopy is a track, refills plus flare checks. Dental is one touch plus a conditional bundle line. Recessed vulva is one touch. The amputation decision is left out of driving, the journey supports it but does not push it.

### Step 4, design each touch, six decisions

| Decision | What it means | Ikko example |
|---|---|---|
| **Trigger** | An event in Vetspire and Segment language. Composite is fine. | `Weight Status Changed + bcs + breed_key` |
| **What it says** | The function in our words, plus grounded content quoted verbatim from the evidence file. | weight program entry, carrying `Advised reducing her current food volume by a quarter of a cup daily` |
| **Channel** | Chosen by cost, intimacy, the pet's profile, and what the message has to do. Two-way and Giga-answerable is SMS. One-way education is email. Clinical is the nurse. Cost is the agent. A real milestone is a handwritten note. Digital silence is one postcard. | free tech weigh-in offered by email, monthly SMS after |
| **Gate** | Fires for everyone on the track, or only if something happens. Expensive touches almost always carry an "only if". | nurse call on the nail only if the 2-day recheck shows no improvement |
| **Cost** | From the fixed table, tallied at the end. | |
| **Timing** | A relative day offset, spaced so touches do not stack, repeated asks softened each time. | |

### Step 5, run every touch through the ground rules

Before a touch is final, check it against `ground-rules.md`:

- **Reply path.** If it makes the owner ask "what does this mean", can Giga answer from the record. If not, quote enough that it can, or route to a human on purpose.
- **Chart pollution.** Worth a permanent line in a chart a vet reads. If borderline, cut it.
- **Clinical claims.** Anything about the pet's health that is not a direct quote gets rewritten as a quote or a question.
- **Suppression.** If it fires while the vet has an open recheck loop running, it pauses. Ikko's nail is on a 2-day recheck cadence, so the recurring spine and any commercial touch pause until the nail track exits.
- **Consent.** Clinical touch fires regardless of a marketing opt-out. Commercial touch honours it.
- **Transactional spine.** Never rewritten, only layered on top.

### Step 6, the recurring spine

The always-on layer, Biscuit's Phase F. Annual rebooking, or "confirm the forward-booked visit" when one exists. Vaccine reminders, gated on structured Vetspire data when the export is unreliable. Membership, retrospective math for a member, a conversion pitch for a non-member. Lifestage. Insurance paperwork handed over automatically when the pet is insured.

### Step 7, the footer

Annual cost, unconditional and if-every-gate-fires. Data we would need from Vetspire. What we left out and why. Caught inconsistencies.

### Step 8, sanity pass

Unconditional spend around twenty to forty cents. Fully-escalated number makes sense for the risk. Fifteen to twenty-four touches. Every pet-specific phrase traces to the evidence file. Shape is Biscuit's: cheap first, humans gated on a real signal, tracks that end themselves, additive to the spine.

## What gets weighed throughout

1. **Usefulness against restraint.** The default is "do not send it."
2. **What comms can change.** Adherence, refill timing, booking a stalled procedure, showing up for a weigh-in, catching a problem early, membership retention. Not: the amputation decision, the allergy diagnosis, treatment. Touches only get built around the first list.
3. **The owner's state.** Engaged, cost-aware, an hour from the clinic. So lean on digital and virtual care, smooth the refill process, send money questions to the agent.
4. **Tone.** The nail is a scary open situation. The weight track is routine. Different tracks run in different registers.
5. **Biscuit as a scaffold, not a cage.** Biscuit resolved tidily. Real records are messier, with open crises and months-long conditions. The journey shows that honestly, with branches and "pause here if X".

## What is shared across all five journeys

Built once for Ikko, reused: the evidence-file format, the Biscuit CSS and HTML template, `verify_quotes.py`, the 11 ground rules, the footer structure, the trigger vocabulary.

Unique per pet: the evidence file, which threads become tracks, the judgment calls, the channel and gate choices.
