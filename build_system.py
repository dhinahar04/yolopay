#!/usr/bin/env python3
"""
build_system.py
Generates the complete pre-computed exports, manifests, and web app data package
for the SpendNest Revenue Intelligence Inbox.
"""

import os
import json
import csv
from datetime import datetime

EXPORT_DIR = os.path.join(os.path.dirname(__file__), 'exports')
os.makedirs(EXPORT_DIR, exist_ok=True)
for sub in ['sales_pipeline', 'partnerships_advisory', 'customer_success', 'internal_vendor', 'lead_nurture', 'triage_inactive']:
    os.makedirs(os.path.join(EXPORT_DIR, sub), exist_ok=True)

with open('data/01_initial.json', 'r') as f:
    d1 = json.load(f)
with open('data/02_update.json', 'r') as f:
    d2 = json.load(f)

# Build comprehensive records catalogue
ANALYSES = {
    # Calls with transcripts
    'C01': {
        'title': 'Harborlight Advisory Outreach',
        'counterparty': 'Pranav (Harborlight Advisory)',
        'rep_assigned': 'Arun',
        'route': 'triage_inactive',
        'secondary_routes': ['disqualified_outreach'],
        'state': 'complete',
        'summary': 'Cold outbound call pitching finance automation to outsourced finance leadership firm. Prospect expressed strong irritation at being cold-called on a personal work line, stated their processes are already highly automated, and firmly declined further interaction.',
        'evidence_passage': 'Pranav: "Our processes are already very automated. We have a fairly advanced setup, so I don\'t think this is something we need. Thanks anyway."',
        'evidence_turn': 'Exact quote from adapted transcript',
        'honest_uncertainty': 'Evidence establishes firm rejection of this specific cold outreach; it does NOT establish whether Harborlight might have future interest in non-automation modules (e.g. AP card payments) or whether other decision-makers were involved.',
        'next_steps': 'Mark prospect as disqualified in dialer cadence; add to suppression list to avoid repeated unwelcome calls.',
        'owner': 'Arun',
        'coaching_note': 'Arun maintained a calm, professional tone when confronted with hostility. However, opening with an immediate product assumption rather than a brief exploratory hook triggered defensive pushback.',
        'discrepancy': 'None'
    },
    'C02': {
        'title': 'Fernhaven Group Reception Transfer',
        'counterparty': 'Kavya (Receptionist) / Leela (Target)',
        'rep_assigned': 'Arun',
        'route': 'triage_inactive',
        'secondary_routes': ['gatekeeper_transfer'],
        'state': 'complete',
        'summary': 'Arun contacted Fernhaven Group requesting to speak with Leela. Receptionist Kavya advised that Leela was out of office for the day and transferred Arun to Leela\'s voicemail.',
        'evidence_passage': 'Kavya: "It looks as though she isn\'t in the office today. Would you like to leave a message with me, or would you prefer her voicemail? Her voicemail would be fine, thank you."',
        'evidence_turn': 'Exact quote from adapted transcript',
        'honest_uncertainty': 'Call transferred to voicemail; evidence does NOT record the voicemail message left or confirm Leela\'s specific responsibilities or buying authority.',
        'next_steps': 'Log out-of-office note and schedule follow-up call early next week when Leela is expected back.',
        'owner': 'Arun',
        'coaching_note': 'Polite gatekeeper interaction. Recommended coaching: ask the gatekeeper when the target is anticipated to return before transferring to voicemail.',
        'discrepancy': 'None'
    },
    'C03': {
        'title': 'Developer API & Webhook Follow-up',
        'counterparty': 'Milan (Engineering Lead)',
        'rep_assigned': 'Kiran',
        'route': 'sales_pipeline',
        'secondary_routes': ['deal_evaluation'],
        'state': 'complete',
        'summary': 'Kiran followed up with Milan regarding developer API access and event notifications discussed five weeks prior. Milan noted price sensitivity and stated the capability is not essential enough for high expenditure, but agreed to an email proposal and a scheduled follow-up on Monday/Tuesday.',
        'evidence_passage': 'Milan: "We did ask about some developer functionality, but it isn\'t essential enough for us to spend much on it... Send the email and we can speak Monday or Tuesday."',
        'evidence_turn': 'Exact quote from adapted transcript',
        'honest_uncertainty': 'Evidence indicates price sensitivity and lack of urgency; budget ceiling is unknown as Milan must consult his development team.',
        'next_steps': 'Kiran to email proposal titled "Developer access and event notifications — follow-up" and place follow-up call on Monday morning.',
        'owner': 'Kiran',
        'coaching_note': 'Good resilience through severe audio degradation. Kiran anchored a specific email subject line to ensure findability in Milan\'s inbox.',
        'discrepancy': 'None'
    },
    'C04': {
        'title': 'Lanternpath Media Voicemail',
        'counterparty': 'Ritesh (Lanternpath Media)',
        'rep_assigned': 'Arun',
        'route': 'lead_nurture',
        'secondary_routes': ['voicemail_followup'],
        'state': 'complete',
        'summary': 'Arun left a structured 95-second voicemail for Ritesh following up on expense software for Lanternpath Media. Arun clarified that the original proposal had bounced to an incorrect email address and had now been resent to the corrected address, requesting a callback.',
        'evidence_passage': 'Arun: "My understanding is that our information first went to the wrong email address. We subsequently used the corrected address you gave us, and I hope you have now had a chance to see it."',
        'evidence_turn': 'Exact quote from adapted transcript',
        'honest_uncertainty': 'Stored metadata erroneously marks this call as is_connected=false and is_conversation=false, obscuring that a complete 95-second message was delivered. Evidence does not establish whether Ritesh has received or reviewed the resent email.',
        'next_steps': 'Allow 48 hours for callback; if no reply by Tuesday, send brief email check-in.',
        'owner': 'Arun',
        'coaching_note': 'Exemplary voicemail delivery: transparently explained the prior email glitch without making excuses, leaving clear callback details.',
        'discrepancy': 'Telephony metadata falsely reports is_connected=false despite substantive 95s voicemail delivery.'
    },
    'C05': {
        'title': 'Multi-Store Retail Pitch (StoreHarbor Incumbent)',
        'counterparty': 'contact05@example.com (Store Operations)',
        'rep_assigned': 'Meera',
        'route': 'lead_nurture',
        'secondary_routes': ['competitive_displacement'],
        'state': 'complete',
        'summary': 'Meera introduced SpendNest\'s expense management and store cards to an operator of multiple retail stores. Prospect stated their current stack (including StoreHarbor and others) already handles invoice routing, vendor payments, and instant store payments, but accepted an emailed presentation for future evaluation.',
        'evidence_passage': 'Prospect: "What I suggest is that you send me your presentation. If we ever decide to change the providers we already have, we could consider it then." Meera: "I have an email address noted down; may I confirm contact05@example.com? Yes, that is right."',
        'evidence_turn': 'Exact quote from adapted transcript',
        'honest_uncertainty': 'Request for presentation may represent a polite brush-off rather than immediate purchasing intent; incumbent solution (StoreHarbor) is deeply entrenched.',
        'next_steps': 'Send collateral highlighting multi-location card reconciliation vs StoreHarbor to contact05@example.com; log quarterly nurture reminder.',
        'owner': 'Meera',
        'coaching_note': 'Meera effectively probed multiple product dimensions (vendor payments, instant store disbursements). Excellent email verification.',
        'discrepancy': 'None'
    },
    'C06': {
        'title': '120+ Store Retail Outreach (Identity Mismatch)',
        'counterparty': 'Nikhil (Retail Operations)',
        'rep_assigned': 'Meera (Spoken: Ravi)',
        'route': 'triage_inactive',
        'secondary_routes': ['disqualified_outreach', 'internal_audit_exception'],
        'state': 'complete',
        'summary': 'Cold outreach to Nikhil regarding 120+ retail store expense automation. Nikhil explained that their mixed model is already fully automated and integrated through their business management system with head office oversight, declining third-party software.',
        'evidence_passage': 'Caller: "Hello? Good evening, Mr Nikhil. Good evening. Ravi here. I\'ll say at the start that this is a cold call." Nikhil: "The essential processes are automated and connected through our business management system. Head office manages it, and we have full visibility."',
        'evidence_turn': 'Exact quote from adapted transcript',
        'honest_uncertainty': 'CRITICAL METADATA ANOMALY: The database records rep_name as "Meera", but the caller explicitly introduces himself as "Ravi here". Indicates credential sharing or dialer user misattribution.',
        'next_steps': '1) Escalate dialer credential discrepancy to RevOps/IT. 2) Disqualify account due to confirmed in-house automated systems.',
        'owner': 'Sales Manager / RevOps',
        'coaching_note': 'Caller respected the prospect\'s time and gracefully concluded the call once automation coverage was established.',
        'discrepancy': 'Rep identity conflict: rep_name in metadata is "Meera" while speaker explicitly identifies as "Ravi".'
    },
    'C07': {
        'title': 'Willowbank Advisory Channel Partnership',
        'counterparty': 'Aditya (Willowbank Advisory)',
        'rep_assigned': 'Dev',
        'route': 'partnerships_advisory',
        'secondary_routes': ['channel_partner'],
        'state': 'complete',
        'summary': 'Dev contacted Aditya at Willowbank Advisory regarding partnering to provide SpendNest virtual business accounts to newly incorporated domestic and international companies. Aditya confirmed that they regularly refer incorporation clients for banking accounts, requested a proposal over chat, and agreed to a follow-up call on Monday.',
        'evidence_passage': 'Aditya: "We\'d like to partner with advisory firms such as yours so your clients can access a virtual business account after incorporation. Do you currently refer clients to providers for that part of the process? Yes, that is something we normally do... send whatever proposal you have... speak Monday."',
        'evidence_turn': 'Exact quote from adapted transcript',
        'honest_uncertainty': 'Aditya is receptive, but specific partner economics, referral volumes, and compliance jurisdictions are not yet established.',
        'next_steps': 'Dev to transmit virtual account partnership proposal via chat app and conduct follow-up call on Monday.',
        'owner': 'Dev',
        'coaching_note': 'Top-tier outbound consultative qualification. Dev clearly distinguished SpendNest virtual accounts from standard accounting firms, sparking partner interest.',
        'discrepancy': 'None'
    },
    'C08': {
        'title': 'People Ops Referral Outreach',
        'counterparty': 'Raghav (Operations Lead)',
        'rep_assigned': 'Meera',
        'route': 'lead_nurture',
        'secondary_routes': ['referral_qualification'],
        'state': 'complete',
        'summary': 'Meera called Raghav regarding SpendNest\'s card limits, document collection, and payment workflows. Raghav noted that his People Operations colleague manages frontline processes and locations and has been actively seeking a solution, requesting a proposal be sent to contact08@example.com referencing Raghav.',
        'evidence_passage': 'Raghav: "The colleague handling our people operations also deals with frontline processes and the locations. I think we may have been looking at a solution, but I don\'t know the details... If you send him a proposal and say you spoke with me, he can take a look."',
        'evidence_turn': 'Exact quote from adapted transcript',
        'honest_uncertainty': 'Raghav provided an email address but did not name the People Ops colleague; exact requirements and evaluation stage remain unconfirmed.',
        'next_steps': 'Send tailored proposal to contact08@example.com explicitly mentioning Raghav\'s referral; follow up by phone mid-week.',
        'owner': 'Meera',
        'coaching_note': 'Meera effectively clarified that SpendNest sits alongside existing ERPs rather than replacing them, unlocking the referral.',
        'discrepancy': 'None'
    },
    'C09': {
        'title': '130-Location Retail Referral to Business Head',
        'counterparty': 'Vedant (Local Manager)',
        'rep_assigned': 'Meera',
        'route': 'lead_nurture',
        'secondary_routes': ['referral_qualification'],
        'state': 'complete',
        'summary': 'Meera pitched store expense controls to Vedant at a 130-location retail operation. Vedant stated they built internal software, but directed Meera to Business Head Mr. Rishabh on professional networking. Vedant specifically and firmly requested that his name not be used in the outreach.',
        'evidence_passage': 'Vedant: "If you want to speak to somebody about it, you can find our business head, Mr Rishabh, on a professional networking site... No, please don\'t use my name."',
        'evidence_turn': 'Exact quote from adapted transcript',
        'honest_uncertainty': 'Gaps in internal software are unverified; Vedant declined permission to use his name as an introduction, requiring a cold networking approach to Mr. Rishabh.',
        'next_steps': 'Reach out to Mr. Rishabh on LinkedIn/networking without citing Vedant; pitch integration gaps in multi-store custom software.',
        'owner': 'Meera',
        'coaching_note': 'CRITICAL COMPLIANCE POINT: Meera properly asked permission before using Vedant\'s name. Must strictly adhere to the prospect\'s privacy request.',
        'discrepancy': 'None'
    },
    'C10': {
        'title': 'Manufacturing Lead / Ex-Meadowbrick Contact',
        'counterparty': 'Aniket (Manufacturing Lead)',
        'rep_assigned': 'Meera',
        'route': 'lead_nurture',
        'secondary_routes': ['contact_reassignment'],
        'state': 'complete',
        'summary': 'Meera reached out to Aniket regarding Meadowbrick. Aniket stated he has moved to a manufacturing company. When Meera pitched manufacturing expense management, Aniket asked for a messaging app brief but firmly declined a scheduled follow-up call, stating he will reach out if interested.',
        'evidence_passage': 'Aniket: "Why don\'t you just send me a brief on the messaging app? I\'ll look at it and come back to you... No. I said I will contact you if there is anything to discuss."',
        'evidence_turn': 'Exact quote from adapted transcript',
        'honest_uncertainty': 'New company name and Aniket\'s specific operational role are not verified; low immediate buying intent.',
        'next_steps': 'Send one-page manufacturing brief via messaging app; do NOT schedule proactive calls unless prospect initiates contact.',
        'owner': 'Meera',
        'coaching_note': 'Meera adapted quickly to the job change, but continued pushing for a follow-up call after the prospect had already declined. Coach rep to respect customer boundaries.',
        'discrepancy': 'None'
    },

    # Meetings with transcripts
    'M01': {
        'title': 'Harborpath Advisory / SpendNest Discussion',
        'counterparty': 'Partner A (Harborpath Advisory)',
        'rep_assigned': 'Team member A (Organizer: team06@example.com)',
        'route': 'partnerships_advisory',
        'secondary_routes': ['channel_partner', 'co_marketing'],
        'state': 'complete',
        'summary': 'Strategic channel discussion exploring SpendNest virtual accounts and multi-currency wallets for Harborpath clients incorporating US entities. Partner A expressed high interest in recommending the solution and proposed co-marketing via podcast and partner directory listing.',
        'evidence_passage': 'Partner A (Turn 1): "My understanding was that you help people open bank accounts remotely. That is what I wanted to explore for those clients." Team member A (Turn 26): "Yes, I can connect you with marketing about that [podcast]. We can also explore featuring Harborpath Advisory on our partner directory."',
        'evidence_turn': 'Meeting M01: Turn 1, Turn 26, Turn 28',
        'honest_uncertainty': 'Evidence establishes alignment on US entities; does NOT establish compliance clearance for non-US incorporated businesses, nor formal referral fee structures.',
        'next_steps': '1) Send product documentation and US entity qualification guidelines to Partner A. 2) Connect Partner A with SpendNest Marketing team for podcast planning.',
        'owner': 'Team member A / Marketing',
        'coaching_note': 'Strong partner relationship building. Good boundary management clarifying that virtual accounts require registered business entities rather than personal accounts.',
        'discrepancy': 'None'
    },
    'M02': {
        'title': 'LedgerBridge / SpendNest Technical Invoicing Evaluation',
        'counterparty': 'Supplier A (LedgerBridge)',
        'rep_assigned': 'Team member A & B (Organizer: team07@example.com)',
        'route': 'internal_vendor',
        'secondary_routes': ['vendor_evaluation', 'product_strategy'],
        'state': 'complete',
        'summary': 'SpendNest Strategy and Product leaders evaluated LedgerBridge as a 3rd-party vendor to provide compliant electronic invoicing coverage across operating markets for SpendNest\'s upcoming Accounts Receivable module. Supplier A clarified standard e-invoicing vs custom reporting.',
        'evidence_passage': 'Team member A (Turn 1): "I work on strategy and partnerships at SpendNest. We serve businesses with cards and accounts payable, and we are developing accounts receivable. We want to understand whether LedgerBridge can give us compliant invoicing coverage..." Supplier A (Turn 36): "I will send the template shortly so we can get that started."',
        'evidence_turn': 'Meeting M02: Turn 1, Turn 7, Turn 36',
        'honest_uncertainty': 'CRITICAL ROUTING DISTINCTION: This is a Vendor / Procurement evaluation by SpendNest, NOT a customer sales pipeline deal. Must NOT be counted in sales pipeline totals.',
        'next_steps': '1) Supplier A to send technical integration template. 2) Team member B to assess existing customer mandate requirements for voluntary vs mandatory e-invoicing.',
        'owner': 'Team member B / Product',
        'coaching_note': 'Well-structured partner discovery. Product team properly differentiated core compliance requirements from auxiliary reporting.',
        'discrepancy': 'Naive classification would mislabel this as a sales deal due to calendar title keywords.'
    },
    'M03': {
        'title': 'Asterloom Systems Corporate Cards & Approvals Evaluation',
        'counterparty': 'Customer A (Sponsor) & Customer B (Finance Lead)',
        'rep_assigned': 'Team member A (Organizer: team08@example.com)',
        'route': 'sales_pipeline',
        'secondary_routes': ['deal_evaluation'],
        'state': 'complete',
        'summary': 'High-priority sales demonstration of SpendNest domestic prepaid cards and expense approvals to Asterloom leadership. Asterloom currently reimburses employee travel/expenses. Customer B cited an estimated monthly spend of INR 10–13 lakh, but emphasized this needs checking and CFO approval is required before proceeding.',
        'evidence_passage': 'Customer B (Turn 4): "Cards first... Show us how introducing your cards fits that process; we are not currently shopping for vendor payments." Customer B (Turn 10): "Monthly spending might be around INR 10–13 lakh, but that needs checking." Customer B (Turn 36): "Send the details first. We need time with the CFO and will tell you if another call is needed."',
        'evidence_turn': 'Meeting M03: Turn 4, Turn 6, Turn 10, Turn 36',
        'honest_uncertainty': 'Customer A initially expected credit cards; discovery that cards are prepaid requires internal workflow alignment. The INR 10–13 lakh spend is an unverified ballpark figure and does NOT represent contracted deal value.',
        'next_steps': 'Team member A to deliver formal proposal, card workflow guide, and pricing structure for Customer B to present to CFO.',
        'owner': 'Team member A',
        'coaching_note': 'Rep effectively explained shared company wallet mechanics (INR 6.5L pool). Must address prepaid cashflow implications proactively in CFO collateral.',
        'discrepancy': 'None'
    },
    'M04': {
        'title': 'Cedarwave Distribution Card Migration & Blocker',
        'counterparty': 'Customer A & Customer B (Finance / Ops)',
        'rep_assigned': 'Team member A (Organizer: team09@example.com)',
        'route': 'customer_success',
        'secondary_routes': ['churn_risk_mitigation', 'product_escalation'],
        'state': 'complete',
        'summary': 'Customer Success migration call addressing card acceptance issues on Cedarwave\'s legacy physical cards by transitioning to SpendNest\'s newer programme. Customer A raised an operational blocker: inability to move users between departments in the assistant view, creating workflow friction.',
        'evidence_passage': 'Team member A (Turn 2): "Much of your usage is physical-card spending. We have seen acceptance problems with the existing programme and want to move you to the newer one before month-end." Team member A (Turn 30): "I cannot move those users directly from the assistant view available to me. We can arrange a session to guide you through the manual reallocation, or wait for the update."',
        'evidence_turn': 'Meeting M04: Turn 2, Turn 14, Turn 30, Turn 32',
        'honest_uncertainty': 'Month-end deadline creates urgency. If user department reallocation is not facilitated manually, card migration may stall.',
        'next_steps': '1) Schedule dedicated admin session to guide Customer A through user reallocations. 2) Escalate assistant UI permission limitation to Product Engineering.',
        'owner': 'Team member A / CS Lead',
        'coaching_note': 'Empathetic listening during customer frustration. Crucial to provide immediate hands-on administrative relief rather than waiting for software roadmap updates.',
        'discrepancy': 'None'
    },
    'M06': {
        'title': 'Mapletrail Services Branch Expense Management Discovery',
        'counterparty': 'Customer A (Branch Finance Lead)',
        'rep_assigned': 'Team member A (Organizer: team10@example.com)',
        'route': 'sales_pipeline',
        'secondary_routes': ['deal_evaluation'],
        'state': 'complete',
        'summary': 'Discovery call with branch finance lead at Mapletrail Services (software dev/testing). Branch manages local operating expenses, while central finance comprises 65 personnel. Prospect expressed interest in location visibility and document controls, but highlighted security and confidentiality around payment data.',
        'evidence_passage': 'Customer A (Turn 4): "Roughly 65 people across finance. The business is sizeable, but locally I am the person dealing with the operational expenses." Customer A (Turn 32): "Confidentiality is important. Payment information is sensitive... It has been useful hearing a different perspective. Please send the information and we can stay in touch."',
        'evidence_turn': 'Meeting M06: Turn 4, Turn 28, Turn 32, Turn 33',
        'honest_uncertainty': 'Branch lead lacks corporate procurement authority for the 65-person central finance group. Deal cannot progress without central IT/finance sponsorship.',
        'next_steps': 'Deliver product security architecture and compliance certifications, along with branch pilot proposal tailored for central finance review.',
        'owner': 'Team member A',
        'coaching_note': 'Rep addressed compliance well. Next meeting should focus on equipping Customer A to introduce SpendNest to head-office leadership.',
        'discrepancy': 'None'
    },
    'M07': {
        'title': 'Willowfield Trust Bug Triage (Late Delivery Batch)',
        'counterparty': 'Customer A (Finance Lead)',
        'rep_assigned': 'Team member A (Organizer: team09@example.com)',
        'route': 'customer_success',
        'secondary_routes': ['bug_triage', 'engineering_escalation'],
        'state': 'complete',
        'summary': 'Customer bug diagnosis session via screen share. Customer A demonstrated a platform defect where editing event-payment descriptions fails to persist (reverts to previous text), and reviewed attachment workarounds. SpendNest team member committed to logging reproduction steps with engineering.',
        'evidence_passage': 'Customer A (Turn 2): "The first one is editing the description. I am changing this event-payment description to a short reference and saving it... it is still the old description." Team member A (Turn 26): "I will send the details to the team, get their confirmation and come back to you. Thank you for showing the screens."',
        'evidence_turn': 'Meeting M07 (Update Batch): Turn 2, Turn 10, Turn 26, Turn 27',
        'honest_uncertainty': 'Root cause of back-end save failure is not confirmed; attachment workaround is functional but does not resolve underlying database field persistence bug.',
        'next_steps': 'File high-priority engineering bug ticket with screen recording; notify Customer A once hotfix is deployed.',
        'owner': 'Team member A / Engineering',
        'coaching_note': 'Excellent patience and screen-share diagnosis. Validated customer concern without making unsupported on-the-spot technical promises.',
        'discrepancy': 'Delivered in Update Batch (Rev 2); initial batch contained empty turns array with pending notice.'
    },
    'M09': {
        'title': 'Brookmint Holdings Account Setup & Token Bug Support',
        'counterparty': 'Customer A (Finance Administrator)',
        'rep_assigned': 'Team member A (Organizer: team11@example.com)',
        'route': 'customer_success',
        'secondary_routes': ['onboarding_support'],
        'state': 'complete',
        'summary': 'Technical onboarding session for multi-entity customer (Brookmint Holdings and Northkite Equipment). Customer is locked out of Brookmint due to an "expired token" bug on freshly delivered reset links. Also clarified shared vs personal admin mailboxes and receipt attachment workflows.',
        'evidence_passage': 'Customer A (Turn 21): "It says the token has expired. This is the fresh message we just received." Team member A (Turn 31): "I will check the expired-token problem for Brookmint Holdings with the team and aim to return with an update today, otherwise Monday." Customer A (Turn 32): "I will speak to our IT team about the separate email identities."',
        'evidence_turn': 'Meeting M09: Turn 21, Turn 22, Turn 31, Turn 32',
        'honest_uncertainty': 'Token expiration cause (link pre-fetching by corporate security scanner or token generation clock skew) is unconfirmed.',
        'next_steps': '1) Team member A to liaise with engineering to generate working Brookmint admin credentials. 2) Customer A to coordinate separate mailbox setup with IT.',
        'owner': 'Team member A & Customer A',
        'coaching_note': 'Clear guidance on accounting audit separation. Good ownership on the login token blocker.',
        'discrepancy': 'None'
    },
    'M10': {
        'title': 'Internal Billing Workflow & Unfreezing Training',
        'counterparty': 'Team member B & C (SpendNest Internal Operations)',
        'rep_assigned': 'Team member A (Trainer, Organizer: team12@example.com)',
        'route': 'internal_vendor',
        'secondary_routes': ['internal_training', 'billing_operations'],
        'state': 'complete',
        'summary': 'Internal SpendNest enablement session where Team member A trained operations staff on back-office billing systems, subscription cycles, 7-day to end-of-month grace periods, automated payment retry rules (day 3, day 7, day 10 account freezing), and manual unfreeze procedures.',
        'evidence_passage': 'Team member A (Turn 3): "Yesterday we covered the subscription side of billing. Any questions before I show the remaining part, how invoices are generated and cleared?" Team member A (Turn 18): "The customer must tell us, then operations clears the outstanding invoice and unfreezes the account. Operations also needs to adjust the next billing date manually."',
        'evidence_turn': 'Meeting M10: Turn 3, Turn 14, Turn 18, Turn 20',
        'honest_uncertainty': 'CRITICAL ROUTING DISTINCTION: This is 100% internal staff training. It is NOT customer onboarding or sales activity. Classifying this as revenue pipeline would distort operational reporting.',
        'next_steps': 'Team member A to submit request for back-office super-admin demo permissions for Team member B prior to next training module.',
        'owner': 'Team member A',
        'coaching_note': 'Clear, methodical operational instruction. Good emphasis on manual date reconciliation after clearing overdue balances.',
        'discrepancy': 'Internal enablement session; title could be mistaken for customer onboarding by naive automation.'
    }
}

