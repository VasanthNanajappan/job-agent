import uuid
import pandas as pd
from pathlib import Path

CSV_PATH = "data/career_pages.csv"

COLUMNS = [
    "id",
    "company",
    "url",
    "platform",
    "enabled"
]


class CareerPageService:

    @staticmethod
    def _initialize_csv():
        """
        Create CSV with proper headers if it doesn't exist.
        """
        if not Path(CSV_PATH).exists():
            df = pd.DataFrame(columns=COLUMNS)
            df.to_csv(CSV_PATH, index=False)

    @staticmethod
    def get_all():
        try:
            CareerPageService._initialize_csv()

            df = pd.read_csv(CSV_PATH)

            df = df.fillna("")

            return df.to_dict(orient="records")

        except Exception as e:
            print(f"Error reading CSV: {e}")
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