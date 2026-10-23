# Revenue Intelligence Inbox — Five Presentation Slides
**Candidate Submission for SpendNest Revenue Intelligence Assessment**  
**Date:** 21 August 2026 (Asia/Kolkata Context)  
**Format:** Slide Deck (Viewable via `slides.html` or embedded in the web application tab)

---

## Slide 1: The Manager Problem & Main Findings

### Header
**Synthesizing Fragmented Sales Evidence into Actionable Operational Direction**

### 1. The Manager Problem Chosen to Solve
Sales managers are bombarded with raw telephone call logs, meeting notetaker recordings, and automated CRM labels from multiple upstream systems. These records arrive asynchronously (some transcripts are delayed), carry inaccurate system-generated tags, and conflate internal discussions with customer pipeline. The manager needs an executive control center that cuts through the noise, highlights immediate revenue and churn risks, and provides evidence-backed next steps without creating artificial metrics.

### 2. Three Most Important Findings (With Source Citations & Product Impacts)

1. **Finding 1: Metadata vs. Spoken Identity Discrepancy (Account Sharing / Dialer Attribution Bug)**
   - *Observation:* Call `C06` metadata records `rep_name: "Meera"`, but the caller explicitly introduces himself as:
     > *"Hello? Good evening, Mr Nikhil. Good evening. Ravi here. I'll say at the start that this is a cold call."* (Call `C06`, exact quote).
   - *Where It Affected the Product:* 
     - **Screen:** Alerted in the **Executive Dashboard Exception Notice** and highlighted in the **C06 Deep Inspector View** with a `Metadata Discrepancy` warning.
     - **Rule/Output:** Attributed to *"Meera (Spoken: Ravi)"* in `exports/manifest.json` and flagged in `manager_brief_2026-08-21.md` under "Rep Attribution Audit" to prevent misallocating sales coaching or activity bonuses to Meera.

2. **Finding 2: False Positive & Inverted Upstream Telephony Connection Flags**
   - *Observation:* Upstream machine classification flags conflict directly with conversation evidence. Call `C04` is labelled `is_connected: false` and `is_conversation: false`, yet Arun delivered a complete, substantive 95-second voicemail addressing a misdirected proposal:
     > *"Hello, this is a message for Ritesh. Arun from SpendNest here. I'm following up on your consideration of our expense platform for Lanternpath Media. My understanding is that our information first went to the wrong email address..."* (Call `C04`, exact quote).
     Conversely, calls `B11` (talk time 26s) and `B14` (talk time 9s) are labelled `is_connected: true`, yet both were unresponsive with zero speech detected.
   - *Where It Affected the Product:*
     - **Screen:** The **Executive Dashboard KPI Grid** separates "Source-Reported Connection Rate" (11/30 = 36.7%) from "Verified Dialogue Rate" (10/10 = 100% of calls with transcripts).
     - **Rule/Output:** Voicemail `C04` is actively routed to `Lead Nurture` rather than discarded as a dropped call.

3. **Finding 3: Commercial Misclassification of Internal Strategic & Vendor Meetings**
   - *Observation:* Meeting `M02` is titled *"LedgerBridge / SpendNest discussion"*, which a naive keyword or calendar parser treats as an outbound customer sales opportunity. The transcript proves SpendNest's strategy and product teams evaluating LedgerBridge as a 3rd-party electronic invoicing API vendor:
     > *"I work on strategy and partnerships at SpendNest. We serve businesses with cards and accounts payable, and we are developing accounts receivable. We want to understand whether LedgerBridge can give us compliant invoicing coverage across our operating markets."* (Meeting `M02`, Turn 1).
     Similarly, `M10` (*"Billing workflow walkthrough"*, Turn 3) is an internal training session on back-office account unfreezing.
   - *Where It Affected the Product:*
     - **Screen:** Filterable under `Internal & Vendor Operations` in the **Inbox & Deep Inspector**.
     - **Rule/Output:** Excluded from the `sales_pipeline` directory and pipeline KPIs in `exports/manifest.json`, preventing false revenue inflation.

---

## Slide 2: Interface Choices & Deliberately Rejected Decision

### Header
**Designing for High-Signal Actionability While Rejecting False Precision**

