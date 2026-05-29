import numpy as np

from app.matcher.embedding_service import (
    EmbeddingService
)

PROFILE_PATH = "data/profile.txt"

EMBEDDING_PATH = (
    "data/profile_embedding.npy"
)


class ProfileService:

    @staticmethod
    def generate_profile_embedding():

        with open(
            PROFILE_PATH,
            "r",
            encoding="utf-8"
        ) as f:
            profile_text = f.read()

        embedding = (
            EmbeddingService
            .generate_embedding(
                profile_text
            )
        )

        np.save(
            EMBEDDING_PATH,
            embedding
        )

        return {
            "status": "success",
            "dimensions": len(
                embedding
            )
        }

    @staticmethod
    def load_profile_embedding():

        return np.load(
            EMBEDDING_PATH
        )