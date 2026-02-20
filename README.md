Enterprise Code Checker (Agent-Based)

This project is an automated **code rule checker** built using an **Agent + Skill architecture**.

The goal is simple:

- Check code files against company coding rules  
- Detect violations automatically
- Fail the build in GitHub CI if rules are broken  

This simulates how real companies enforce coding standards.

---

## What this project does

When a developer pushes code:

1. GitHub Actions automatically starts
2. The Agent system receives the task
3. A suitable skill (code checker) is selected
4. The checker scans the file using predefined rules
5. Violations are returned as JSON
6. CI fails if violations exist (Quality Gate)

---

##  Architecture (Simple View)

User / GitHub Action
↓
Agent (core controller)
↓
Router (chooses skill)
↓
Executor (runs skill)
↓
Code Checker Skill
↓
Rule Engine
↓
JSON Report

---

##  Project Structure

enterprise-agent/
│
├── agent/
│ ├── core.py
│ ├── router.py
│ ├── context.py
│ └── skill_registry.py
│
├── engine/
│ └── executor.py
│
├── skills/
│ └── code_checker/
│ ├── checker.py
│ ├── rules.json
│ ├── runner.py
│ └── skill.json
│
├── .github/workflows/
│ └── code-check.yml
│
└── main.py

##  How it works (Step by Step)

1. `main.py` starts the system
2. Agent receives the task
3. Context is created (language detection etc.)
4. Router selects matching skill
5. Executor dynamically loads the skill
6. Checker scans file line-by-line
7. Violations are returned as structured JSON
8. GitHub CI fails if violations exist

---

##  Example Rule (rules.json)

```json
{
  "id": "R001",
  "description": "Avoid System.out.println",
  "pattern": "System.out.println",
  "severity": "MEDIUM"
}

