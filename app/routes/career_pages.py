from fastapi import APIRouter

from app.models.career_pages import CareerPageCreate
from app.service.career_pages import CareerPageService

router = APIRouter(
    prefix="/career-pages",
    tags=["Career Pages"]
)


@router.post("")
def create_career_page(
    payload: CareerPageCreate
):
    return CareerPageService.create(payload)


@router.get("")
def list_career_pages():
    return CareerPageService.get_all()