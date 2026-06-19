# Assessment Submission Coach Skill

A standalone Codex skill for coaching Agentic AI Foundations learners through a
competency-based assessment submission.

## Contents

- `skills/assessment-submission-coach/SKILL.md`: the Codex skill entrypoint.
- `skills/assessment-submission-coach/references/`: assessment requirements and
  checking guidance used by the skill.
- `skills/assessment-submission-coach/assets/`: reusable learner submission
  template.
- `skills/assessment-submission-coach/scripts/`: lightweight completeness
  checker for draft submissions.
- `templates/`: optional Appendix A Word templates from
  `AppendixA_Templates_Agentic_AI_Foundations_v1.1.zip`.

## Install

Install the skill folder itself:

```text
skills/assessment-submission-coach
```

### Windows PowerShell

```powershell
git clone https://github.com/nexiusdev/skillsfuture-assessment-coach.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\skillsfuture-assessment-coach\skills\assessment-submission-coach" "$env:USERPROFILE\.codex\skills\assessment-submission-coach"
```

### macOS Or Linux

```bash
git clone https://github.com/nexiusdev/skillsfuture-assessment-coach.git
mkdir -p "$HOME/.codex/skills"
cp -R ./skillsfuture-assessment-coach/skills/assessment-submission-coach "$HOME/.codex/skills/assessment-submission-coach"
```

Restart Codex after copying the skill if it does not appear immediately.

## Verify Installation

After installation, confirm this file exists:

```text
~/.codex/skills/assessment-submission-coach/SKILL.md
```

On Windows, the equivalent path is:

```text
C:\Users\<your-name>\.codex\skills\assessment-submission-coach\SKILL.md
```

## Prompt Codex To Install

```text
Install the Codex skill from this GitHub repository:
https://github.com/nexiusdev/skillsfuture-assessment-coach

Copy skills/assessment-submission-coach into my Codex skills directory and
confirm that SKILL.md is installed.
```

## Common Install Issues

- The repository root was copied instead of the skill folder. The installed
  path should end with `skills/assessment-submission-coach`.
- The `SKILL.md` file is missing from the installed folder.
- The repository ZIP was not extracted before copying.
- Codex needs to be refreshed or restarted after adding the skill.

## Use Case

Use this skill when a learner needs help preparing, reviewing, improving, or
packaging the final Agentic AI Foundations assessment portfolio.

The final learner submission should be a single PDF and must use only dummy or
anonymized data.

## Safety Boundary

Do not include real personal data, confidential client information, API keys,
passwords, private URLs, or screenshots containing secrets in learner
submissions or reusable examples.

## Template Status

The skill works without the optional `.docx` templates. If the `templates/`
folder is present, learners may use those files as supporting worksheets before
compiling the final single-PDF submission.
