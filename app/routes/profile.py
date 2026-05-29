from fastapi import APIRouter

from app.matcher.profile_service import (
    ProfileService
)

router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)


@router.post("/generate-embedding")
def generate_embedding():

    return (
        ProfileService
        .generate_profile_embedding()
    )