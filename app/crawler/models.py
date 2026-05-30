from pydantic import BaseModel


class Job(BaseModel):
    identity_hash: str
    title: str
    location: str
    url: str