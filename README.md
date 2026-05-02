# Freelance Automation Backend

Django backend scaffold for a freelance automation system that can ingest jobs from platforms such as Upwork, Fiverr, and Freelancer, normalize them, score them with AI services, and prepare bidding workflows.

This repository is currently a base architecture. It includes a working Django project shell, a first database model, Django REST Framework endpoints, Docker support, and service/adaptor layers that are ready for expansion.

## Tech Stack

- Python 3.11+
- Django 5
- Django REST Framework
- SQLite for local development
- Docker and Docker Compose for containerized startup

## Project Goals

The structure is designed to support these responsibilities:

- Pull opportunities from freelance platforms
- Normalize raw platform payloads into a shared internal model
- Score opportunities with AI logic
- Prepare bid/proposal workflows
- Run ingestion and AI processing in background workers
- Expose internal operations through API endpoints

## Project Structure

```text
.
|-- app
|   |-- core
|   |   |-- config.py
|   |   `-- logger.py
|   |-- platforms
|   |   |-- upwork.py
|   |   |-- fiverr.py
|   |   `-- freelancer.py
|   |-- strategies
|   |   |-- api.py
|   |   |-- scraper.py
|   |   `-- notifications.py
|   |-- adapters
|   |   |-- upwork_adapter.py
|   |   |-- fiverr_adapter.py
|   |   `-- freelancer_adapter.py
|   |-- services
|   |   |-- ingestion_service.py
|   |   |-- ai_service.py
|   |   `-- bidding_service.py
|   |-- workers
|   |   |-- ingestion_worker.py
|   |   `-- ai_worker.py
|   |-- db
|   |   |-- models.py
|   |   `-- repository.py
|   |-- api
|   |   `-- routes.py
|   |-- utils
|   |   `-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   `-- models.py
|-- backend
|   |-- settings.py
|   |-- urls.py
|   |-- asgi.py
|   `-- wsgi.py
|-- manage.py
|-- Dockerfile
|-- docker-compose.yml
|-- .env.example
|-- .gitignore
`-- requirements.txt
```

## Architecture Overview

### `app/core`

Shared application concerns.

- `config.py`: environment-driven application settings
- `logger.py`: logging helpers and centralized logging setup

### `app/platforms`

Raw platform clients live here.

- `upwork.py`: Upwork client entry point
- `fiverr.py`: Fiverr client entry point
- `freelancer.py`: Freelancer client entry point

These files should eventually contain HTTP clients, authentication, rate-limit handling, pagination, and platform-specific request logic.

### `app/strategies`

Execution strategies define how data is collected or delivered.

- `api.py`: fetch opportunities through official APIs
- `scraper.py`: fetch opportunities through scraping workflows
- `notifications.py`: notification formatting and dispatch logic

This layer is useful when one platform supports multiple acquisition methods.

### `app/adapters`

Adapters convert platform-specific payloads into the common internal model.

- `upwork_adapter.py`
- `fiverr_adapter.py`
- `freelancer_adapter.py`

This separation keeps platform quirks away from the service layer.

### `app/services`

Core business orchestration.

- `ingestion_service.py`: takes raw jobs and stores normalized opportunities
- `ai_service.py`: scores opportunities and produces AI summaries
- `bidding_service.py`: creates proposal/bidding payloads from opportunities

### `app/workers`

Background execution layer.

- `ingestion_worker.py`: runs ingestion batches
- `ai_worker.py`: runs AI scoring jobs

These can later be moved behind Celery, Django Q, RQ, or cron-based execution.

### `app/db`

Persistence and repository logic.

- `models.py`: Django ORM models and domain support objects
- `repository.py`: repository abstraction and Django ORM implementation

### `app/api`

HTTP entry points.

- `routes.py`: Django REST Framework views and URL patterns for the current API
- `serializers.py`: request validation for API payloads

### `backend`

This is the Django project wrapper.

- `settings.py`: Django configuration
- `urls.py`: root URL configuration
- `asgi.py` and `wsgi.py`: deployment entry points

## Current Implementation Status

The scaffold currently includes:

- Django project configuration
- One main persisted model: `Opportunity`
- Django admin registration for `Opportunity`
- Repository implementation using Django ORM
- Three DRF JSON endpoints under `/api/`
- Docker and Compose files for local container startup
- Base service, adapter, strategy, worker, and platform modules

