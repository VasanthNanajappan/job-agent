from fastapi import APIRouter

from app.notifier.slack_notifier import (
    SlackNotifier
)

router = APIRouter(
    prefix="/slack",
    tags=["Slack"]
)


@router.post("/test")
def test_slack():

    SlackNotifier.send(
        "🚀 Job Monitoring Agent Started"
    )

    return {
        "status": "sent"
    }