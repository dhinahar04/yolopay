# SpendNest — Revenue Intelligence Inbox

A professional, clickable executive workspace transforming fragmented sales calls, meeting recordings, delayed transcripts, and contradictory telephony classifications into actionable revenue intelligence.

---

## 1. Quick Start & How to Run

This application is built with zero runtime dependencies. It can be opened directly in any modern web browser or served locally.

### Option A: Direct Browser Launch (Recommended)
Simply double-click or open `index.html` in Chrome, Safari, Edge, or Firefox:
```bash
open index.html   # On macOS
# or double-click index.html in Finder / File Explorer
```
*Note: All data and assets are self-contained in `data.js` and `app.js` with zero CORS restrictions.*

### Option B: Local HTTP Server (Optional)
```bash
python3 -m http.server 8000
# Open http://localhost:8000 in your browser
```

---

## 2. Reproducing the Replay Contract & Invariant Tests

The system strictly adheres to `DATA_CONTRACT.md`. The public replay suite can be tested via the interactive quickbar at the top of the interface or in the **Replay Suite & Audit** tab:

| Step | Action in UI | Expected Behavioral Invariant |
|---|---|---|
| **1. Initial Import** | Click `1. Initial Batch (v1)` | Ingests `data/01_initial.json`. Exactly 44 distinct records keyed by `(source_type, source_id)`. Usable supplied text count = 17. |
| **2. Repeat Import** | Click `2. Re-import (Dedup Check)` | Re-imports `01_initial.json` with records shuffled. Total record count remains **44** (0 duplicates created, zero count inflation). |
| **3. Manual Correction** | Click `3. Override Route (M07)` (or change route via dropdown) | Manually change `M07` to `Customer Success`. The override is saved in persistent storage. |
| **4. Update Batch** | Click `4. Update Batch (M07 v2)` | Ingests `data/02_update.json` (Rev 2). `M07` turns increase from 0 to 27. Total records remains **44**. Usable transcripts increases from 17 to **18**. |
| **5. Preserve Judgment** | Click `5. Verify State` (or refresh browser page) | Simulates application restart. The manual route override on `M07` remains active, and newer text remains inspectable. |

---

## 3. The Three Most Important Findings

### Finding 1: Metadata vs. Spoken Identity Discrepancy & Dialer Account Sharing
- **Source Evidence:** Call `C06` database payload lists `rep_name: "Meera"`, but the caller explicitly introduces himself on the audio transcript:
  > *"Hello? Good evening, Mr Nikhil. Good evening. Ravi here. I'll say at the start that this is a cold call."* (Call `C06`, exact quote).
- **Product Impact:** 
  - Alerted in the **Executive Dashboard Exception Notice** and on the **C06 Deep Inspector View** with a `Metadata Discrepancy` badge.
  - Attributed to *"Meera (Spoken: Ravi)"* in `exports/manifest.json` and highlighted in `exports/manager_brief_2026-08-21.md` under "Rep Attribution Audit" so management does not improperly assign coaching feedback or quota credits to Meera.

### Finding 2: False Positive & Inverted Upstream Telephony Connection Flags
- **Source Evidence:** Upstream machine flags contradict reality. Call `C04` is labelled `is_connected: false` and `is_conversation: false`, yet Arun delivered a complete, substantive 95-second voicemail addressing a misdirected proposal:
  > *"Hello, this is a message for Ritesh. Arun from SpendNest here. I'm following up on your consideration of our expense platform for Lanternpath Media. My understanding is that our information first went to the wrong email address..."* (Call `C04`, exact quote).
  Conversely, calls `B11` (talk time 26s) and `B14` (talk time 9s) are labelled `is_connected: true`, yet both were unresponsive with zero speech detected.
- **Product Impact:**
  - The **Executive Dashboard KPI Grid** separates "Source-Reported Connection Rate" (11/30 = 36.7%) from "Verified Dialogue Rate" (10/10 = 100% of calls with transcripts).
  - Voicemail `C04` is actively routed to `Lead Nurture` rather than discarded as a dropped call.

### Finding 3: Commercial Misclassification of Internal Strategic & Vendor Meetings
- **Source Evidence:** Meeting `M02` is titled *"LedgerBridge / SpendNest discussion"*, which a naive keyword or calendar parser treats as an outbound customer sales opportunity. The transcript proves SpendNest's strategy and product teams evaluating LedgerBridge as a 3rd-party electronic invoicing API vendor:
  > *"I work on strategy and partnerships at SpendNest. We serve businesses with cards and accounts payable, and we are developing accounts receivable. We want to understand whether LedgerBridge can give us compliant invoicing coverage across our operating markets."* (Meeting `M02`, Turn 1).
  Similarly, `M10` (*"Billing workflow walkthrough"*, Turn 3) is an internal training session on back-office account unfreezing.
- **Product Impact:**
  - Routed to `Internal & Vendor Operations` in the **Inbox & Deep Inspector**.
  - Excluded from the `sales_pipeline` directory and pipeline KPIs in `exports/manifest.json`, preventing false revenue inflation.

---

## 4. The One Deliberately Rejected Decision

