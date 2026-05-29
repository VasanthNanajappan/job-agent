from pydantic import BaseModel, HttpUrl


class CareerPageCreate(BaseModel):
    company: str
    url: HttpUrl
    platform: str
    enabled: bool = True


class CareerPage(CareerPageCreate):
    id: str