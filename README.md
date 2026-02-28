# Social Media Multi‑Agent System

Multi‑agent backend for social media management using FastAPI and Docker.

## Services

- Orchestrator – API gateway to other agents.
- Content Agent – generates post variants.
- Scheduler Agent – assigns posting times.
- Analytics Agent – stores posts & engagement, returns reports.

## Project Structure

```text
social_media_multiagent/
  orchestrator/
    main.py
    Dockerfile
  content_agent/
    main.py
    Dockerfile
  scheduler_agent/
    main.py
    Dockerfile
  analytics_agent/
    main.py
    Dockerfile
  shared/
    models.py
  requirements.txt
  docker-compose.yml
  README.md
  .gitignore
  docs/
    architecture.md
