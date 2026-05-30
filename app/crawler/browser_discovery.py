import asyncio
import threading
from playwright.async_api import async_playwright


class BrowserDiscovery:

    @staticmethod
    async def capture_network(url: str):
        result = []
        exception = []

        def run_in_thread():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                result.extend(loop.run_until_complete(
                    BrowserDiscovery._playwright_task(url)
                ))
            except Exception as e:
                exception.append(e)
            finally:
                loop.close()

        thread = threading.Thread(target=run_in_thread)
        thread.start()
        thread.join()

        if exception:
            raise exception[0]

        return result

    @staticmethod
    async def _playwright_task(url: str):
        responses = []

        async with async_playwright() as p:

            browser = await p.chromium.launch(
                headless=True
            )

            page = await browser.new_page()

            async def handle_response(response):

                try:

                    responses.append({
                        "url": response.url,
                        "status": response.status,
                        "content_type": response.headers.get(
                            "content-type",
                            ""
                        )
                    })

                except Exception as e:

                    print(
                        f"Response Capture Error: {e}"
                    )

            page.on(
                "response",
                handle_response
            )

            await page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=60000
            )

            await browser.close()

        return responses