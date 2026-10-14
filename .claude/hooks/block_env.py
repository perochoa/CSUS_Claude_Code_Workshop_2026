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
