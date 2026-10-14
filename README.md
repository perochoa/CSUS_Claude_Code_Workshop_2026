# CSUS Event Hub

A small FastAPI + SQLite API for club events, members, and RSVPs. It's the sample codebase for the CSUS workshop **Beyond Autocomplete: Building an AI-Native Dev Workflow with Claude Code**.

The code is deliberately imperfect. During the workshop you'll use Claude Code to explore it, fix it, test it, review it, and refactor it.

> **Attendees:** the step-by-step handout is in [`workshop/`](workshop/README.md).

## Before the workshop

You need:

- A GitHub account
- Python 3.11 or newer, and Git
- A terminal you're comfortable in. On Windows, use **WSL (Ubuntu)** (recommended) or **PowerShell 7**. If you use native Windows, you also need [Git for Windows](https://git-scm.com/download/win).
- [Claude Code](https://docs.claude.com/en/docs/claude-code/setup), signed in with your own Claude plan or the CSUS-provided API key
- Optional: Node.js 20+ for the browser (Playwright MCP) demo, and the GitHub CLI (`gh`)

## Setup

Clone the repo. **WSL users:** clone it inside your Linux home folder (`~/`), not under `/mnt/c/`, because WSL is much slower on Windows-mounted folders.

```bash
git clone https://github.com/perochoa/CSUS_Claude_Code_Workshop_2026.git
cd CSUS_Claude_Code_Workshop_2026
```

Then run these commands:

| Step                  | Mac, Linux, or WSL          | Windows PowerShell 7          |
| --------------------- | --------------------------- | ----------------------------- |
| Create venv           | `python3 -m venv .venv`     | `python -m venv .venv`        |
| Activate venv         | `source .venv/bin/activate` | `.venv\Scripts\Activate.ps1`  |
| Install               | `pip install -e ".[dev]"`   | `pip install -e ".[dev]"`     |
| Create local env file | `cp .env.example .env`      | `Copy-Item .env.example .env` |
| Run tests             | `pytest`                    | `pytest`                      |

When `pytest` finishes, **every test should pass**. If any fail, ask a floater for help.

If PowerShell refuses to activate the venv, run this once: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

**Always start Claude Code from the activated venv**, so that `python`, `pytest`, and `ruff` resolve correctly for the agent:

```bash
claude
```

## Everyday commands

| Task                      | Command                                 |
| ------------------------- | --------------------------------------- |
| Run all tests             | `pytest`                                |
| Run one test file or test | `pytest tests/test_events.py -k <name>` |
| Lint and auto-fix         | `ruff check --fix .`                    |
| Format                    | `ruff format .`                         |
| Load demo data            | `python -m app.seed`                    |
| Run the API               | `uvicorn app.main:app --reload`         |

While the API is running, interactive docs are at <http://localhost:8000/docs>.

## Project layout

```text
app/
├── main.py              # FastAPI app + router wiring
├── config.py            # settings read from environment variables
├── db.py                # engine and session dependency
├── models.py            # SQLModel tables and schemas: Event, Member, RSVP
├── seed.py              # demo data
├── routes/
│   ├── events.py        # CRUD for events
│   ├── members.py       # members
│   ├── rsvps.py         # RSVPs and check-in
│   └── stats.py         # exec dashboard numbers
└── services/
    ├── events.py        # event business logic
    └── legacy_stats.py  # stats calculations
tests/
├── conftest.py          # test client + in-memory DB fixtures
└── test_events.py
```

## Falling behind? Use a checkpoint

Each workshop module has a branch that already contains the configuration from that module and all the earlier ones. Commit or stash your work, then switch:

```bash
git stash            # or: git add -A && git commit -m "my work"
git switch checkpoint/04-skills
```

| Branch                       | State after                                       |
| ---------------------------- | ------------------------------------------------- |
| `main`                       | Starting point, with no AI configuration          |
| `checkpoint/01-setup`        | M1: setup and first agent task                    |
| `checkpoint/02-instructions` | M2: `CLAUDE.md` project instructions              |
| `checkpoint/03-context`      | M3: giving useful context                         |
| `checkpoint/04-skills`       | M4: the `write-endpoint-tests` skill              |
| `checkpoint/05-agents`       | M5: the `code-reviewer` agent                     |
| `checkpoint/06-hooks`        | M6: format and secret-guard hooks                 |
| `checkpoint/07-capstone`     | M7: Playwright MCP server, ready for the capstone |

The checkpoints add configuration only, never code fixes, so the exercises are still yours to solve.
