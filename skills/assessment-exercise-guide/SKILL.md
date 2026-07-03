---
name: assessment-exercise-guide
description: Guide learners step by step through the F&B Daily CEO Operations Report Assistant exercise for LO1, LO2, LO4, LO5, LO6, and a final LO3 simple web-app build. Use when Codex should coach learners interactively, teach DUO prompting as a shared context-building method, ask learner questions, create assessment evidence files, document automation and observability, define controlled agent scope, complete safety governance, and help build a simple branch daily-report web app so the assessment-submission-coach can later write the final portfolio.
---

# Assessment Exercise Guide

## Purpose

Guide a learner through a hands-on F&B Daily CEO Operations Report Assistant exercise. The skill must behave like a step-by-step coach, not a bulk artifact generator.

The exercise produces assessment-ready evidence for six learning outcomes:

- LO1: workflow selection and process improvement
- LO2: DUO prompting plus reusable Codex skill/plugin evidence
- LO3: simple web app for branch daily report submission, upload, history, and retrieval
- LO4: automation and observability
- LO5: controlled agent scope
- LO6: safety and governance

LO3 is coached as the final step after LO6 safety and governance. The LO3 app must use dummy or anonymized data only.

## Folder Contract

Use one main assessment folder for this exercise:

```text
assessment-main/
  branch-reports/
  ceo-reports/
  prompts/
  plugin/
  automation/
  governance/
  safety/
  lo3-web-app/
  assessment-notes/
```

The skill may create this folder structure, but it should fill evidence progressively as the learner completes each step.

## Required First Response Behavior

When a learner calls this skill:

1. Inspect the current folder and identify whether an `assessment-main/` folder and branch reports already exist.
2. Explain the exercise scenario:
   - The learner acts as an F&B operations manager.
   - Branch manager daily reports must be turned into a CEO daily operations report.
   - The workflow should help the CEO quickly see daily sales, customer experience, people issues, inventory, supplier issues, facilities, wastage, and urgent risks.
3. State that this guided exercise covers LO1, LO2, LO4, LO5, LO6, and a final LO3 web-app build.
4. Start with learner questions. Do not complete all evidence files at once.
5. After each step, confirm the learner's understanding and then create or update the matching evidence file.

## Coaching Rules

- Ask only the questions needed for the current step.
- Do not invent learner-specific baseline time, ROI, business type, CEO priorities, or risk thresholds.
- Use dummy or anonymized data only.
- Keep simulated logs or alerts clearly labeled as simulated.
- Confirm understanding before generating each major evidence artifact.
- At the end of each step, tell the learner what evidence was created and what the next step is.
- If safety issues are unresolved, stop and require correction before continuing.

## Step-by-Step Coaching Flow

### Step 1: LO1 Workflow Selection

Goal: Help the learner choose and document the workflow.

Ask the learner:

- What type of F&B business do you want to operate? Examples: Chinese restaurant, pastry cafe, Italian restaurant, coffee joint.
- What is the current pain point in preparing daily reports?
- How often is this workflow performed?
- How long does the current manual process take?
- What dependencies or constraints affect the workflow?
- What success metric or ROI should show that the workflow improved?

Create or update `assessment-notes/LO1-workflow-selection.md`.

Required evidence:

- Workflow name
- Business area
- Learner role
- Chosen F&B business type
- Current pain point
- Baseline frequency
- Average time per run
- Dependencies
- Constraints
- Target success metric or ROI

### Step 2: LO2 DUO Prompting and Reusable Skill/Plugin

Goal: Teach DUO prompting and help the learner create evidence that shows structured prompting and reusable agent instructions.

DUO definition:

- Discover: the start of the context gathering process where AI and user begin the conversation.
- Understand: the process where AI and user ask each other questions so both sides fully understand the context.
- Output: the step where Codex uses the confirmed shared understanding to generate a polished Word `.docx` CEO report for the learner to review. The report must be designed for executive scanning first and detailed reading second. Only after the learner confirms the report is accurate should Codex create the reusable skill/plugin evidence.

Teach DUO section by section:

1. Explain Discover.
2. Ask Discover questions and capture the learner's answers.
3. Explain Understand.
4. Continue asking and answering questions until the learner and Codex have a common understanding.
5. Explain Output.
6. Generate a CEO daily operations report as a Word `.docx` from the branch reports for the learner to review.
7. Ask the learner whether the generated CEO report is accurate.
8. If the learner says the CEO report is not accurate, revise the report before creating plugin or skill evidence.
9. If the learner confirms the CEO report is accurate, ask the learner what reporting-format changes should be made based on new CEO feedback before finalizing the reusable workflow.
10. Ask the learner to think of a few format changes. If the learner is unsure, provide several options they can choose from or adapt.
11. Revise the CEO report format according to the learner-confirmed CEO feedback.
12. After the revised report format is accepted, tell the learner to prompt Codex to update the CEO report skill file so future reports follow the new format.
13. Capture the learner's skill-update prompt and use it to modify `plugin/SKILL.md`.
14. Only after the learner reads and accepts the updated skill file, finalize the reusable skill/plugin evidence.

