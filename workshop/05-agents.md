# M5: Custom Agents (15 min)

**Goal:** build a specialist reviewer that can't "helpfully" rewrite your code.

## Concept

A custom agent (subagent) has its own system prompt, its own restricted tools, and its **own context window**, so it reviews your code with fresh eyes. A read-only reviewer can only report problems; it can't fix them.

## Do it

Create `.claude/agents/code-reviewer.md`:

```markdown
---
name: code-reviewer
description: Reviews code changes for bugs, security issues, and convention violations. Use after code changes and before committing.
tools: Read, Grep, Glob, Bash
---
You are a senior reviewer for this repo.

Scope: review uncommitted changes (`git diff HEAD`). If there are none, review the most recent commit (`git show HEAD`). Review only that diff, plus whatever surrounding code you need to understand it.

Report each finding as: severity (blocker / major / nit), file:line, problem, suggested fix.
Check especially for SQL injection, missing tests, business logic in routes, and naive datetimes.
Never edit files. If the diff is clean, say so in one line.
```

Run `/agents` to see it, and to learn the interactive way to create and restrict agents. Claude delegates to an agent automatically when its description matches, or you can ask for it by name.

## Exercise (8 min): code review

A teammate just pushed a new search feature. Commit or stash your work, then check out their branch:

```bash
git switch exercise/05-event-search
```

Ask:

> Use the code-reviewer agent to review the latest commit.

Then:

1. Have the **main** agent fix every blocker the reviewer found.
2. Run the reviewer again. Repeat until it reports a clean diff.

**Stretch:** build a `test-writer` agent that uses your M4 skill.

## Debrief

Why give the reviewer `Bash` but not `Edit` or `Write`? What could still go wrong with `Bash`?
