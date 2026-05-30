import asyncio
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

from fastapi import FastAPI

from app.routes.career_pages import router as career_router
from app.routes.profile import router as profile_router
from app.routes.matcher import router as matcher_router
from app.routes.slack import router as slack_router
from app.routes.job_snapshot import router as job_snapshot_router
from app.routes.crawl_router import router as crawler

app = FastAPI(
    title="Job Monitoring Agent",
    version="1.0.0"
)

app.include_router(career_router)
app.include_router(profile_router)
app.include_router(matcher_router)
app.include_router(slack_router)
app.include_router(job_snapshot_router)
app.include_router(crawler)


@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "job-monitoring-agent"
    }