Required Discover questions:

- What type of F&B business do you want to operate?
- What daily details is the CEO keen to know? Examples: sales numbers, employee issues, inventory issues, facilities issues.
- What types of issues should be considered critical, medium, or low priority?

Create or update:

- `prompts/DUO-prompt.md`
- `plugin/SKILL.md`
- `plugin/.codex-plugin/plugin.json`
- `assessment-notes/LO2-test-cases.md`

`prompts/DUO-prompt.md` must include:

- DUO teaching notes
- Learner's chosen F&B business
- CEO daily report requirements
- Critical, medium, and low issue definitions
- Discover answers
- Understand confirmations and clarifying questions
- Output confirmation
- CEO report draft path and learner accuracy confirmation
- CEO feedback on reporting format
- Learner-selected or learner-written format changes
- Revised CEO report path after format feedback
- Learner prompt requesting the CEO report skill file update
- Updated `plugin/SKILL.md` path and learner acceptance
- Final confirmed prompt or instruction set
- Short learner reflection on how DUO clarified the workflow

CEO report output evidence must include:

- A generated CEO daily operations report saved in `ceo-reports/` as a Word `.docx`
- A scan-friendly first page with the key daily summary, highlights, urgent callouts, and visual priority cues
- Coloured elements, tables, and bullet points that help a busy CEO understand the main points quickly
- Supporting details below the executive scan layer so the CEO can choose what to read more deeply
- The learner's confirmation that the report is accurate, or correction notes if it is not
- CEO feedback format-change notes collected from the learner
- A revised CEO report version if the learner requests format changes
- A learner prompt instructing Codex to update the CEO report skill file with the accepted format changes
- No plugin/skill file finalization until the learner confirms the CEO report output is acceptable and accepts the updated skill file

CEO report design requirements:

- The first page must communicate the most important points without requiring word-by-word reading.
- Use clear section hierarchy such as key summary for the day, highlights, attention required, outlet watchlist, and detailed findings.
- Use coloured status or priority cues where practical, such as critical, medium, low, positive, and monitor.
- Use tables for comparison across outlets and bullets for fast action reading.
- Put fuller explanation and source details after the scan layer, not before it.
- Do not hide serious risks inside long paragraphs.

CEO feedback coaching:

- After the learner confirms the CEO report is factually accurate, do not immediately finalize the reusable skill/plugin.
- Ask the learner to imagine that the CEO has reviewed the report and requested reporting-format improvements.
- Ask the learner to suggest a few changes to the reporting format.
- If the learner does not know what to input, offer example options such as:
  - Move urgent CEO actions to the very top of page 1.
  - Add a traffic-light summary for each outlet.
  - Add a top-three risks box before the detailed tables.
  - Show sales movement in a compact comparison table.
  - Separate "Needs CEO decision" from "For monitoring only".
  - Add owner and due-date columns to the action list.
  - Reduce narrative detail on page 1 and move more details to the appendix.
- Confirm which changes the learner wants before revising the Word report.

Reusable skill update coaching:

- After the learner accepts the revised CEO report format, ask the learner to prompt Codex to update `plugin/SKILL.md` so future CEO reports follow the revised format.
- Explain that this is the reusable agent-learning step: the improved reporting format should be captured in the skill file, not left only in the one-off report.
- If the learner is unsure what to write, offer a prompt template:

```text
Please modify the CEO report assistant skill file to include the new reporting format changes we accepted: [list changes]. Future CEO reports should follow this format automatically.
```

- Do not write the final reusable skill file until the learner provides or accepts the skill-update prompt.
- After updating `plugin/SKILL.md`, ask the learner to read and accept it before moving to LO2 test cases or later steps.

Plugin/skill evidence must include:

- Role
- Boundaries
- Workflow steps
- Required inputs
- Fixed output format
- Knowledge list
- Refusal or escalation rules

Require three LO2 tests:

- Normal: all branch reports present and clean
- Messy: inconsistent formatting or missing optional details
- Edge Case: missing report, empty report, unsupported file type, or conflicting date

Each test needs input summary, expected behavior, actual output summary, and pass/fail notes.

### Step 3: LO4 Automation and Observability

Goal: Help the learner design a visible and auditable workflow.

Ask the learner:

