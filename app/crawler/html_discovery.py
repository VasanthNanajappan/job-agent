from bs4 import BeautifulSoup

from app.crawler.hash_util import (
    HashUtil
)


class HTMLJobDiscovery:

    @staticmethod
    def discover(
        html: str,
        base_url: str
    ):

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        jobs = []

        job_items = soup.find_all(
            "li",
            attrs={
                "data-intuit-jobid": True
            }
        )

        for item in job_items:

            job_id = item.get(
                "data-intuit-jobid"
            )

            location = item.get(
                "data-org-location",
                ""
            )

            link = item.find("a")

            if not link:
                continue

            title = (
                link.get_text(
                    strip=True
                )
            )

            href = link.get("href")

            if not href:
                continue

            if href.startswith("/"):

                url = (
                    base_url.rstrip("/")
                    + href
                )

            else:
                url = href

            identity_hash = (
                HashUtil
                .generate_identity_hash(
                    title=title,
                    location=location,
                    url=url
                )
            )

            jobs.append({
                "identity_hash":
                    identity_hash,

                "job_id":
                    job_id,

                "title":
                    title,

                "location":
                    location,

                "url":
                    url,

                "description":
                    ""
            })

        return jobs