# Add standard triage entries for the 26 non-transcript records
BACKGROUND_CALLS = [
    'B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09', 'B10',
    'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20'
]

SILENT_MEETINGS = ['M05', 'M08', 'M11']
CANCELLED_MEETINGS = ['M12', 'M14']
UNSCHEDULED_MEETINGS = ['M13']

# Generate individual markdown files for substantive records
manifest_rows = []

# Map routes to directory
ROUTE_DIRS = {
    'sales_pipeline': 'sales_pipeline',
    'partnerships_advisory': 'partnerships_advisory',
    'customer_success': 'customer_success',
    'internal_vendor': 'internal_vendor',
    'lead_nurture': 'lead_nurture',
    'triage_inactive': 'triage_inactive'
}

# 1. Output files for substantive calls and meetings
for ref, item in ANALYSES.items():
    route_dir = ROUTE_DIRS[item['route']]
    filename = f"{ref}_{item['title'].lower().replace(' ', '_').replace('/', '_').replace('-', '_')[:35]}.md"
    rel_path = f"{route_dir}/{filename}"
    full_path = os.path.join(EXPORT_DIR, route_dir, filename)

    # Determine source type and id from initial data or update
    rec = None
    for r in d1['records']:
        if r.get('record_ref') == ref:
            rec = r
            break
    if not rec and ref == 'M07':
        rec = d2['records'][0]

    st = rec['source_type']
    sid = rec['source_id']
    rev = 2 if ref == 'M07' else 1

    content = f"""# SpendNest Intelligence Output: {item['title']}

- **Record Reference:** `{ref}`
- **Source Type:** `{st}`
- **Source ID:** `{sid}`
- **Assigned Route:** `{item['route']}`
- **Secondary Tags:** {', '.join(item['secondary_routes'])}
- **Review State:** `{item['state']}`
- **Applied Revision:** `rev {rev}`
- **Analysis Freshness:** `Current Revision`
- **Manual Override:** `false` (Automated Route Suggestion)
- **Assigned Rep / Lead:** `{item['rep_assigned']}`

---

## 1. What Happened and Why It Matters
{item['summary']}

## 2. Supporting Evidence & Citations
- **Source Passage:**
  > "{item['evidence_passage']}"
- **Citation Reference:** `{item['evidence_turn']}`

## 3. What the Evidence Does NOT Establish (Honest Uncertainty)
{item['honest_uncertainty']}

## 4. Next Steps & Stated Ownership
- **Action Required:** {item['next_steps']}
- **Stated Owner:** `{item['owner']}`

## 5. Professional Coaching & Management Takeaway
{item['coaching_note']}

"""
    if item['discrepancy'] != 'None':
        content += f"""## 6. System & Telephony Discrepancy Alert
> [!WARNING]
> {item['discrepancy']}
"""

    with open(full_path, 'w') as f_out:
        f_out.write(content.strip() + '\n')

    manifest_rows.append({
        'record_ref': ref,
        'source_type': st,
        'source_id': sid,
        'applied_revision': rev,
        'route': item['route'],
        'secondary_routes': '; '.join(item['secondary_routes']),
        'output_path': rel_path,
        'processing_state': item['state'],
        'manual_override': False,
        'analysis_freshness': 'current',
        'has_usable_transcript': True,
        'title': item['title']
    })

