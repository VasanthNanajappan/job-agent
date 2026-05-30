import re


class EndpointValidator:

    JOB_KEYWORDS = [
        "job",
        "jobs",
        "career",
        "opening",
        "position",
        "vacancy",
        "search"
    ]

    IGNORE_KEYWORDS = [
        "auth",
        "login",
        "footer",
        "header",
        "passport",
        "account",
        "signin"
    ]

    @staticmethod
    def score(endpoint: str):

        endpoint_lower = endpoint.lower()

        score = 0

        # positive scoring

        for keyword in (
            EndpointValidator.JOB_KEYWORDS
        ):

            if keyword in endpoint_lower:
                score += 10

        # negative scoring

        for keyword in (
            EndpointValidator.IGNORE_KEYWORDS
        ):

            if keyword in endpoint_lower:
                score -= 20

        # API bonus

        if "/api/" in endpoint_lower:
            score += 30

        if "graphql" in endpoint_lower:
            score += 30

        return score

    @staticmethod
    def rank(endpoints):

        results = []

        for endpoint in endpoints:

            results.append(
                {
                    "endpoint": endpoint,
                    "score":
                        EndpointValidator
                        .score(endpoint)
                }
            )

        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return results