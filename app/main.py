from fastapi import FastAPI

from app.routes.career_pages import router as career_router

app = FastAPI(
    title="Job Monitoring Agent",
    version="1.0.0"
)

app.include_router(career_router)


@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "job-monitoring-agent"
    }