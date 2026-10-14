# M4: Skills (15 min)

**Goal:** turn "the way we always do it" into a reusable procedure the agent loads on its own.

## Concept

A skill is a folder containing a `SKILL.md`. The agent loads the skill only when the task matches its **description**, so the description must say *when* to use it. Skills can also bundle scripts and reference files, which the agent reads only when it needs them.

## Do it

Create `.claude/skills/write-endpoint-tests/SKILL.md`:

```markdown
---
name: write-endpoint-tests
description: Write pytest tests for a FastAPI endpoint in this repo. Use when asked to add, extend, or fix tests for a route.
---
# Writing endpoint tests

1. Read the route and the models it touches.
2. Read tests/conftest.py and reuse the existing fixtures.
3. Cover: happy path, validation error (422), not found (404), and every business rule in the route.
4. Run `pytest <file> -q` and iterate until the tests themselves are correct.
5. If a test exposes a real bug, stop and report it. Never weaken a test to make it pass.
```

Restart Claude Code, or run `/clear`. Then ask:

> What skills do you have available?

## Exercise (7 min): testing

Ask:

> Write tests for the RSVP routes.

Watch for:

- [ ] The skill kicks in. The agent mentions it or follows its steps.
- [ ] The tests reuse the fixtures from `conftest.py`.
- [ ] Step 5 makes the agent **report** any real bug it finds instead of quietly writing a passing test around it. Did it find one?

**Finished early?** Write a second skill of your own, for example `add-endpoint`, covering how a new route, service function, and test should be laid out in this repo.

## Debrief

What's the difference between putting this procedure in `CLAUDE.md` and putting it in a skill?
