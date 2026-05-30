from fastapi import APIRouter

from app.crawler.job_discovery_service import (
    JobDiscoveryService
)

from app.crawler.browser_discovery import(
    BrowserDiscovery
)

from app.crawler.request_filter import(
    RequestFilter
)

from app.crawler.response_inspector import(
    ResponseInspector
)

router = APIRouter(
    prefix="/crawler",
    tags=["Crawler"]
)


@router.get("/discover")
async def discover(
    url: str
):

    return (
        await JobDiscoveryService
        .discover(url)
    )

@router.get("/network")
async def network(url: str):

    responses = (
        await BrowserDiscovery
        .capture_network(url)
    )

    filtered = (
        RequestFilter.filter(
            responses
        )
    )

    return {
        "count": len(filtered),
        "responses": filtered
    }


@router.get("/inspect")
async def inspect(url: str):

    return await (
        ResponseInspector
        .inspect(url)
    )