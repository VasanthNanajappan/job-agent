from urllib.parse import urljoin

import httpx


class EndpointProbeService:

    JOB_KEYS = [
        "job",
        "jobs",
        "title",
        "location",
        "description",
        "job_id",
        "jobid"
    ]

    @staticmethod
    async def probe(
        career_page_url: str,
        endpoints: list[str]
    ):

        results = []

        async with httpx.AsyncClient(
            timeout=15,
            follow_redirects=True
        ) as client:

            for endpoint in endpoints:

                try:

                    # -----------------------
                    # Ignore garbage entries
                    # -----------------------

                    if " " in endpoint:
                        continue

                    if len(endpoint) < 3:
                        continue

                    full_url = urljoin(
                        career_page_url,
                        endpoint
                    )

                    response = await client.get(
                        full_url,
                        headers={
                            "User-Agent":
                            "Mozilla/5.0"
                        }
                    )

                    content_type = (
                        response.headers.get(
                            "content-type",
                            ""
                        )
                    )

                    looks_like_jobs = False

                    body = response.text.lower()

                    for key in (
                        EndpointProbeService
                        .JOB_KEYS
                    ):

                        if key in body:
                            looks_like_jobs = True
                            break

                    results.append({
                        "endpoint":
                            endpoint,

                        "full_url":
                            full_url,

                        "status_code":
                            response.status_code,

                        "content_type":
                            content_type,

                        "looks_like_jobs":
                            looks_like_jobs
                    })

                except Exception:

                    continue

        return results