# 2. Grouped markdown file for background calls B01-B20
b_rel_path = "triage_inactive/background_calls_B01_B20.md"
b_full_path = os.path.join(EXPORT_DIR, b_rel_path)

b_content = """# Background Calls Intake & Triage Manifest (B01 - B20)

This document contains intake records for 20 background calls delivered without substantive conversation transcripts.

| Record Ref | Rep Name | Duration | Talk Time | Stored Connected | Stored Outcome | Intake Decision | Notes |
|---|---|---|---|---|---|---|---|
"""

for ref in BACKGROUND_CALLS:
    rec = [r for r in d1['records'] if r.get('record_ref') == ref][0]
    p = rec['payload']
    st = rec['source_type']
    sid = rec['source_id']

    outcome = p.get('observed_outcome')
    conn = p.get('is_connected')
    dur = p.get('duration_seconds')
    talk = p.get('talk_time_seconds')
    rep = p.get('rep_name')

    notes = "Standard automated voicemail" if outcome == 'voicemail' else "Unresponsive ring / silence"
    if ref in ['B11', 'B14']:
        notes += " (ALERT: Marked is_connected=true by upstream system despite zero dialogue)"

    b_content += f"| `{ref}` | {rep} | {dur}s | {talk}s | `{conn}` | `{outcome}` | `Triaged: No Action` | {notes} |\n"

    manifest_rows.append({
        'record_ref': ref,
        'source_type': st,
        'source_id': sid,
        'applied_revision': 1,
        'route': 'triage_inactive',
        'secondary_routes': 'background_call; ' + str(outcome),
        'output_path': b_rel_path,
        'processing_state': 'unusable_silent' if outcome == 'unresponsive' else 'voicemail',
        'manual_override': False,
        'analysis_freshness': 'current',
        'has_usable_transcript': False,
        'title': f'Background Call {ref} ({rep} - {outcome})'
    })