- **Alternative Considered:** Synthesizing an automated "Pipeline Currency Deal Value" widget and rep revenue quota leaderboard by multiplying conversational figures (e.g. Customer B stating *"Monthly spending might be around INR 10–13 lakh"* in `M03`, or virtual account fees in `M01`).
- **Why It Was Rejected:** 
  The dataset supplies no authoritative CRM opportunity table, win probabilities, or verified credit underwriting. In `M03` (Turn 10), Customer B explicitly cautioned:
  > *"Monthly spending might be around INR 10–13 lakh, but that needs checking. First we need to establish whether the workflow fits."*
  Furthermore, SpendNest domestic cards are prepaid wallets funded by company cash, not corporate credit facilities with interchange revenue guarantees. Calculating an annualized revenue or deal pipeline value from offhand conversational ballpark estimates presents false precision to executive leadership.
- **Accepted Trade-off & Product Result:**
  We omitted synthetic revenue currency totals from the dashboard. Instead, we implemented qualitative **Opportunity Stages**, **Verified Next Steps**, and **Stated Ownership**. Every number presented on screen is auditable to source metadata.

---

## 5. Metric Definitions & Mathematical Denominators

All activity falls on **21 August 2026** in **Asia/Kolkata** (calls use `started_at`, meetings use `starts_at`).

| Metric Name | Value | Exact Mathematical Formula & Denominator | Meaning & Integrity Note |
|---|---|---|---|
| **Selected Activity** | **44** | Distinct count of `(source_type, source_id)` | 30 calls + 14 meetings. Selected sample, not full team history. |
| **Usable Transcript Coverage** | **38.6%** $\rightarrow$ **40.9%** | Records with non-empty text / 44 total records | 17 initially (`C01`–`C10` calls + `M01`–`M04`, `M06`, `M09`, `M10` meetings); 18 post-update (`M07` rev 2). |
| **Calls Transcript Coverage** | **33.3%** | 10 calls with transcript / 30 total calls | 20 background calls intentionally unrecorded. |
| **Meetings Transcript Coverage**| **50.0%** $\rightarrow$ **57.1%** | 7 (then 8) meetings with $\ge 1$ turns / 14 meetings | 3 empty recordings, 2 bot cancelled, 1 not scheduled. |
| **Source Reported Connect Rate**| **36.7%** | Calls with `is_connected == true` / 30 calls | Upstream telephony classification. Inaccurate on voicemails (`C04`) and silent calls (`B11`, `B14`). |
| **Verified Dialogue Connect Rate**| **100.0%** | Calls with dialogue / 10 calls with transcript | Verified human conversation rate over recorded attempts. |

---

## 6. Where Generated Outputs Are Written

All generated files reside in `exports/` and can be downloaded as a ZIP directly from the web app:

```
exports/
├── manifest.json                                      # Machine-readable delivery manifest (JSON)
├── manifest.csv                                       # Machine-readable delivery manifest (CSV)
├── manager_brief_2026-08-21.md                        # Executive Daily Brief for 21 August 2026
├── sales_pipeline/
│   ├── C03_developer_api_&_webhook_follow_up.md
│   ├── M03_asterloom_systems_corporate_cards_&.md
│   └── M06_mapletrail_services_branch_expense_.md
├── partnerships_advisory/
│   ├── C07_willowbank_advisory_channel_partner.md
│   └── M01_harborpath_advisory___spendnest_dis.md
├── customer_success/
│   ├── M04_cedarwave_distribution_card_migrati.md
│   ├── M07_willowfield_trust_bug_triage_(late_.md
│   └── M09_brookmint_holdings_account_setup_&_.md
├── internal_vendor/
│   ├── M02_ledgerbridge___spendnest_technical_.md
│   └── M10_internal_billing_workflow_&_unfreez.md
├── lead_nurture/
│   ├── C04_lanternpath_media_voicemail.md
│   ├── C05_multi_store_retail_pitch_(storeharb.md
│   ├── C08_people_ops_referral_outreach.md
│   ├── C09_130_location_retail_referral_to_bus.md
│   └── C10_manufacturing_lead___ex_meadowbrick.md
└── triage_inactive/
    ├── C01_harborlight_advisory_outreach.md
    ├── C02_fernhaven_group_reception_transfer.md
    ├── C06_120+_store_retail_outreach_(identit.md
    ├── background_calls_B01_B20.md                    # 20 background calls triage
    └── silent_cancelled_meetings_M05_M08_M11_M12_M13_M14.md # 6 inactive meetings triage
```

---

## 7. Submission Artifacts & Disclosure

- **Working Application:** `index.html` (Complete offline-capable web application).
- **Original Reading Pack:** `reader.html` (Preserved intact for reviewer convenience).
- **Interactive Slides Viewer:** `slides.html` (Printable to PDF via Ctrl/Cmd + P).
- **Markdown Slides:** `SLIDES.md` (Five complete presentation slides).
- **Screen Recording Script:** `RECORDING_SCRIPT.md` (Timed 3-minute narration script).
- **AI Usage:** AI was utilized to extract, cross-verify, and format conversational evidence, turning points, and coaching points. All outputs were subsequently audited against verbatim source turns to ensure zero hallucination. Ingestion, deduplication, revision ordering, state persistence, KPI computation, filter indexing, and export manifest generation run dynamically in the client/runtime.
- **Time Spent:** ~7.5 hours of dedicated design, engineering, verification, and artifact production.
- **Known Limitations:** Single shifted date extract; no live CRM bi-directional webhook sync.
# yolopay
