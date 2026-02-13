# Social-Media-Manager-Agent
Autonomous, multi-agent backend for social media management using FastAPI and Docker.
The system has separate agents for content generation, scheduling, and analytics, all coordinated by an orchestrator service.

---

## Features

- **Multi‑agent architecture** with clear separation of concerns.
- **Content Agent** to generate multiple post variants per campaign.
- **Scheduler Agent** to assign posting times to posts.
- **Analytics Agent** to track engagement and compute basic reports.
- **Orchestrator** that exposes a single public API and calls all other agents.
- **Docker Compose** setup for one‑command local deployment.

---

## Architecture

Services:

- `orchestrator`  
  - Public API gateway.  
  - Coordinates calls to other agents.  
  - Registers posts and forwards engagement events.

- `content_agent`  
  - Accepts a campaign request and generates platform‑specific post variants.  
  - Ready to be extended with LLM calls.

- `scheduler_agent`  
  - Accepts generated posts and assigns scheduled times.  
  - Currently uses a simple “1 hour apart” rule.

- `analytics_agent`  
  - Stores posts and engagement events (in memory for demo).  
  - Returns total posts, average engagement, and top posts.