### 1. Progressive Disclosure Architecture
- **Tier 1 (Executive Overview):** Headline KPIs with explicit formulas, denominators, and a dual-connection rate comparison.
- **Tier 2 (Operational Matrix):** Matrix table isolating Call Representatives (Arun, Meera, Leela, Kiran, Dev) from Meeting Organizers (`team06`–`team14`, `arun@example.com`).
- **Tier 3 (Deep Inspector):** Split-screen layout displaying verifiable intelligence: What Happened, Transcript Quotes, Honest Uncertainty Warnings, and Attributed Next Steps.

### 2. The Deliberately Rejected Decision
- **Alternative Considered:** Building an automated "Pipeline Currency Deal Value" widget and rep revenue quota leaderboard by multiplying conversational figures (e.g. Customer B stating *"Monthly spending might be around INR 10–13 lakh"* in `M03`, or virtual account fees in `M01`).
- **Why It Was Rejected:** 
  The dataset supplies no authoritative CRM opportunity table, win probabilities, or verified credit underwriting. In `M03` (Turn 10), Customer B explicitly cautioned:
  > *"Monthly spending might be around INR 10–13 lakh, but that needs checking. First we need to establish whether the workflow fits."*
  Furthermore, SpendNest domestic cards are prepaid wallets funded by company cash, not corporate credit facilities with interchange revenue guarantees. Calculating an annualized revenue or deal pipeline value from offhand conversational ballpark estimates presents false precision to executive leadership.
- **Accepted Trade-off & Product Result:**
  We omitted synthetic revenue currency totals from the dashboard. Instead, we implemented qualitative **Opportunity Stages**, **Verified Next Steps**, and **Stated Ownership**. Every number presented on screen is auditable to source metadata.

### 3. What Was Deliberately Left Out
- **Generic Word Clouds & Sentiment Gauges:** Unactionable without contextual evidence.
- **Forced Identity Joins:** Refused to merge companies based on similar domain names without explicit proof.
- **Hallucinated Summaries for Silent Records:** Records with no speech (`M05`, `M08`, `M11`, `B01`–`B20`) are marked with an explicit intake status rather than fictional AI summaries.

---

## Slide 3: Routing Architecture & Edge Case Handling

### Header
**Differentiated Operational Taxonomy Preserving Human Judgment**

### 1. Six Differentiated Operational Routes
Rather than generating generic one-size-fits-all summaries, the system routes records to specialized destinations:
1. `Sales Pipeline`: Active evaluations (`M03` Asterloom cards, `C03` Developer API, `M06` Mapletrail branch).
2. `Partnerships & Advisory`: Channel multipliers (`M01` Harborpath US incorporation, `C07` Willowbank virtual accounts).
3. `Customer Success & Support`: Account retention, migration, and bug triage (`M04` Cedarwave, `M07` Willowfield, `M09` Brookmint).
4. `Internal & Vendor Operations`: Vendor procurement and internal training (`M02` LedgerBridge e-invoicing, `M10` Billing walkthrough).
5. `Lead Nurture & Referrals`: Future pipeline and warm referrals (`C05` StoreHarbor, `C08` People Ops, `C09` Rishabh, `C10` Manufacturing).
6. `Triage / Inactive`: Disqualified calls, voicemails, and cancelled calendar slots (`C01` rejected cold call, `C02` gatekeeper, `B01`–`B20`, `M05`, `M08`, `M11`–`M14`).

### 2. Multi-Destination Context Preservation
A conversation often serves more than one purpose. 
- *Example (`M04` Cedarwave Distribution):* Primary route is `Customer Success` (card programme migration to new wallet network), but secondary tag is `Engineering Escalation` because the customer is blocked from reallocating users between departments in the assistant view.
- *Preservation:* Both tags are recorded in `manifest.json`, and cross-functional action items are attributed to distinct owners.

### 3. Difficult Case Walkthrough: M07 (Late-Arriving Transcript & Preserved Judgment)
- In the initial batch (`01_initial.json`), `M07` (*Willowfield Trust*) had `has_transcript: true` but an empty turns array with `unavailable_reason: "Transcript not included in this delivery..."`.
- The manager manually assigns `M07` to `Customer Success` and logs a note.
- When `02_update.json` arrives with revision 2 and 27 turns, the system applies the newer payload without wiping the manager's manual route.
- The analysis status updates to show fresh transcript coverage while keeping the manager's operational judgment intact across application restarts.

---

## Slide 4: Verification of Key Numbers & Analytical Conclusions

### Header
**Mathematical Rigor, Explicit Denominators, and Verifiable Source Citations**

