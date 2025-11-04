# Task Tracker API

A Django REST Framework application with Celery for asynchronous task processing.

## Features

- REST API for task management
- Asynchronous task processing with Celery
- Automatic cleanup of old completed tasks using Celery Beat
- Dockerized with Docker Compose

## Setup

### Prerequisites

- Docker and Docker Compose
- Python 3.11+ (for local development)

### Installation

1. Clone the repository
2. Install pre-commit hooks (optional but recommended):
   ```bash
   pip install pre-commit
   pre-commit install
   ```

### Running with Docker Compose

1. Build and start all services:
   ```bash
   docker-compose up --build
   ```

2. Run migrations (in a new terminal):
   ```bash
   docker-compose exec web python manage.py migrate
   ```

3. Access the API at: http://localhost:8000/api/tasks/

### API Endpoints

- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/` - List all tasks
- `GET /api/tasks/<id>/` - Retrieve a single task
- `POST /api/tasks/<id>/complete/` - Trigger Celery job to process a task

### Example API Usage

Create a task:
```bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"title": "My Task", "description": "Task description"}'
```

List all tasks:
```bash
curl http://localhost:8000/api/tasks/
```

Complete a task:
```bash
curl -X POST http://localhost:8000/api/tasks/1/complete/
```

## Pre-commit Hooks

The project includes pre-commit hooks for code quality:
- **black**: Code formatting
- **flake8**: Linting
- **isort**: Import sorting

To install pre-commit hooks:
```bash
pip install pre-commit
pre-commit install
```

## Services

- **web**: Django application
- **db**: PostgreSQL database
- **redis**: Redis broker for Celery
- **celery**: Celery worker
- **celery-beat**: Celery Beat scheduler

