# SkillsFuture Assessment Coach Skills

Standalone Codex skills for guiding Agentic AI Foundations learners through
the hands-on exercise and final competency-based assessment submission.

## Contents

- `skills/assessment-exercise-guide/SKILL.md`: the Codex skill entrypoint for
  the guided F&B CEO report exercise and LO1-LO6 evidence creation.
- `skills/assessment-exercise-guide/references/`: evidence mapping and class
  flow guidance used by the exercise skill.
- `skills/assessment-exercise-guide/assets/`: reusable learner evidence
  templates.
- `skills/assessment-exercise-guide/scripts/`: scaffold helper for creating the
  exercise folder structure.
- `skills/assessment-submission-coach/SKILL.md`: the Codex skill entrypoint.
- `skills/assessment-submission-coach/references/`: assessment requirements and
  checking guidance used by the skill.
- `skills/assessment-submission-coach/assets/`: reusable learner submission
  template.
- `skills/assessment-submission-coach/scripts/`: lightweight completeness
  checker for draft submissions.
- `templates/`: optional Appendix A Word templates from
  `AppendixA_Templates_Agentic_AI_Foundations_v1.1.zip`.

## Recommended Learner Flow

1. Install and use `assessment-exercise-guide` to create LO1-LO6 evidence.
2. Install and use `assessment-submission-coach` to prepare, package, and email
   the final Word portfolio.

## Install

Install each skill folder separately. Learners may install one or both skills.

Skill folders:

```text
skills/assessment-exercise-guide
skills/assessment-submission-coach
```

### Windows PowerShell

```powershell
git clone https://github.com/nexiusdev/skillsfuture-assessment-coach.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\skillsfuture-assessment-coach\skills\assessment-exercise-guide" "$env:USERPROFILE\.codex\skills\assessment-exercise-guide"
Copy-Item -Recurse -Force ".\skillsfuture-assessment-coach\skills\assessment-submission-coach" "$env:USERPROFILE\.codex\skills\assessment-submission-coach"
```

### macOS Or Linux

```bash
git clone https://github.com/nexiusdev/skillsfuture-assessment-coach.git
mkdir -p "$HOME/.codex/skills"
cp -R ./skillsfuture-assessment-coach/skills/assessment-exercise-guide "$HOME/.codex/skills/assessment-exercise-guide"
cp -R ./skillsfuture-assessment-coach/skills/assessment-submission-coach "$HOME/.codex/skills/assessment-submission-coach"
```

Restart Codex after copying the skill if it does not appear immediately.

## Verify Installation

After installation, confirm this file exists:

```text
~/.codex/skills/assessment-exercise-guide/SKILL.md
~/.codex/skills/assessment-submission-coach/SKILL.md
```

On Windows, the equivalent path is:

```text
C:\Users\<your-name>\.codex\skills\assessment-exercise-guide\SKILL.md
C:\Users\<your-name>\.codex\skills\assessment-submission-coach\SKILL.md
```

## Prompt Codex To Install

```text
Install the Codex skill from this GitHub repository:
https://github.com/nexiusdev/skillsfuture-assessment-coach

Copy skills/assessment-exercise-guide and skills/assessment-submission-coach
into my Codex skills directory as two separate skill folders, then confirm that
both SKILL.md files are installed.
```

## Common Install Issues

- The repository root was copied instead of the skill folder. The installed
  paths should end with `skills/assessment-exercise-guide` and/or
  `skills/assessment-submission-coach`.
- The `SKILL.md` file is missing from the installed folder.
- The repository ZIP was not extracted before copying.
- Codex needs to be refreshed or restarted after adding the skill.

## Use Case

Use `assessment-exercise-guide` when a learner needs step-by-step coaching to
create exercise evidence. Use `assessment-submission-coach` when a learner needs
help preparing, reviewing, improving, packaging, or emailing the final Agentic
AI Foundations assessment portfolio.

The final learner submission should be a professional Microsoft Word `.docx`
portfolio and must use only dummy or anonymized data.

## Safety Boundary

Do not include real personal data, confidential client information, API keys,
passwords, private URLs, or screenshots containing secrets in learner
submissions or reusable examples.

## Template Status

The skill works without the optional `.docx` templates. If the `templates/`
folder is present, learners may use those files as supporting worksheets before
compiling the final Word portfolio submission.