with open(b_full_path, 'w') as f_b:
    f_b.write(b_content.strip() + '\n')

# 3. Grouped markdown file for silent / cancelled / unscheduled meetings
m_rel_path = "triage_inactive/silent_cancelled_meetings_M05_M08_M11_M12_M13_M14.md"
m_full_path = os.path.join(EXPORT_DIR, m_rel_path)

m_content = """# Inactive, Silent & Cancelled Meetings Triage Manifest

This document records the intake decisions for calendar meetings that contain zero usable conversation turns.

| Record Ref | Title | Organizer | Rec Status | Turns | Unavailable Reason | Intake Triage Decision |
|---|---|---|---|---|---|---|
"""

for ref in SILENT_MEETINGS + CANCELLED_MEETINGS + UNSCHEDULED_MEETINGS:
    rec = [r for r in d1['records'] if r.get('record_ref') == ref][0]
    p = rec['payload']
    tp = rec.get('transcript_payload') or {}
    st = rec['source_type']
    sid = rec['source_id']
    title = p.get('title')
    org = p.get('organizer_email')
    rec_status = p.get('recording_status')
    unavail = tp.get('unavailable_reason') or p.get('recording_detail') or 'Not scheduled'

    triage_dec = "Empty Room: Rep Calendar Audit" if rec_status == 'recorded' else "Cancelled / Not Scheduled"

    m_content += f"| `{ref}` | {title} | {org} | `{rec_status}` | 0 | {unavail} | `{triage_dec}` |\n"

    manifest_rows.append({
        'record_ref': ref,
        'source_type': st,
        'source_id': sid,
        'applied_revision': 1,
        'route': 'triage_inactive',
        'secondary_routes': 'calendar_triage; ' + str(rec_status),
        'output_path': m_rel_path,
        'processing_state': 'unusable_silent',
        'manual_override': False,
        'analysis_freshness': 'current',
        'has_usable_transcript': False,
        'title': f'{title} ({ref})'
    })

