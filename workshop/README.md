# Beyond Autocomplete: Attendee Handout

Stop treating AI like a fancy autocomplete. Teach it your codebase, give it guardrails, and make it a teammate.

**The one idea behind today:** the AI is only as good as the context and guardrails you give it. Each module adds one layer, so watch how the output improves as the layers stack.

## Before you start

Finish the setup in the [main README](../README.md). You're ready when:

- `pytest` passes in your activated venv
- running `claude` in the repo folder opens a session

## Modules

| Clock | Module | You'll practise | Catch-up branch |
| --- | --- | --- | --- |
| 0:10 | [M1 Setup and first agent task](01-setup.md) | Codebase onboarding | `checkpoint/01-setup` |
| 0:20 | [M2 Project instructions](02-instructions.md) | Feature development | `checkpoint/02-instructions` |
| 0:35 | [M3 Giving useful context](03-context.md) | Debugging | `checkpoint/03-context` |
| 0:45 | [M4 Skills](04-skills.md) | Testing | `checkpoint/04-skills` |
| 1:00 | Break 🍕 | | |
| 1:10 | [M5 Custom agents](05-agents.md) | Code review | `checkpoint/05-agents` |
| 1:25 | [M6 Hooks](06-hooks.md) | Guardrails | `checkpoint/06-hooks` |
| 1:40 | [M7 MCP servers](07-mcp.md) | External tooling | `checkpoint/07-capstone` |
| 1:50 | [Capstone: pick a ticket](08-capstone.md) | The full loop | `checkpoint/07-capstone` |
| 2:20 | [Responsible use](#responsible-use) | | |

**Stuck or behind?** That's fine and expected. Commit or stash your work, then jump to the branch for the module you're on:

```bash
git stash
git switch checkpoint/05-agents
```

## The toolkit on one page

| Concept | What it does | Where it lives | How you use it |
| --- | --- | --- | --- |
| Project instructions | Always-loaded rules about the repo | `CLAUDE.md` at the repo root | `/init` to generate, `/memory` to edit |
| Scoped instructions | Rules for one part of the repo | `CLAUDE.md` inside a subfolder | Loaded when Claude works in that folder |
| Skills | A packaged procedure, loaded on demand | `.claude/skills/<name>/SKILL.md` | Triggered when the task matches the description |
| Subagents | A specialist with its own prompt, tools, and context | `.claude/agents/<name>.md` | `/agents`; delegated automatically or by name |
| Hooks | Deterministic scripts at lifecycle events | `hooks` in `.claude/settings.json` | `/hooks` to inspect |
| MCP servers | External tools and data | `.mcp.json` | `claude mcp add`, `/mcp` for status |
| Context control | Point at exactly the right code | — | `@file`, `!` for shell, `/clear`, `/compact` |
| Safety controls | Decide what runs, undo mistakes | Permission settings | Shift+Tab cycles modes (incl. plan mode); `/rewind` |

**Mental model:**

- **Instructions** are what the AI should know.
- **Skills** are how to do a task.
- **Agents** are who does it.
- **Hooks** are what always happens, no matter what the AI decides.
- **MCP** is what it can reach outside the repo.

## Safety habits, all day

1. **Commit before every agent task.** `git add -A && git commit -m "checkpoint"` gives you a clean place to come back to.
2. **Read every diff before you accept it.** You own every line you commit.
3. **Undo is cheap.** `/rewind` (or press Esc twice) rolls back the conversation and the code.

## Responsible use

- **Academic integrity comes first.** AI policies differ by course and by assignment. Using these tools where a syllabus prohibits them is academic misconduct, so check every course outline. Today's skills are for personal projects, hackathons, internships, and courses that allow them.
- **You own every line you commit.** If you couldn't explain a diff in an interview or a code review, don't merge it.
- **Learning still matters.** Use agents to go faster on things you understand, and to explain things you don't. Don't use them to skip fundamentals you'll be tested on.
- **Protect secrets and data.** Never paste API keys or private data into prompts. Hooks like the `.env` guard exist because "just tell it not to" isn't enough.
- **Watch for prompt injection through MCP.** A malicious web page, issue, or README can contain instructions aimed at your agent. Connect only servers you trust, and keep command approval on for anything destructive.
- **Verify, don't trust.** Agents confidently produce code that looks right and is wrong. Tests, review, and hooks are the safety net.
