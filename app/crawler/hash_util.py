import hashlib


class HashUtil:

    @staticmethod
    def generate_identity_hash(
        title: str,
        location: str,
        url: str
    ):

        value = (
            f"{title}|"
            f"{location}|"
            f"{url}"
        )

        return hashlib.sha256(
            value.encode()
        ).hexdigest()