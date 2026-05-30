class RequestFilter:

    KEYWORDS = [
        "job",
        "jobs",
        "career",
        "search",
        "graphql",
        "/rest/"
    ]

    @staticmethod
    def filter(responses):

        filtered = []

        for item in responses:

            url = item["url"].lower()

            content_type = (
                item["content_type"]
                .lower()
            )

            if "json" in content_type:

                filtered.append(item)
                continue

            if any(
                keyword in url
                for keyword in (
                    RequestFilter.KEYWORDS
                )
            ):

                filtered.append(item)

        return filtered