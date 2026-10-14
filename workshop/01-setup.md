# M1: Setup and First Agent Task (10 min)

**Goal:** drive Claude Code safely on a codebase you've never seen.

## Concept

Today is terminal-first. Claude Code runs as an agent in your shell: it reads files, runs commands, and edits code across the repo. It's a different tool from inline autocomplete in an editor.

## Do it

1. Activate your venv, then start Claude Code from the repo root:

   ```bash
   claude
   ```

2. Ask it:

   > Explain this repo's architecture and trace how a POST /rsvps request flows from route to database. Don't change any code.

3. While it works, try out the safety controls:
   - **Approve or deny** each command it asks to run.
   - **Shift+Tab** cycles the permission modes. One of them is **plan mode**, where Claude can read and plan but not edit.
   - **`/rewind`** (or **Esc Esc**) rolls back to an earlier point in the conversation.

## Exercise (4 min)

Ask the agent:

> Which parts of this codebase look riskiest, and why?

Compare your answer with your neighbour's. Did you get the same list? Why might the answers differ?

## Debrief

What did the agent get right about the architecture without being told anything? What did it have to guess?
