from app.matcher.embedding_service import (
    EmbeddingService
)

from app.matcher.profile_service import (
    ProfileService
)

from app.matcher.similarity_service import (
    SimilarityService
)


class JobMatcher:

    @staticmethod
    def match(job_text: str):

        profile_embedding = (
            ProfileService
            .load_profile_embedding()
        )

        job_embedding = (
            EmbeddingService
            .generate_embedding(job_text)
        )

        score = (
            SimilarityService
            .calculate(
                profile_embedding,
                job_embedding
            )
        )

        return {
            "similarity_score": round(score, 4),
            "is_match": score >= 0.5
        }