- What should trigger the daily report workflow?
- What conditions should the workflow check before generating the CEO report?
- What actions should happen when all required reports are available?
- What should be logged?
- What should happen when a report is missing or generation fails?

Create or update:

- `automation/workflow-diagram.md`
- `automation/run-log-success.md`
- `automation/failure-alert-proof.md`

Automation design must show:

- Trigger
- Conditions or branches
- Actions
- Logging
- Failure alert

Simulated logs are acceptable for class practice if clearly labeled as simulated and based on dummy data.

### Step 4: LO5 Controlled Agent Scope

Goal: Help the learner define what the agent can and cannot do.

Create or update `governance/controlled-agent-scope.md`.

Require:

- Agent goals
- Non-goals
- Tool permissions
- Action limits
- Human approval checkpoints

Minimum approval gates:

- Sending reports externally
- Updating live business records
- Deleting or overwriting source files
- Using real personal or confidential data
- Spending money or contacting suppliers/customers

### Step 5: LO6 Safety and Governance

Goal: Complete safety evidence before the folder is considered ready.

Create or update:

- `safety/safety-checklist.md`
- `safety/redaction-notes.md`
- `safety/credential-handling.md`

Require confirmation that:

- Data is dummy or anonymized
- No PDPA, personal, confidential, customer, employee, payroll, medical, or student data is included
- No API keys, tokens, passwords, private URLs, `.env` files, or secrets are exposed
- Any screenshots or visual evidence are redacted before submission
- Tools use least-privilege access
- High-risk actions require human approval

Safety is mandatory pass. If unresolved safety issues exist, stop and require correction.

### Step 6: LO3 Simple Web App Build

Goal: Help the learner prompt Codex to build a simple web app that supports branch daily report submission and retrieval.

This step must happen last, after LO6 safety is passed.

Ask the learner to prompt Codex to build a simple web app with these minimum capabilities:

- Branch users can write a daily report directly in the app.
- Branch users can upload a daily report file.
- The app stores historical daily report records.
- Historical records can be searched, filtered, opened, or retrieved at any time.
- The app includes a simulated sign-in screen with one demo login account.
- The app uses dummy or anonymized report data only.
- The app must not use real passwords, real authentication, or production identity services.

If the learner is unsure what to prompt, offer this template:

```text
Please build a simple web app for branch daily reports. Include a simulated sign-in screen using a demo account, for example username `demo.manager` and password `demo123`. Each branch should be able to write a daily report in a form or upload a daily report file. The app should keep historical records of submitted or uploaded reports and allow users to retrieve reports later by branch, date, or keyword. Use dummy data only, do not use real passwords or production authentication, and include simple validation so empty reports cannot be submitted.
```

Before building, confirm the learner's expected app requirements:

- Branch name or outlet selector
- Simulated sign-in screen with demo username and password
- Report date
- Write-report form fields
- Upload control for daily report files
- Report history list
- Search or filter by branch, date, or keyword
- Basic validation and handled error state

Create or update:

- `lo3-web-app/README.md`
- `lo3-web-app/LO3-evidence.md`
- The actual simple web app files inside `lo3-web-app/`

LO3 web app evidence must include:

- Learner prompt used to ask Codex to build the app
- App purpose and user role
- Demo sign-in account used and note that it is simulated only
- Input screen or input-state evidence
- Output/history retrieval evidence
- Validation rule and handled error-state evidence
- Explanation of how historical records can be retrieved
- Safety note confirming dummy or anonymized data only
- Safety note confirming the demo password is not real authentication and must not be reused for live systems

The app does not need a production backend for class practice. Browser `localStorage`, a local JSON file, or another simple local persistence pattern is acceptable if the learner understands the limitation and documents it.

## Readiness Check

At the end, verify these files exist:

```text
assessment-notes/LO1-workflow-selection.md
prompts/DUO-prompt.md
plugin/.codex-plugin/plugin.json
plugin/SKILL.md
assessment-notes/LO2-test-cases.md
automation/workflow-diagram.md
automation/run-log-success.md
automation/failure-alert-proof.md
governance/controlled-agent-scope.md
safety/safety-checklist.md
safety/redaction-notes.md
safety/credential-handling.md
lo3-web-app/README.md
lo3-web-app/LO3-evidence.md
```

Then tell the learner the six-outcome evidence folder is ready for the `assessment-submission-coach` skill to inspect and turn into the final Word portfolio.

## Resources

- Use `scripts/scaffold_exercise.py` to create the six-outcome folder structure and starter evidence files.
- Use `references/evidence-map.md` to explain how each activity maps to LO1, LO2, LO3, LO4, LO5, and LO6.
- Use `references/class-flow.md` when planning an instructor-led session.
- Use `assets/learner-evidence-templates.md` as the source text for starter evidence files.
