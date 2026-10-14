# M7: MCP Servers (10 min)

**Goal:** give the agent a new capability from outside the repo, and know when you don't need one.

## Concept

MCP (Model Context Protocol) is a standard plug for giving agents new tools: a browser, GitHub issues, a database, docs. **Install only servers you trust.** Anything an MCP server returns becomes context the agent may act on.

## Do it

Add the Playwright MCP server, which lets the agent drive a real browser. It needs Node.js 20+.

```bash
claude mcp add --scope project playwright -- npx @playwright/mcp@latest
```

`--scope project` writes the server to `.mcp.json`, so everyone who clones the repo gets it. Check its status with `/mcp`.

> **Native Windows (not WSL):** if the server fails to start, use `claude mcp add --scope project playwright -- cmd /c npx @playwright/mcp@latest`.

Load some demo data first:

```bash
python -m app.seed
```

Then ask:

> Start the API in the background with `uvicorn app.main:app`, open localhost:8000/docs, create an event with capacity 2, RSVP three different members to it, and tell me what happened.

This is end-to-end testing done by the agent itself.

## CLI or MCP?

If the GitHub CLI (`gh`) is installed, Claude can read issues with plain shell commands, for example `gh issue list` and `gh issue view 3`. No MCP server is needed for that. Knowing when a CLI beats an MCP server is part of the skill.

## Debrief

What could a malicious web page do if your agent visits it with a browser tool?
