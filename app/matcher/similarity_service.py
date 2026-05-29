from sklearn.metrics.pairwise import cosine_similarity


class SimilarityService:

    @staticmethod
    def calculate(
        profile_embedding,
        job_embedding
    ) -> float:

        score = cosine_similarity(
            [profile_embedding],
            [job_embedding]
        )[0][0]

        return float(score)