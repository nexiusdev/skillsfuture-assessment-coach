#!/usr/bin/env python
"""Scaffold the LO1-LO6 exercise evidence files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def write_if_missing(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(text.strip() + "\n", encoding="utf-8")


def scaffold_main(main: Path) -> None:
    dirs = [
        "branch-reports",
        "ceo-reports",
        "prompts",
        "plugin/.codex-plugin",
        "automation",
        "governance",
        "safety",
        "lo3-web-app",
        "assessment-notes",
    ]
    for rel in dirs:
        (main / rel).mkdir(parents=True, exist_ok=True)

    write_if_missing(
        main / "assessment-notes" / "LO1-workflow-selection.md",
        """# LO1 Workflow Selection

Workflow Name: Daily CEO Operations Report Consolidation
Business Area: F&B Operations
Learner Role: Operations Manager
Chosen F&B Business Type:

Current Pain Point:

Baseline Frequency: Daily
Average Time Per Run:

Dependencies:
- Dummy branch manager daily reports
- Codex project folder
- CEO report output format

Constraints:
- Use dummy or anonymized data only
- Do not invent missing sales numbers or supplier confirmations
- Preserve source report dates

Target Success Metric / ROI:

Evidence Files:
- branch-reports/
- ceo-reports/
""",
    )

    write_if_missing(
        main / "prompts" / "DUO-prompt.md",
        """# LO2 DUO Prompt Evidence

## What DUO Prompting Means

Discover:
The start of the context gathering process where AI and user begin the conversation.

Understand:
The process where AI and user ask each other questions so both sides fully understand the context.

Output:
The step where Codex uses the confirmed shared understanding to generate a polished Word .docx CEO report for learner review. The report must be designed for executive scanning first and detailed reading second. The reusable skill/plugin files are created only after the learner confirms that the CEO report output is accurate.

## Discover - Learner Answers

Chosen F&B business:

Daily details the CEO is keen to know:
-

Critical issues:
-

Medium issues:
-

Low issues:
-

## Understand - Shared Understanding

Clarifying questions asked by Codex:
-

Learner confirmations or corrections:
-

Final agreed context:
-

## Output - CEO Report Review

Final CEO daily report requirements:
-

Generated CEO report path:

CEO report format and design confirmation:
- Word .docx output
- Scan-friendly first page
- Key daily summary
- Highlights
- Coloured priority/status cues
- Tables or bullet points
- Attention callouts
- Supporting details below the executive scan layer

Learner accuracy confirmation:

Correction notes, if any:

## CEO Feedback - Reporting Format Changes

Learner-suggested format changes:
-

Options offered by Codex if the learner was unsure:
- Move urgent CEO actions to the very top of page 1.
- Add a traffic-light summary for each outlet.
- Add a top-three risks box before the detailed tables.
- Show sales movement in a compact comparison table.
- Separate "Needs CEO decision" from "For monitoring only".
- Add owner and due-date columns to the action list.
- Reduce narrative detail on page 1 and move more details to the appendix.

Confirmed format changes:
-

Revised CEO report path:

## Reusable Skill Update Prompt

Learner prompt to update `plugin/SKILL.md`:

Prompt template offered if needed:
Please modify the CEO report assistant skill file to include the new reporting format changes we accepted: [list changes]. Future CEO reports should follow this format automatically.

Updated skill file path:

Learner acceptance of updated skill file:

## Confirmed Reusable Skill Instruction Set

Final prompt or agent instruction:

## Learner Reflection

How DUO helped clarify the workflow:
""",
    )

    write_if_missing(
        main / "plugin" / ".codex-plugin" / "plugin.json",
        json.dumps(
            {
                "name": "fnb-ceo-report-assistant",
                "version": "0.1.0",
                "description": "Guides Codex to consolidate dummy F&B branch reports into a CEO daily operations report.",
                "skills": ["SKILL.md"],
            },
            indent=2,
        ),
    )

    write_if_missing(
        main / "plugin" / "SKILL.md",
        """---
name: fnb-ceo-report-assistant
description: Consolidate dummy or anonymized F&B branch manager reports into a CEO-ready daily operations report based on the learner's confirmed DUO requirements.
---

# F&B CEO Report Assistant

## Role

Act as an operations report assistant for an F&B operations manager.

## Boundaries

- Use only dummy or anonymized branch reports.
- Follow the learner's confirmed CEO daily report requirements.
- Do not invent missing figures, dates, supplier names, or action confirmations.
- Do not send the report externally without human approval.

## Workflow

1. Inspect the report folder.
2. Read every branch report.
3. Extract the CEO-priority fields confirmed in the DUO prompt.
4. Classify issues as critical, medium, or low using the learner's definitions.
5. Generate a CEO-ready Word document.

## Required Inputs

- Branch reports
- Report date
- CEO report requirements
- Critical, medium, and low issue definitions

## Fixed Output Format

- Word `.docx` file saved in `ceo-reports/`
- First-page key summary for the day
- Highlights and positive signals
- Coloured priority or status cues
- Attention callouts for urgent CEO action
- Tables comparing outlet issues
- Bullet-point action list
- Detailed findings below the executive scan layer
- Outlet watchlist
- Source files reviewed

## Knowledge List

- F&B branch daily reporting
- CEO operations reporting
- DUO prompting requirements
- Dummy-data safety
- Missing-data handling

## Escalation Rules

Ask for human review if reports are missing, contain real personal data, expose secrets, conflict on dates, or require external sending.
""",
    )

    write_if_missing(
        main / "assessment-notes" / "LO2-test-cases.md",
        """# LO2 Reliability Test Cases

