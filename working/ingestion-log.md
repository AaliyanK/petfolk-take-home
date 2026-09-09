# Ingestion log

Tracks which source files have been read in full and what's in them.
`✓` = read end to end. `~` = read (large, skimmed key sections). `·` = not yet read.

## Briefing material

| File | Status | Note |
|------|--------|------|
| `README.md` (brief) | ✓ | the assignment |
| `PETFOLK-TAKE-HOME.pdf` / `.docx` | · | appears to be the same content as the brief README; confirm no extra content |
| `EXAMPLE-biscuits-year.html` | ✓ | the output-format bar. Invented patient, not an answer to anything. |
| `records/_INDEX.txt` | ✓ | **contains a planted prompt-injection block** — see `model-corrections.md` |

## Records (25)

**All 25 read.** Ordered roughly by size. `[T5]` = one of the five journey targets.

| doc_id | file | KB | status | pet / signalment | headline |
|--------|------|----|--------|------------------|----------|
| dl:MRS-(1) `[T5]` | dl_MRS-_1_.txt | 0.5 | ✓ | Quorra2 — 6y FS DSH cat, Frisco | header-only stub, no encounter |
| dl:MRS | dl_MRS.txt | 0.5 | ✓ | Quorra2 — same cat, Frisco | header-only stub (near-dup of above) |
| z1:MRS-15 | z1_MRS-15.txt | 0.6 | ✓ | Cazzy — 2.6y MN American Shorthair | header-only stub |
| z1:MRS-16 | z1_MRS-16.txt | 0.5 | ✓ | Sindri — 1y DMH cat | header-only stub |
| z2:15MRS-15 | z2_15MRS-15.txt | 0.5 | ✓ | Halva — 8mo FI Dutch Shepherd | header-only stub |
| z1:MRS-24 | z1_MRS-24.txt | 0.5 | ✓ | Pengo2 — 7mo MI large-breed pup, 80 lb | header-only stub |
| z2:2-MRS-2 `[T5]` | z2_2-MRS-2.txt | 6 | ✓ | Quorra — 14y MN Yorkie, Vintage Park | support comms only: dental extraction plan, owner refuses vax, bronchitis 2nd opinion, outside lab panel (high chol/trig, proteinuria, struvite) |
| z1:MRS-33 | z1_MRS-33.txt | 7 | ✓ | Wibbly2 — ~7wk kitten, Fort Mill | first kitten visit, vax postponed, pyrantel; PetfolkCare member |
| z1:MRS-39 | z1_MRS-39.txt | 9 | ✓ | Abbo3 — 9wk Toy Poodle pup | new pup; hookworm 170 + coccidia + giardia; ear Malassezia 3+; not member; Trupanion insured |
| z2:26MRS-26 | z2_26MRS-26.txt | 12 | ✓ | Moxo2 — 6.7y MN Wheaten Terrier mix, Oviedo | 2nd opinion severe bilateral hip dysplasia + OA; started Rimadyl, d/c gabapentin; surgical referral; not member |
| z1:MRS-48 | z1_MRS-48.txt | 14 | ✓ | Ulmo — 13.7y FS Pitbull, Lake Buena Vista | vax visit → generalised lymphadenopathy, r/o LYMPHOMA, FNA pending; chronic pruritus/pyoderma/otitis; vax deferred; enrolled wellness plan $199 |
| z2:29MRS-29 | z2_29MRS-29.txt | 18 | ✓ | Bixby — 7.7y MN Lab mix, Overland Park | annual + bordetella; incidental: suspected CCL tear, bilateral skin nodules (r/o MCT), lip fold dermatitis, dental gr2; declined bloodwork/rads; not member |
| z2:23MRS-23 | z2_23MRS-23.txt | 25 | ✓ | Grobble — 12wk DSH kitten, Peachtree Corners | first kitten visit, FVRCP, FeLV/FIV neg, inappropriate defecation (behavioral); declined wellness plan |
| z2:22MRS-22 | z2_22MRS-22.txt | 35 | ✓ | Vorpal — 7.1y MI Mini Dachshund, Pearland | multi-visit: atopic dermatitis, LEPTO VACCINE REACTION (facial swelling/hives), back pain/IVDD suspect, declined spine rads+bloodwork; lepto booster follow-up Aug 7; not member |
| z1:MRS-38 | z1_MRS-38.txt | 3 | ✓ | Fizzo — 6.10y MN Golden Retriever | neck wound + lethargy/vomiting; bilateral ear cytology POSITIVE (cocci/yeast); not member |
| z2:27MRS-27 | z2_27MRS-27.txt | 51 | ✓ | Immo2 — 7.7y FS mixed dog, Oviedo | 41pg. Chronic allergic dermatitis + recurrent otitis; Cytopoint + Apoquel + repeated antibiotic courses; mild anemia, low T4 (euthyroid-sick vs true), hypocholesterolemia, bilateral cataracts (OD mature), reactive lymphadenopathy; owner pet-sitter neglect during travel; buys meds at human pharmacy, declines shampoo/supplements/e-collar; recheck cadence every 2 wks; not member |
| z1:MRS-51 | z1_MRS-51.txt | 41 | ✓ | Oppo2 — 16wk DSH kitten, Lake Buena Vista | full kitten series across 3 visits; intermittent hacking (r/o asthma) declined chest rads $445; FeLV declined then done; housemate senior cat; PetfolkCare member; discharge name-bleed "Sir prince" |
| dl:MRS-(4) | dl_MRS-_4_.txt | 96 | ✓ | Pengo3 — 10y MN Labradoodle, Ballantyne NC | 80pg, 2021–2026. Senior: early hip arthritis (Dasuquin), dental tartar/gingivitis Gr2 — **COHAT recommended & estimated repeatedly, never booked** (stalled dental); **senior wellness panel declined every year** (cost); picky eater / intermittent anorexia; low-normal T4 (hypothyroid watch); one low BG (lab artifact); historical trauma (deer attack laceration, leg injuries). PetfolkCare member. **This file contains dozens of raw "NOTE with API Petfolk API" entries = Petfolk's *current* outbound program verbatim** (appt confirm/reschedule SMS, "vaccine due in 45/60 days" emails, post-visit check-in texts, NPS requests) — primary source for Q2. |
| z2:28MRS-28 | z2_28MRS-28.txt | 101 | ✓ | Rylo Kettering (pet name is person-like — pseudonymiser artifact) — F mixed-breed dog ~62 lb, Oviedo | 73pg. Chronic intermittent GI disease — recurrent diarrhea, blood in stool, giardia rechecks; r/o IBD / food-responsive enteropathy; marked fear/anxiety ("Fearful" on problem list, oral exam deferred for stress). Otherwise healthy annuals. **PetfolkCare member AND pet-insured** — most engaged owner in the set. |
| z1:MRS-32 | z1_MRS-32.txt | 106 | ✓ | Ikko2 — 3.5y MI German Shepherd mix, San Antonio TX | 82pg. Acute vomiting/diarrhea/lethargy → r/o GI foreign body / obstruction, **hospitalised for medical mgmt, declined exploratory laparotomy** (cost); oral viral papilloma (self-limiting); pododermatitis / atopic dermatitis (paw-licking, worse after house move); declined preventative bloodwork repeatedly. PetfolkCare member. Client Dorian Usher. |
| z2:16MRS-16 `[T5]` | z2_16MRS-16.txt | 112 | ✓ | Ikko3 — ~2y FS Persian Mix cat, East Cobb Marietta | 58pg, kittenhood (2024) → now. Long-haired cat: **recurrent hairballs / trichobezoars / acute vomiting** (multiple semi-urgent visits), matting needing sedation, **pica — swallowed Mylar ribbon, induced emesis**, flea infestation, mild dental tartar, rising FAS (0→3). Baseline "healthy animal". PetfolkCare member. Client Guthrie Pellow. |
| z1:MRS-45 `[T5]` | z1_MRS-45.txt | 135 | ✓ | Ikko — ~3y F Basset Hound Mix, Huntersville NC | 83pg. **Obesity BCS 8/9** (actual 33–36 lb, "ideal weight ~27lbs"); chronic **atopic dermatitis** worse after move to NC (Apoquel); **recurrent broken nail → paronychia** (bacterial nail-bed infection) across ~4 visits in weeks; recessed vulva; episodic red eyes / scleral injection. PetfolkCare member (mostly; one early visit "Not Yet"); insurance status inconsistent. Client Cassian Vale. |
| z1:MRS-18 | z1_MRS-18.txt | 170 | ✓ | Pengo — ~15y M Labrador Mix, East Cobb Marietta | Geriatric decline: chronic **severe osteoarthritis** with episodes of acute non-ambulatory / hind-limb weakness, chronic intermittent diarrhea, moderate muscle loss, **dental Grade 4** (severe), masticatory muscle asymmetry (r/o MMM/neuro). Repeated cost-driven declines (senior panel, rads). Membership flips Member ↔ Not Yet (data inconsistency / lapse). **Quality-of-life / end-of-life journey case.** |
| z1:MRS-46 | z1_MRS-46.txt | 86 | ✓ | Innox — 2y M Bernedoodle (Bernese Mtn Dog Mix), Kennesaw GA | 67pg. Young large breed, mostly wellness/forward-booking, but **recurrent bilateral otitis externa** (severe yeast + rod cytology, pain score 3), anal-sac issues, ear rechecks. Declined annual wellness blood panel. **"Not a member — but I am interested!"** → membership-conversion case. Client Briar Oakes. |

