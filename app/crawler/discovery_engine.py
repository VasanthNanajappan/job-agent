from app.crawler.job_source_discovery import (
    JobSourceDiscovery
)
from app.crawler.endpoint_validator import (
    EndpointValidator
)
from app.crawler.endpoint_probe_service import (
    EndpointProbeService
)


class DiscoveryEngine:

    @staticmethod
    async def discover(
        url: str
    ):

        source = (
            await JobSourceDiscovery
            .discover(url)
        )

        ranked = EndpointValidator.rank(
        source.get(
                "endpoint",
                []
            )
        )
        
        top_candidates = [
            item["endpoint"]
            for item in ranked[:5]
        ]

            
        probed = (
            await EndpointProbeService.probe(
                career_page_url=url,
                endpoints=top_candidates
            )
        )

        return {
            "career_page": url,
            "job_source": source,
            "ranked_endpoints": ranked[:10],
            "probed_endpoints": probed
        }