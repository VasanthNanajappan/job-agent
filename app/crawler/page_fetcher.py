import httpx


class PageFetcher:

    @staticmethod
    async def fetch(url: str):

        async with httpx.AsyncClient(
            timeout=30
        ) as client:

            response = await client.get(
                url,
                headers={
                    "User-Agent":
                    "Mozilla/5.0"
                }
            )

            response.raise_for_status()

            return response.text