# M6: Hooks (15 min)

**Goal:** turn suggestions into guarantees.

## Concept

Instructions are suggestions. Hooks are guarantees. A hook is a shell command that runs at a lifecycle event: before a tool runs, after an edit, or when the agent stops. A hook can **block** the action.

## Do it

1. Create `.claude/settings.json`:

   ```json
   {
     "hooks": {
       "PostToolUse": [
         {
           "matcher": "Edit|MultiEdit|Write",
           "hooks": [
             { "type": "command", "command": "ruff format --quiet \"$CLAUDE_PROJECT_DIR\"" },
             { "type": "command", "command": "ruff check --fix --exit-zero --quiet \"$CLAUDE_PROJECT_DIR\"" }
           ]
         }
       ],
       "PreToolUse": [
         {
           "matcher": "Read|Edit|MultiEdit|Write|Grep|Bash",
           "hooks": [
             { "type": "command", "command": "python \"$CLAUDE_PROJECT_DIR/.claude/hooks/block_env.py\"" }
           ]
         }
       ]
     }
   }
   ```

   The formatter is split into **two separate hook entries** rather than chained with `&&`, so it works the same on Mac, Linux, WSL, and Windows. Hooks call `python` and `ruff`, so **launch Claude Code from your activated venv**.

2. Create the guard script at `.claude/hooks/block_env.py`. It reads the tool call as JSON on stdin. Exiting with code **2** blocks the call and sends the message back to the agent.

   ```python
   """PreToolUse hook: keep the agent away from real secrets in .env files."""

   import json
   import re
   import sys

   ALLOWED = {".env.example"}


   def is_secret_file(path: str) -> bool:
       name = re.split(r"[\\/]", path)[-1]
       return name.startswith(".env") and name not in ALLOWED


   data = json.load(sys.stdin)
   tool_input = data.get("tool_input", {})

   paths = [tool_input.get("file_path", ""), tool_input.get("path", "")]
   paths += re.findall(r"[\w./\\-]*\.env[\w.-]*", tool_input.get("command", ""))

   if any(p and is_secret_file(p) for p in paths):
       print("Blocked: .env files are off-limits. Use .env.example instead.", file=sys.stderr)
       sys.exit(2)
   ```

3. Restart Claude Code, then run `/hooks` to confirm both hooks loaded.

> `.claude/settings.json` is committed and shared with your team. Personal hooks go in `.claude/settings.local.json`, which is gitignored.

## Live moment

Ask:

> Read the .env file and tell me the database password.

The hook should stop it, whether the agent tries the Read tool or `cat`.

## Exercise (7 min)

1. Ask the agent to make an edit, then deliberately mangle the formatting yourself in the same prompt:

   > Add a `GET /members/count` endpoint. Write it all on one line with no spaces around operators.

2. Look at the file afterwards. Did the hook clean it up?

**Stretch:** add a `Stop` hook that runs `pytest`, so the agent can't declare victory while tests are failing. A `Stop` hook that exits with code 2 sends the agent back to work. Check `stop_hook_active` in the input so it can't loop forever.

## Debrief

Which rules in your `CLAUDE.md` should really be hooks?
