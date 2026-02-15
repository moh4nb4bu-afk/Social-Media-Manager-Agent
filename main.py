from fastapi import FastAPI
from typing import List
from datetime import datetime, timedelta

from shared.models import ScheduleRequest, ScheduledPost

app = FastAPI(title="Scheduler Agent")


@app.post("/schedule-posts", response_model=List[ScheduledPost])
async def schedule_posts(req: ScheduleRequest):
    base = datetime.utcnow()
    scheduled: List[ScheduledPost] = []

    # Simple rule: 1 hour apart from now
    for idx, post in enumerate(req.posts):
        scheduled_time = base + timedelta(hours=idx + 1)
        scheduled.append(
            ScheduledPost(
                id=post.id,
                platform=post.platform,
                content=post.content,
                scheduled_time=scheduled_time,
            )
        )

    return scheduled
