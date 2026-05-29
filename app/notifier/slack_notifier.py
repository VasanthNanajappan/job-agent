import os
import requests

from dotenv import load_dotenv

load_dotenv()


class SlackNotifier:

    @staticmethod
    def send(message: str):

        webhook_url = os.getenv(
            "SLACK_WEBHOOK_URL"
        )

        if not webhook_url:
            raise Exception(
                "Slack webhook missing"
            )

        response = requests.post(
            webhook_url,
            json={
                "text": message
            }
        )

        response.raise_for_status()

        return True