The scaffold does not yet include:

- Authentication or permissions
- Real platform API integration
- Background queue integration
- Tests
- Production settings split

## Data Model

### `Opportunity`

Stored in `app/db/models.py`.

Fields:

- `external_id`: unique platform identifier
- `platform`: source platform name
- `title`: opportunity title
- `description`: opportunity body or summary
- `budget`: optional budget text
- `url`: source URL
- `metadata`: raw or normalized JSON payload
- `processed`: whether the opportunity has already gone through downstream logic
- `created_at`: creation timestamp

## API Endpoints

Base prefix: `/api/`

### `GET /api/health/`

Returns service health status.

Example response:

```json
{
  "status": "ok"
}
```

### `POST /api/ingest/`

Placeholder endpoint for ingestion triggers.

Example response:

```json
{
  "message": "Ingestion endpoint initialized",
  "service": "IngestionService"
}
```

### `POST /api/bids/evaluate/`

Builds a preview bid/proposal response for a submitted opportunity payload.

Example request:

```json
{
  "external_id": "job-123",
  "platform": "upwork",
  "title": "Build a Django backend",
  "description": "Need a backend engineer for a job marketplace automation tool.",
  "budget": "$500",
  "url": "https://example.com/jobs/job-123",
  "metadata": {
    "category": "web development"
  }
}
```

Example response:

```json
{
  "proposal": "Proposal for Build a Django backend: recommended score 0.80."
}
```

Validation for this endpoint is handled by `app/api/serializers.py`.

## Setup

### 1. Create a virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Create environment file

```powershell
Copy-Item .env.example .env
```

### 4. Create database migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser

```powershell
python manage.py createsuperuser
```

### 6. Run the server

```powershell
python manage.py runserver
```

Admin panel:

- `http://127.0.0.1:8000/admin/`

API base:

- `http://127.0.0.1:8000/api/`

## Environment Variables

The project currently reads these environment variables:

| Variable | Default | Purpose |
|---|---|---|
| `DJANGO_SECRET_KEY` | `django-insecure-change-me` | Django secret key |
| `DJANGO_DEBUG` | `true` | Enables Django debug mode |
| `DJANGO_ALLOWED_HOSTS` | `*` | Comma-separated allowed hosts |
| `APP_ENV` | `development` | Application environment label |
| `LOG_LEVEL` | `INFO` | Root logging level |
| `POLLING_INTERVAL_SECONDS` | `60` | Default worker polling interval |
| `NOTIFICATION_WEBHOOK` | empty | Placeholder notification target |
| `TIME_ZONE` | `UTC` | Django timezone |

PowerShell example:

```powershell
$env:DJANGO_SECRET_KEY="replace-this"
$env:DJANGO_DEBUG="true"
$env:LOG_LEVEL="DEBUG"
```

## Docker

### Build and run

```powershell
docker compose up --build
```

The container startup command runs migrations and then starts Gunicorn on port `8000`.

### Notes

- Copy `.env.example` to `.env` before using Docker Compose
- The current container setup is intended for local development and basic deployment use
- SQLite remains the default database inside the container

## Development Workflow

Recommended order for building out the backend:

1. Replace placeholder platform clients in `app/platforms/` with real integrations.
2. Expand adapters so every platform maps into a stable internal schema.
3. Extend the existing DRF layer with authentication, permissions, and richer serializers.
4. Introduce service tests and API tests.
5. Add async/background job support for ingestion and AI processing.
6. Split settings into `base.py`, `local.py`, and `production.py` when deployment starts.

## Suggested Next Improvements

- Add `pytest` and Django test coverage
- Add `.env` loading with `python-dotenv` or `django-environ`
- Add authentication and permission classes for DRF endpoints
- Add Celery and Redis for background workers
- Add structured logging and error monitoring
- Add separate apps if the codebase grows too large for a single `app` package

## Notes

- `app/models.py` exists as a bridge so Django can discover models defined in `app/db/models.py`.
- `app/api/routes.py` is included from `backend/urls.py` under the `/api/` prefix.
- The current repository uses SQLite to keep local startup simple.
- `.gitignore` excludes local database files, Python build artifacts, and environment files.

## License

Add your preferred license before publishing or deploying this project.
