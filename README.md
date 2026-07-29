# KnowledgeHub AI

FastAPI backend for KnowledgeHub AI.

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
uv sync
```

Optional: copy environment defaults into `.env`:

```env
APP_NAME=KnowledgeHub AI
APP_VERSION=0.1.0
ENVIRONMENT=development
```

## Run

```bash
uv run uvicorn app.main:app --reload
```

- API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Health: [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

Example response:

```json
{
  "status": "healthy",
  "version": "0.1.0",
  "app_name": "KnowledgeHub AI"
}
```

## Test

```bash
uv run pytest
```

## Project layout

```text
app/
  main.py              # FastAPI application
  api/v1/              # Versioned HTTP routes
  core/                # Config, shared infrastructure
  schemas/             # Pydantic request/response models
  services/            # Business logic (future)
  models/              # Domain / persistence models (future)
  dependencies/        # FastAPI dependencies (future)
  middleware/          # HTTP middleware (future)
  utils/               # Shared helpers (future)
tests/                 # Pytest suite
```

## Stack

- FastAPI + Uvicorn
- Pydantic Settings
- Pytest + httpx2 (`TestClient`)
- uv for packaging and environments
