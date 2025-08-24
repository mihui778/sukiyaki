from pydantic import BaseModel


class CategoryOut(BaseModel):
    id: int
    name: str
    # name: str = Field(alias="imya")


class CategoryIn(BaseModel):
    name: str