### 1. Invariant Key Numbers Checked Against Source Data

| Headline Metric | Computed Value | Mathematical Denominator & Formula | Source Verification |
|---|---|---|---|
| **Selected Source Records** | **44** | Distinct count of `(source_type, source_id)` | 30 calls + 14 meetings. Exactly 44 records. |
| **Initial Usable Transcript Coverage** | **38.6%** | $17 / 44$ records with non-empty text | 10 calls (`C01`–`C10`) + 7 meetings (`M01`–`M04`, `M06`, `M09`, `M10`). |
| **Post-Update Transcript Coverage** | **40.9%** | $18 / 44$ records with non-empty text | 10 calls + 8 meetings (after `M07` rev 2 update). |
| **Calls Transcript Coverage** | **33.3%** | $10 / 30$ total selected calls | 20 background calls intentionally unrecorded. |
| **Meetings Transcript Coverage** | **57.1%** | $8 / 14$ total selected meetings | 3 empty recordings, 2 bot cancelled, 1 not scheduled. |
| **Source-Reported Connection Rate** | **36.7%** | $11 / 30$ calls where `is_connected == true` | Upstream stored status. Excludes unknown (0). |
| **Verified Dialogue Connect Rate** | **100.0%** | $10 / 10$ calls with supplied transcripts | Substantive human conversation rate on recorded calls. |

### 2. Replay Contract Verification Steps
- **Step 1 (Initial Import):** 44 records loaded, 17 usable transcripts.
- **Step 2 (Repeat Import):** Shuffled order imported again; duplicate count = 0, total records remains 44.
- **Step 3 (Manual Correction):** Route on `M07` changed; saved to persistent storage.
- **Step 4 (Update Batch):** `02_update.json` imported; `M07` updated to rev 2 (27 turns); total records remains 44; usable count becomes 18.
- **Step 5 (Judgment Preservation):** After full page reload, manual route remains in effect.

### 3. Traceability of Analytical Conclusions
Every recommendation in the workspace links directly to a verifiable turn number or quote:
- *Asterloom (`M03`):* Cashflow prepay hurdle cited from **Turn 6** (*"Wait, these are prepaid? ... So we put money in before anyone spends"*).
- *Willowbank (`C07`):* Channel referral viability cited from exact quote (*"Yes, that is something we normally do... message me on our chat app"*).
- *Brookmint (`M09`):* Login failure diagnosed from **Turn 21** (*"It says the token has expired. This is the fresh message we just received"*).

---

## Slide 5: Trade-offs, AI Usage, Known Limitations & Roadmap

### Header
**Transparent Technical Disclosure and Production Roadmap**

### 1. AI Usage & Governance Disclosure
- **Pre-generation vs. Dynamic Execution:**
  - *Dynamic:* Ingestion, deduplication, revision ordering, state persistence, KPI computation, filter indexing, and export manifest generation execute entirely at runtime in the browser.
  - *Pre-generated:* Detailed conversation analyses were extracted and structured using LLM assistance, followed by 100% human audit against source transcripts to guarantee citation fidelity.
- **No Hallucination Policy:** Substantive analysis is strictly withheld for silent or unrecorded records (`B01`–`B20`, `M05`, `M08`, `M11`–`M14`).

### 2. Architecture & Technical Trade-offs Accepted
- **Zero-Dependency Vanilla Web Stack:** Implemented in pure HTML5, CSS3, and ES6 JavaScript. Runs instantly from `file:///` without requiring `node_modules`, build steps, or backend services.
- **Client-Side ZIP Archiving:** Packaged with an in-memory PKZIP Store encoder, allowing reviewers to download the entire structured export archive offline with one click.
- **Date Boundary Scope:** All activity is pinned to 21 August 2026 (Asia/Kolkata), precluding cross-date cohort analysis.

### 3. Known Limitations & What We Would Improve Next
1. **Live Bi-Directional CRM Sync:** In production, route overrides and notes should sync back to Salesforce / HubSpot via REST webhooks.
2. **Audio/Waveform Player:** If upstream media recordings were provided, the transcript reader would include an audio waveform player synced to turn timecodes.
3. **Automated Re-Analysis Trigger:** When a revision arrives (such as `M07` rev 2), trigger an automated background LLM re-run with human approval diff view.
4. **Time Spent:** ~7.5 hours of dedicated engineering, verification, and artifact production.
