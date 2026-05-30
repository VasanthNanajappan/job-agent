from bs4 import BeautifulSoup

from app.crawler.page_fetcher import (
    PageFetcher
)

from app.crawler.network_discovery import (
    NetworkDiscovery
)


class JobSourceDiscovery:

    @staticmethod
    async def discover(url: str):

        html = await PageFetcher.fetch(url)

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        html_lower = html.lower()

        # ------------------------------------------------
        # GraphQL Detection
        # ------------------------------------------------

        graphql_indicators = [
            "graphql",
            "__apollo_state__",
            "apollo-client"
        ]

        for indicator in graphql_indicators:

            if indicator in html_lower:

                return {
                    "source_type": "GRAPHQL",
                    "endpoint": "/graphql"
                }

        # ------------------------------------------------
        # AJAX Detection
        # ------------------------------------------------

        ajax_elements = soup.find_all(
            attrs={
                "data-ajax-url": True
            }
        )

        if ajax_elements:

            endpoint = ajax_elements[0].get(
                "data-ajax-url"
            )

            return {
                "source_type": "AJAX",
                "endpoint": endpoint
            }

        # ------------------------------------------------
        # API Detection
        # ------------------------------------------------

        api_patterns = [
            "/api/",
            "jobs-api",
            "application/json"
        ]
        candidate_endpoints = (
            NetworkDiscovery.discover(
                html
            )
        )

        for pattern in api_patterns:

            if pattern in html_lower:

                return {
                    "source_type": "API",
                    "endpoint": candidate_endpoints
                }

        # ------------------------------------------------
        # HTML Fallback
        # ------------------------------------------------

        return {
            "source_type": "HTML",
            "endpoint": None
        }