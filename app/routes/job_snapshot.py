from fastapi import APIRouter

from app.service.job_snapshot_service import (
    JobSnapshotService
)

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.get("/exists/{job_id}")
def exists(job_id: str):

    return {
        "exists":
        JobSnapshotService.exists(
            job_id
        )
    }