import uuid
import pandas as pd

CSV_PATH = "data/career_pages.csv"

class CareerPageService:

    @staticmethod
    def get_all():
        try:
            df = pd.read_csv(CSV_PATH)

            df = df.fillna("")

            return df.to_dict("records")

        except Exception as e:
            print(e)
            return []

    @staticmethod
    def create(data):
        df = pd.read_csv(CSV_PATH)

        row = {
            "id": str(uuid.uuid4()),
            "company": data.company,
            "url": str(data.url),
            "platform": data.platform,
            "enabled": data.enabled,
        }

        df = pd.concat(
            [df, pd.DataFrame([row])],
            ignore_index=True
        )

        df.to_csv(CSV_PATH, index=False)

        return row