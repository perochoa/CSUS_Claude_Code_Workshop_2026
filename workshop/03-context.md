# M3: Giving Useful Context (10 min)

**Goal:** point the agent at exactly the right code, error, and expected behaviour, and nothing else.

## Concept

Context is a budget. A vague prompt makes the agent search, guess, and wander. A precise prompt gets a precise fix.

> ❌ **Bad:** RSVPs are broken, fix it.

> ✅ **Good:** In @app/routes/rsvps.py, an event with capacity 50 accepts a 51st RSVP. Reproduce it with a failing test first, explain the root cause, then fix it. Don't touch other files.

## Context tools

| Tool | Example | What it does |
| --- | --- | --- |
| `@` file reference | `@app/routes/rsvps.py` | Puts exactly that file in context |
| Paste | stack trace, screenshot | The agent sees the real error |
| `!` shell command | `!pytest -x` | Runs the command and puts its output in context |
| Pipe to a one-shot prompt | `pytest 2>&1 \| claude -p "explain this failure"` | Scriptable; works in CI and over SSH |
| Plan mode | Shift+Tab until you see plan mode | Get a plan before any edit |
| `/clear` | between unrelated tasks | Old context doesn't leak in |
| `/compact` | in long sessions | Summarizes history to free up space |

## Exercise (5 min): debugging

Run `/clear`, commit, then fix the capacity bug using **reproduce → explain → fix**:

1. Ask for a failing test that reproduces the overbooking.
2. Ask for the root cause in one sentence.
3. Only then, ask for the fix.

Check yourself:

- [ ] A regression test exists and fails without the fix.
- [ ] The fix is a small change in one file.
- [ ] `pytest` is green.

## Debrief

How many files did the agent open with the bad prompt compared with the good one?
