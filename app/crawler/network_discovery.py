import re

from bs4 import BeautifulSoup


class NetworkDiscovery:

    API_PATTERNS = [

        r'["\'](\/api\/[^"\']+)["\']',

        r'["\'](\/graphql[^"\']*)["\']',

        r'["\'](\/search[^"\']*)["\']',

        r'["\']([^"\']*jobs[^"\']*)["\']'
    ]

    @staticmethod
    def discover(html: str):

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        endpoints = set()

        # ---------------------------------
        # Script Inspection
        # ---------------------------------

        scripts = soup.find_all("script")

        for script in scripts:

            content = script.string

            if not content:
                continue

            for pattern in (
                NetworkDiscovery.API_PATTERNS
            ):

                matches = re.findall(
                    pattern,
                    content,
                    re.IGNORECASE
                )

                for match in matches:

                    endpoints.add(match)

        # ---------------------------------
        # Data Attributes
        # ---------------------------------

        ajax_elements = soup.find_all(
            attrs={
                "data-ajax-url": True
            }
        )

        for element in ajax_elements:

            endpoint = element.get(
                "data-ajax-url"
            )

            if endpoint:

                endpoints.add(
                    endpoint
                )

        return list(endpoints)