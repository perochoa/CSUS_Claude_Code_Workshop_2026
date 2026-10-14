# Capstone: Pick a Ticket (30 min)

**Goal:** run the full loop on a real task, using every layer you built today.

Start from your own branch, or from `checkpoint/07-capstone` to get every config layer:

```bash
git switch checkpoint/07-capstone
git switch -c capstone/<your-name>
```

## The tickets

The tickets are in the repo's **GitHub Issues**. Pick one and work alone or in pairs.

| Difficulty | Type |
| --- | --- |
| Starter | Bug + testing |
| Medium | Feature |
| Medium | Refactoring |
| Stretch | Hard bug |

Read a ticket with `gh issue view <number>` or in your browser.

## The loop

1. **Plan:** ask for a plan first (plan mode), and approve it.
2. **Implement:** let the agent build it, with your instructions and hooks doing their jobs.
3. **Test:** use the testing skill. All tests must be green.
4. **Review:** run the reviewer agent and fix every blocker.
5. **Commit:** read the final diff yourself, then commit.

## Refactoring? Read this first

Before refactoring, have the agent write **characterization tests** that lock in the current behaviour, quirks included. Run them, and refactor only while they stay green.

> Before changing anything in app/services/legacy_stats.py, write characterization tests that pin down its current output exactly, including edge cases like events with no RSVPs and members in year 5+. Don't fix any behaviour you find odd; just record it.

This is the single most transferable habit for internships.

## Last 5 minutes

Two volunteers share their diff and their reviewer output on screen. There's a prize for the best reviewer catch. 🏆
