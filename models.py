from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime


class PostRequest(BaseModel):
    brand: str
    platform: str  # "twitter", "linkedin", "instagram"
    goal: str      # e.g., "promote new feature"
    topic: str     # e.g., "AI agents for social media"
    audience: str  # e.g., "developers", "marketers"


class GeneratedPost(BaseModel):
    id: str
    brand: str
    platform: str
    content: str
    scheduled_time: Optional[datetime] = None
    metadata: Dict = {}


class ScheduleRequest(BaseModel):
    brand: str
    platform: str
    posts: List[GeneratedPost]


class ScheduledPost(BaseModel):
    id: str
    platform: str
    content: str
    scheduled_time: datetime


class EngagementEvent(BaseModel):
    post_id: str
    platform: str
    likes: int
    comments: int
    shares: int
    timestamp: datetime


class AnalyticsReport(BaseModel):
    brand: str
    platform: str
    total_posts: int
    avg_engagement: float
    top_posts: List[GeneratedPost]
