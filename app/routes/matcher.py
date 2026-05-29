from fastapi import APIRouter
from pydantic import BaseModel

from app.matcher.job_matcher import (
    JobMatcher
)

router = APIRouter(
    prefix="/matcher",
    tags=["Matcher"]
)


class MatchRequest(BaseModel):
    job_description: str


@router.post("/test")
def test_match(
    payload: MatchRequest
):
    return JobMatcher.match(
        payload.job_description
    )