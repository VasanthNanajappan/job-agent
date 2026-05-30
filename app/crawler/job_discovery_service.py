from app.crawler.discovery_engine import (
    DiscoveryEngine
)


class JobDiscoveryService:

    @staticmethod
    async def discover(
        url: str
    ):

        return await DiscoveryEngine.discover(
            url
        )