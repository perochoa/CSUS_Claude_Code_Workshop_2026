# M3: Giving Useful Context (10 min)

**Goal:** point the agent at exactly the right code, error, and expected behaviour, and nothing else. Then measure the difference.

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
| `/context` | any time | Shows how much of the context window is in use |
| `/clear` | between unrelated tasks | Old context doesn't leak in |
| `/compact` | in long sessions | Summarizes history to free up space |

## Exercise (5 min): bad prompt vs good prompt

Work in pairs. Each of you runs **one** prompt on your own laptop, then you compare results.

1. **Both partners:** save your work and start from a clean slate:

   ```bash
   git add -A && git commit -m "before M3"
   ```

   Then run `/clear` in Claude Code.

2. **Partner A** sends the bad prompt, exactly as written:

   > RSVPs are broken, fix it.

   **Partner B** sends the good prompt, exactly as written:

   > In @app/routes/rsvps.py, an event with capacity 50 accepts a 51st RSVP. Reproduce it with a failing test first, explain the root cause, then fix it. Don't touch other files.

3. **Keep it fair:** approve the agent's requests, but don't add extra instructions. If it asks you a question, answer briefly and count that as a follow-up.

4. Fill in the scorecard below.

### Scorecard

| | A (bad) | B (good) |
| --- | --- | --- |
| **Fixed the overbooking bug?** (yes / no / fixed something else) | | |
| **Files changed or added:** `git status --short` | | |
| **Regression test added?** | | |
| **Does the test fail without the fix?** (see below) | | |
| **Follow-up prompts you had to send** | | |
| *If time:* files read/searched before the first edit (count in the transcript) | | |
| *If time:* context used, from `/context` | | |
| *If time:* tokens and cost, from `/cost` | | |

**Does the test fail without the fix?** Temporarily remove only the fix, run the tests, then put the fix back:

```bash
git stash push -- app/     # sets aside the change to app/, keeps the new test
pytest                     # the new test should FAIL here
git stash pop              # restore the fix
```

**Partner A, finished early?** Reset and try the good prompt yourself: `git reset --hard && git clean -fd`, `/clear`, go.

## What to expect

This repo is small, so the bad prompt may still "work", and the token and file counts may be close. The rows that reliably differ are about **correctness and control**:

- **Which bug got fixed?** "RSVPs are broken" is ambiguous, and this repo has more than one RSVP problem.
- **Is there proof?** The vague prompt rarely produces a regression test.
- **Did it stay in scope?** The vague prompt is free to edit anything.

Agents vary from run to run, so a single comparison proves little. Compare across the whole room in the debrief.

## Debrief

- Did any bad-prompt run fix a *different* bug from the overbooking? What would happen if you merged that and moved on?
- Which pair saw the biggest gap, and in which row?
- Imagine a 100,000-line codebase. Which rows of the scorecard would grow the most?
