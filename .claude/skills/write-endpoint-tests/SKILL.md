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
