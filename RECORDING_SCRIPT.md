# 3-Minute Screen Recording Narration Script
**Project:** SpendNest Revenue Intelligence Inbox  
**Candidate Walkthrough Guide**  
**Target Duration:** Exactly 3 minutes (180 seconds)  
**Format:** Continuous single-take screen recording with spoken voiceover.

---

## Preparation Checklist Before Recording
1. Open `index.html` in your web browser (Chrome, Edge, or Safari).
2. Ensure browser window is maximized (1920x1080 or clean 16:9 ratio).
3. Have your microphone ready. (Note from recruiters: *"We assess your reasoning, not your accent or audio quality."*)
4. Ensure the app is in its default initial state (click "Reset" on the top quickbar if needed).

---

## Timed Narration & Action Timeline

### Part 1: Useful Manager Workflow (0:00 – 0:50)

- **On-Screen Action (0:00 – 0:15):**  
  Start on the **Executive Dashboard** tab. Move the cursor smoothly over the KPI cards.
- **Spoken Narration (0:00 – 0:15):**  
  > *"Hello. Welcome to the SpendNest Revenue Intelligence Inbox. As a sales manager, my first screen immediately answers what happened on August 21st across our team. Notice our headline metrics: we have 44 selected interactions—30 calls and 14 meetings. Rather than blending unverified numbers, we explicitly separate our denominators."*

- **On-Screen Action (0:15 – 0:30):**  
  Hover over the **Source Connection Rate** KPI (36.7%) and then point to the **Verified Dialogue Rate** (100%).
- **Spoken Narration (0:15 – 0:30):**  
  > *"For example, looking at connection rate: the upstream telephony system claims only a 36.7% connection rate—11 out of 30 calls. But when we audit actual conversational dialogue, our verified connect rate on recorded calls is 100%, 10 out of 10. Upstream machine flags misclassify voicemails like C04 as disconnected, while counting silent rings like B11 as connected."*

- **On-Screen Action (0:30 – 0:50):**  
  Click on the **Inbox & Deep Inspector** tab. Click on `M03: Asterloom Systems` in the master list.
- **Spoken Narration (0:30 – 0:50):**  
  > *"Moving into our daily inbox, let's inspect our highest-priority pipeline opportunity: Asterloom Systems (M03). Here, the manager sees exactly what happened: Asterloom wants corporate prepaid cards to replace employee reimbursements. Customer B mentioned a potential monthly spend of INR 10 to 13 lakh in Turn 10. Crucially, our system highlights 'Honest Uncertainty': the customer explicitly stated that figure needs CFO validation, and domestic cards are prepaid wallets, not credit. We deliberately do not hallucinate a fake pipeline revenue total."*

---

### Part 2: Difficult Routing Decision (0:50 – 1:40)

- **On-Screen Action (0:50 – 1:15):**  
  In the inbox search bar, type `M02` or filter by `Internal & Vendor Operations`. Click on `M02: LedgerBridge / SpendNest discussion`.
- **Spoken Narration (0:50 – 1:15):**  
  > *"Now, let's examine a difficult routing decision: Meeting M02, titled 'LedgerBridge / SpendNest discussion'. In a conventional CRM, this calendar title looks like a high-value prospect sales meeting. However, our context-aware routing inspected the actual dialogue. In Turn 1, our strategy lead says: 'We want to understand whether LedgerBridge can give us compliant invoicing coverage across our operating markets.' LedgerBridge is a third-party software vendor, and SpendNest is the buyer! Naive classification would inflate our sales pipeline with procurement costs."*

- **On-Screen Action (1:15 – 1:40):**  
  Click the **Route Override** dropdown at the top right of the inspector. Select `Internal & Vendor Operations` or demonstrate changing a route, showing the prompt.
- **Spoken Narration (1:15 – 1:40):**  
  > *"We routed M02 to 'Internal & Vendor Operations'. If a manager ever needs to reassign or correct a route, they simply select the dropdown. The system prompts for a reason and marks the decision as a preserved manual override. Human judgment is always respected over automated heuristics."*

---

### Part 3: Duplicate & Update Replay Test (1:40 – 3:00)

- **On-Screen Action (1:40 – 1:55):**  
  Click the **Replay Suite & Invariant Audit** tab (or use the Replay Quickbar buttons).
- **Spoken Narration (1:40 – 1:55):**  
  > *"Next, let's verify the public data contract and replay steps. The contract requires that our system is completely idempotent: repeat imports must never create duplicate records or inflate activity counts, and late-arriving transcripts must update existing records without wiping manual overrides."*

- **On-Screen Action (1:55 – 2:15):**  
  Click **Button 2: Re-import (Dedup Check)**. Look at the toast notification and the audit table.
- **Spoken Narration (1:55 – 2:15):**  
  > *"Let's run Step 2: I am now re-importing the initial batch with all 44 records in a shuffled order. Look at the record count: it stays exactly 44. Zero duplicate records are created. Every metric and activity count remains perfectly stable. The deduplication invariant passes."*

- **On-Screen Action (2:15 – 2:35):**  
  Click **Button 3: Override Route (M07)**. Notice that M07 is now manually overridden.
- **Spoken Narration (2:15 – 2:35):**  
  > *"Now Step 3: in the initial batch, Meeting M07 (Willowfield Trust) arrived without a transcript. I manually override its route to Customer Success because I know this is an active customer bug triage session. The override is saved in local storage."*

- **On-Screen Action (2:35 – 3:00):**  
  Click **Button 4: Update Batch (M07 v2)**. Then click **Button 5: Verify State** (or refresh the page). Point to the M07 turns in the inbox.
- **Spoken Narration (2:35 – 3:00):**  
  > *"Now Step 4: we import the update batch, which contains revision 2 of M07. Watch the transcript coverage: it increases from 17 to 18 usable transcripts. The total record count stays at 44. M07 now has 27 full dialogue turns visible in the inspector. Finally, Step 5: after reloading the application, our manual override on M07 remains fully intact! And with one click on 'Download Export ZIP', all generated files and manifests are exported offline. Thank you!"*

---

## Key Terms & Metrics to Pronounce Clearly
- **SpendNest:** *Spend-Nest*
- **Denominator:** Clarify that 44 is the total selected sample, 30 calls, 14 meetings.
- **C04 Voicemail:** 95-second voicemail left by Arun for Ritesh.
- **C06 Identity Discrepancy:** Rep listed as Meera, but speaker introduces himself as Ravi.
- **M02:** LedgerBridge vendor evaluation (e-invoicing), NOT a prospect.
- **M07:** Willowfield Trust (late transcript in update batch).