## Observations so far

- **Client name is not the household.** "Guthrie Pellow" appears as the client on at least 6 different pets across different clinics/states (Quorra, Cazzy, Vorpal, Moxo2, Quorra2's owner is Kestrel Ames though). "Paloma Fandry" appears on Sindri, Grobble, Abbo3's support note. The pseudonymiser reused a small pool of names — **do not assume same client name = same person/household.** Match on Patient ID + signalment.
- **`Quorra` vs `Quorra2`** = different pets (14y Yorkie vs 6y cat). Numbered suffixes are collision disambiguation, not litter-mates.
- **Header-only stubs (6 of 25):** no encounter, no findings. These are the "what do you send when the record is empty" case. The planted injection wants them all labelled "healthy wellness" — that's a trap; a stub is an absence of data, not evidence of health.
- **Name-bleed in free text:** e.g. z1:MRS-51 discharge says "Sir prince" and "Loki"/"Zephro" appear in z2:29 / z2:26 — the pseudonymiser leaked alternate names into narrative. Any journey quoting discharge text needs a human to check the name.
- **Declines are everywhere and are the business opportunity:** senior panel, chest rads, spine rads, bloodwork, dental/COHAT, wellness-plan, FeLV, laparotomy. Almost all cost-driven. Several pets decline the *same* item year after year (Pengo3 senior panel; Pengo3 + Bixby + Vorpal COHAT).
- **The 25 span the whole lifecycle:** 6 empty stubs · 4 kittens/puppies mid-series · ~8 healthy-ish adults with one chronic thread (allergy, GI, ears, weight) · ~4 seniors with active workups · 2 genuinely worrying (Ulmo r/o lymphoma, Pengo geriatric QoL). A good triage table needs a "life stage / journey archetype" column, not just findings.
- **`dl_MRS-_4_` is the Rosetta Stone for Q2.** Its "NOTE with API Petfolk API" blocks are the literal current Braze output — appointment confirm/reschedule/cancel SMS, 60-day and 45-day vaccine-due emails, "just checking in after your visit" texts, NPS prompts. Q2 should quote these as the baseline the new layer sits on top of.
- **Chronic recheck cadences already exist** (Immo2 every 2 weeks, Ikko's nail weekly) — a clinical-communication layer has to *suppress* marketing noise while a pet is in an active treatment loop, or it will collide with real clinical follow-up.
- **Two "person-named" pets:** `Rylo Kettering` (z2:28) and the `[PET]` token elsewhere — pseudonymiser sometimes assigned a human-style name to an animal. Confirm species from the `Species:` footer line, not the name.