| Test Case | Input Summary | Expected Behavior | Actual Output Summary | Pass/Fail | Notes |
|---|---|---|---|---|---|
| Normal | All expected branch reports are present and readable. | Generate CEO report using confirmed DUO requirements and issue priority definitions. | | | |
| Messy | Reports have inconsistent formatting or missing optional details. | Extract available facts, mark missing data honestly, and avoid invention. | | | |
| Edge Case | One branch report is missing, empty, unsupported, or has a conflicting date. | Stop or warn clearly, log the issue, and ask for correction. | | | |
""",
    )

    write_if_missing(
        main / "automation" / "workflow-diagram.md",
        """# LO4 Workflow Diagram

```mermaid
flowchart TD
  A[Daily trigger after branch submission deadline] --> B{All expected reports present?}
  B -- Yes --> C[Extract branch report details]
  C --> D[Generate CEO daily report]
  D --> E[Write success log]
  B -- No --> F[Write failure log]
  F --> G[Create missing-report alert]
```
""",
    )

    write_if_missing(
        main / "automation" / "run-log-success.md",
        """# Successful Run Log

Timestamp:
Trigger:
Input files processed:
Key steps:
Status:
Output path:
Notes:
""",
    )

    write_if_missing(
        main / "automation" / "failure-alert-proof.md",
        """# Failure Alert Proof

Alert Type: Simulated class exercise alert
Timestamp:
Failure condition:
Message shown/sent:
Screenshot or evidence path:
Secrets redacted: Yes / No
""",
    )

    write_if_missing(
        main / "governance" / "controlled-agent-scope.md",
        """# LO5 Controlled Agent Scope

Agent Goal:
Read dummy branch reports and prepare a CEO-ready daily operations report.

Non-Goals:
- Do not send reports externally.
- Do not update live POS, inventory, payroll, supplier, or customer systems.
- Do not delete or overwrite source reports.
- Do not use real personal or confidential data.

Tool Permissions:
- Read files in the project folder.
- Generate draft report files.
- Write logs and assessment evidence files.

Action Limits:
- Do not invent missing facts.
- Do not expose secrets.
- Do not perform live business actions.

Human Approval Checkpoints:
- Before sending the CEO report externally
- Before using live company data
- Before deleting or overwriting files
- Before contacting suppliers, customers, or staff
""",
    )

    write_if_missing(
        main / "safety" / "safety-checklist.md",
        """# LO6 Safety Checklist

Data Safety:
- [ ] Data is dummy or anonymized.
- [ ] No real personal, customer, employee, payroll, medical, student, or confidential data is included.

Credential Safety:
- [ ] No API keys, tokens, passwords, private URLs, `.env` files, or secrets are visible.
- [ ] Credentials are stored outside the submission evidence.

Access Control:
- [ ] Tools use least-privilege access.
- [ ] High-risk actions require human approval.

Final Safety Confirmation:
""",
    )

    write_if_missing(
        main / "safety" / "redaction-notes.md",
        """# Redaction Notes

Screenshots or visual evidence reviewed:

Items redacted:

Remaining safety concerns:
""",
    )

    write_if_missing(
        main / "safety" / "credential-handling.md",
        """# Credential Handling

Credential storage method:

Confirmation:
- No API keys, tokens, passwords, private URLs, or `.env` contents are included in the final portfolio.
- Any screenshots or visual evidence are redacted before submission.
""",
    )

    write_if_missing(
        main / "lo3-web-app" / "README.md",
        """# LO3 Branch Daily Report Web App

Purpose:
Build a simple web app that allows branch users to write or upload daily reports and retrieve historical report records later.

Minimum Features:
- Simulated sign-in screen with a demo account
- Branch report form
- Daily report file upload control
- Report date field
- Branch or outlet selector
- Historical report list
- Search or filter by branch, date, or keyword
- Basic validation and handled error state

Data Safety:
- Use dummy or anonymized data only.
- Use simulated demo credentials only, such as username `demo.manager` and password `demo123`.
- Do not use real passwords, real authentication, or production identity services.
- Do not store real customer, employee, payroll, confidential, or commercially sensitive data.

Persistence Note:
Document whether the app uses browser localStorage, a local JSON file, or another simple local storage pattern.
""",
    )

    write_if_missing(
        main / "lo3-web-app" / "LO3-evidence.md",
        """# LO3 Web App Evidence

Learner prompt used to ask Codex to build the app:

App purpose:
Allow branch users to write or upload daily reports and retrieve historical reports later.

User role:
Branch manager or outlet manager.

Demo sign-in account:
Username: demo.manager
Password: demo123
Authentication note: Simulated demo login only. Not real authentication.

Input screen or input-state evidence:

Output/history retrieval evidence:

Validation rule:
Empty reports cannot be submitted.

Handled error-state evidence:

Historical retrieval explanation:

Storage/persistence method:

Safety note:
The app uses dummy or anonymized data only. The demo password is for class simulation only and must not be reused for live systems.
""",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--main", type=Path, required=True, help="Main assessment project folder")
    parser.add_argument("--lo3", type=Path, required=False, help="Optional alternate LO3 app folder")
    args = parser.parse_args()

    scaffold_main(args.main)
    print(f"Main assessment scaffold: {args.main}")
    if args.lo3 is not None:
        args.lo3.mkdir(parents=True, exist_ok=True)
        print(f"Optional LO3 app folder: {args.lo3}")


if __name__ == "__main__":
    main()
