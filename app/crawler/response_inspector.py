import httpx


class ResponseInspector:

    @staticmethod
    async def inspect(url: str):

        async with httpx.AsyncClient(
            timeout=30
        ) as client:

            response = await client.get(url)

            content_type = (
                response.headers.get(
                    "content-type",
                    ""
                )
            )

            result = {
                "status_code":
                    response.status_code,

                "content_type":
                    content_type
            }

            if "json" in content_type:

                try:

                    data = response.json()

                    result["response_type"] = (
                        type(data).__name__
                    )

                    if isinstance(data, dict):

                        result["keys"] = (
                            list(data.keys())[:20]
                        )

                        jobs = data.get("jobs")

                        if isinstance(jobs, list):

                            result["job_count"] = len(jobs)

                            if jobs:

                                first_job = jobs[0]

                                if isinstance(
                                    first_job,
                                    dict
                                ):

                                    result["job_keys"] = list(
                                        first_job.keys()
                                    )

                                    result["sample_job"] = first_job

                    elif isinstance(data, list):

                        result["list_size"] = len(data)

                        if data:

                            first = data[0]

                            if isinstance(
                                first,
                                dict
                            ):

                                result[
                                    "first_item_keys"
                                ] = list(
                                    first.keys()
                                )[:20]

                except Exception as e:

                    result["error"] = str(e)

            return result