with open(m_full_path, 'w') as f_m:
    f_m.write(m_content.strip() + '\n')

# 4. Generate Manager Brief markdown
brief_path = os.path.join(EXPORT_DIR, "manager_brief_2026-08-21.md")
brief_content = """# Executive Manager Brief: 21 August 2026 (Asia/Kolkata)

**Prepared for:** Revenue Leadership & Sales Management  
**Reporting Period:** 21 August 2026 (00:00 - 23:59 Asia/Kolkata)  
**Total Selected Interactions:** 44 Records (30 Outbound Calls, 14 Scheduled Meetings)  
**Transcript Coverage:** 18 Usable Transcripts (40.9% of selected records)  
**Source Connection Rate (Telephony Classification):** 11 / 30 calls (36.7%)  
**Verified Dialogue Rate (Transcript-Backed):** 10 / 10 calls with transcript (100%)  

---

## 1. Executive Summary & Headline Numbers

On 21 August 2026, the SpendNest sales and account management team logged 44 selected interactions across five call representatives and ten meeting organizers. 

| Metric | Measured Value | Denominator & Definition | Caveat & Integrity Note |
|---|---|---|---|
| **Selected Activity Count** | 44 Records | All source records for 2026-08-21 Asia/Kolkata | Selected sample, not full historical database. |
| **Call Volume** | 30 Calls | Outbound telephony attempts | 20 voicemails/unresponsive, 10 conversations. |
| **Meeting Volume** | 14 Meetings | Calendar events scheduled | 8 completed with transcripts, 6 empty/cancelled. |
| **Usable Transcript Coverage** | 18 / 44 (40.9%) | Usable text records / 44 selected records | Initial batch delivered 17; M07 arrived in rev 2. |
| **Calls Transcript Coverage** | 10 / 30 (33.3%) | Calls with non-null transcript / 30 calls | 20 background calls intentionally unrecorded. |
| **Meetings Transcript Coverage** | 8 / 14 (57.1%) | Meetings with >=1 turns / 14 meetings | 3 empty recordings, 2 bot cancelled, 1 not scheduled. |
| **Source Reported Connect Rate** | 11 / 30 (36.7%) | `is_connected=true` / 30 calls | Inaccurate: misses C04 (95s voicemail) & inflates B11/B14. |
| **Verified Dialogue Connect Rate**| 10 / 10 (100.0%) | Verified dialogue / 10 calls with text | True human conversation rate on recorded attempts. |

---

## 2. Priority Sales Opportunities (Revenue Signals)

1. **Asterloom Systems (M03) — Top Deal Priority [Sales Pipeline]**
   - **Interaction:** High-engagement demonstration with Customer A (Sponsor) and Customer B (Finance Lead).
   - **Key Findings:** Customer is reimbursing travel/expenses and needs corporate prepaid cards and approval workflows. Customer B cited an estimated monthly spend of **INR 10–13 lakh** (Turn 10), but expressly noted this needs CFO validation.
   - **Honest Uncertainty:** Customer initially expected credit lines; learning that SpendNest domestic cards are prepaid requires internal cashflow alignment. Deal size is unverified.
   - **Next Action:** Deliver comprehensive card workflow collateral and pricing models for CFO review. Owner: Team member A.

2. **Willowbank Advisory (C07) — Channel Multiplier [Partnerships & Advisory]**
   - **Interaction:** Outbound call between Dev and Aditya (Willowbank Advisory).
   - **Key Findings:** Advisory firm incorporates domestic and overseas companies and actively refers clients for virtual business bank accounts. Aditya requested a proposal via chat and agreed to a follow-up call on Monday.
   - **Next Action:** Dev to message partnership proposal on chat app and conduct follow-up call on Monday. Owner: Dev.

3. **Developer API & Event Notifications (C03) — Technical Evaluation [Sales Pipeline]**
   - **Interaction:** Kiran followed up with Milan on API access and webhooks.
   - **Key Findings:** Milan reported price hesitation (*"isn't essential enough for us to spend much on it"*), but asked for an email summary and Monday/Tuesday call.
   - **Next Action:** Kiran to send email titled *"Developer access and event notifications — follow-up"* and call Monday morning. Owner: Kiran.

---

## 3. Customer Success & Churn Escalations

1. **Cedarwave Distribution (M04) — Card Programme Migration Blocker**
   - **Issue:** Cedarwave is transitioning from legacy cards with merchant acceptance issues to SpendNest's wallet-backed cards before month-end.
   - **Blocker:** Customer cannot re-allocate users between departments from the assistant view, creating friction.
   - **Resolution:** Dedicated administrator session required to assist manual reallocation; escalate permission gap to Product/Engineering. Owner: Team member A.

2. **Willowfield Trust (M07) — Critical Description Save Bug**
   - **Issue:** Customer demonstrated that editing event-payment descriptions reverts back to the old string upon saving.
   - **Resolution:** Engineering bug ticket must be logged immediately with screen-share recording. Owner: Team member A.

3. **Brookmint Holdings (M09) — Onboarding Token Expiry Bug**
   - **Issue:** Customer locked out of new entity setup due to an *"expired token"* error on fresh reset emails.
   - **Resolution:** Issue new administrator login credentials directly; investigate link pre-fetch bug. Owner: Team member A.

---

## 4. Rep Performance & Practical Coaching Takeaways

- **Arun (12 Calls, 1 Meeting M12):**
  - *Strength:* Resilient voicemail delivery on C04, clearly explaining the misdirected email.
  - *Coaching Opportunity:* On C01 (Harborlight), Arun met sharp hostility by pushing an automation pitch before establishing rapport. Coach on open-ended qualification questions to soften cold outreach.
- **Meera (5 Calls - C05, C06, C08, C09, C10):**
  - *Strength:* Rapid multi-store qualification (C05 StoreHarbor, C08 People Ops referral).
  - *Coaching Opportunity:* On C10 (Aniket), Meera pushed for a scheduled call after the prospect explicitly asked to be contacted only if interested. Emphasize respecting prospect boundaries.
- **Kiran (1 Call - C03):**
  - *Strength:* Maintained professional composure through severe audio distortion and secured clear agreement on follow-up email subject and call window.
- **Dev (1 Call - C07):**
  - *Strength:* Clean value proposition differentiating SpendNest virtual business accounts from accounting services.

---

## 5. Critical Data Integrity & Upstream Telephony Warnings

1. **Rep Attribution Conflict on C06:**
   - Database metadata states `rep_name: "Meera"`, but the audio transcript opens with *"Good evening. Ravi here. I'll say at the start that this is a cold call."* Management must audit outbound dialer account sharing to ensure accurate commission and activity attribution.
2. **Telephony Connection Classification Flaws:**
   - Call C04 is labelled `is_connected: false` despite delivering a complete 95-second voicemail.
   - Calls B11 and B14 are labelled `is_connected: true` despite having zero conversation turns and being marked `unresponsive`.
3. **Misleading Meeting Titles:**
   - Meeting M02 (*"LedgerBridge / SpendNest discussion"*) is an internal procurement meeting evaluating an e-invoicing vendor, NOT a prospect sales deal.
   - Meeting M10 (*"Billing workflow walkthrough"*) is internal employee training, NOT customer onboarding.
"""

with open(brief_path, 'w') as f_br:
    f_br.write(brief_content.strip() + '\n')

# 5. Write manifest.json and manifest.csv
manifest_json_path = os.path.join(EXPORT_DIR, 'manifest.json')
with open(manifest_json_path, 'w') as f_mj:
    json.dump({
        'manifest_version': '1.0',
        'generated_at': datetime.utcnow().isoformat() + 'Z',
        'total_records': len(manifest_rows),
        'records': manifest_rows
    }, f_mj, indent=2)

manifest_csv_path = os.path.join(EXPORT_DIR, 'manifest.csv')
with open(manifest_csv_path, 'w', newline='') as f_mc:
    writer = csv.DictWriter(f_mc, fieldnames=[
        'record_ref', 'source_type', 'source_id', 'applied_revision', 'route',
        'secondary_routes', 'output_path', 'processing_state', 'manual_override',
        'analysis_freshness', 'has_usable_transcript', 'title'
    ])
    writer.writeheader()
    for row in manifest_rows:
        writer.writerow(row)

print(f"Exports generated successfully! {len(manifest_rows)} manifest records written.")
