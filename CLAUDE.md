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
