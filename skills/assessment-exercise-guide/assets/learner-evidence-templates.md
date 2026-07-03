# Learner Evidence Templates

## LO1 Workflow Selection

```markdown
# LO1 Workflow Selection

Workflow Name:
Business Area:
Learner Role:
Chosen F&B Business Type:

Current Pain Point:

Baseline Frequency:
Average Time Per Run:

Dependencies:
- 

Constraints:
- 

Target Success Metric / ROI:

Evidence Files:
- 
```

## DUO Prompt

```markdown
# LO2 DUO Prompt Evidence

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
```

## LO2 Test Cases

```markdown
# LO2 Reliability Test Cases

| Test Case | Input Summary | Expected Behavior | Actual Output Summary | Pass/Fail | Notes |
|---|---|---|---|---|---|
| Normal | | | | | |
| Messy | | | | | |
| Edge Case | | | | | |
```

## LO4 Automation

```markdown
# LO4 Automation and Observability

Trigger:
Conditions / Branches:
Actions:
Logging:
Failure Alert:

Workflow Diagram:
```

## LO5 Controlled Agent Scope

```markdown
# LO5 Controlled Agent Scope

Agent Goal:

Non-Goals:
- 

Tool Permissions:
- 

Action Limits:
- 

Human Approval Checkpoints:
- 
```

## LO6 Safety

```markdown
# LO6 Safety and Governance

Data Safety:
- [ ] Data is dummy or anonymized.
- [ ] No real personal, customer, employee, payroll, medical, student, or confidential data is included.

Credential Safety:
- [ ] No API keys, tokens, passwords, private URLs, `.env` files, or secrets are visible.
- [ ] Credentials are stored outside the submission evidence.

Access Control:
- [ ] Tools use least-privilege access.
- [ ] High-risk actions require human approval.

Redaction Notes:

Final Safety Confirmation:
```

## LO3 Web App Evidence

```markdown
# LO3 Web App Evidence

Learner prompt used to ask Codex to build the app:

App purpose:
Allow branch users to write or upload daily reports and retrieve historical reports later.

User role:
Branch manager or outlet manager.

Demo sign-in account:
Username: demo.manager
Password: demo123
Authentication note: Simulated demo login only. Not real authentication.

Minimum features:
- Simulated sign-in screen with a demo account
- Branch report form
- Daily report file upload control
- Report date field
- Branch or outlet selector
- Historical report list
- Search or filter by branch, date, or keyword
- Basic validation and handled error state

Input screen or input-state evidence:

Output/history retrieval evidence:

Validation rule:
Empty reports cannot be submitted.

Handled error-state evidence:

Historical retrieval explanation:

Storage/persistence method:

Safety note:
The app uses dummy or anonymized data only. The demo password is for class simulation only and must not be reused for live systems.
```
