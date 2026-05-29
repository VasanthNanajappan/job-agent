import pandas as pd
from pathlib import Path

SNAPSHOT_FILE = "data/jobs_snapshot.csv"


class JobSnapshotService:

    @staticmethod
    def initialize():

        if (
            not Path(SNAPSHOT_FILE).exists()
            or Path(SNAPSHOT_FILE).stat().st_size == 0
        ):

            pd.DataFrame(
                columns=[
                    "job_id",
                    "company",
                    "title",
                    "url",
                    "last_seen"
                ]
            ).to_csv(
                SNAPSHOT_FILE,
                index=False
            )

            
    @staticmethod
    def exists(job_id: str):

        df = pd.read_csv(
            SNAPSHOT_FILE
        )

        return (
            job_id in
            df["job_id"].astype(str).values
        )

    @staticmethod
    def add(job):

        df = pd.read_csv(
            SNAPSHOT_FILE
        )

        df = pd.concat(
            [
                df,
                pd.DataFrame([job])
            ],
            ignore_index=True
        )

        df.to_csv(
            SNAPSHOT_FILE,
            index=False
        )