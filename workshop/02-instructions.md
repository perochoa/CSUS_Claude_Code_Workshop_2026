# M2: Project Instructions (15 min)

**Goal:** write instruction files that change what the AI produces, in ways you can measure.

## Concept

`CLAUDE.md` files load into every session, so the AI stops re-guessing your stack and conventions. Short, specific, command-oriented rules beat long, aspirational ones.

## Do it

1. In Claude Code, run `/init` to generate a draft `CLAUDE.md`.
2. Edit it down to something like this:

   ```markdown
   # CSUS Event Hub

   ## Stack
   - Python 3.11+, FastAPI, SQLModel, SQLite
   - Tests: pytest, using the `client` and `session` fixtures in tests/conftest.py

   ## Commands
   - `pytest` runs everything; `pytest tests/test_rsvps.py -k <name>` runs one test
   - `ruff check --fix .` lints; `ruff format .` formats
   - `uvicorn app.main:app --reload` runs the API

   ## Conventions
   - Routes stay thin; business logic lives in app/services/
   - Every new endpoint gets tests in tests/
   - Raise HTTPException(404) for missing records; never return None
   - Use timezone-aware UTC datetimes everywhere

   ## Don't
   - Don't edit .env files or add dependencies without asking
   ```

3. Add a **scoped** instruction file at `tests/CLAUDE.md`. Claude pulls it in when it works on files in that folder:

   ```markdown
   # Test conventions
   - Reuse the `client`, `session`, `make_event`, and `make_member` fixtures; never start a real server
   - One behaviour per test; name tests test_<action>_<expected_result>
   ```

4. Try `/memory` to open and edit these files mid-session. Also try an `@path` import such as `@README.md`, which pulls a longer doc into `CLAUDE.md` without pasting it in.

## Exercise (6 min): feature development

Commit first, then ask:

> Add an `upcoming=true` query filter to GET /events.

Check the result:

- [ ] Is the logic in `app/services/`, not in the route?
- [ ] Does it compare against a timezone-aware UTC "now"?
- [ ] Did it write a test?

If any answer is no, tighten `CLAUDE.md`, `/rewind`, and run it again.

## Debrief

> If you correct the AI the same way twice, that correction belongs in the instruction file.
