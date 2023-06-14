from pydantic import BaseModel, Field


class BookScheme(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True

class ChapterScheme(BaseModel):
    id: str
    chapter_name: str
    book: str

    class Config:
        orm_mode = True

class CharacterScheme(BaseModel):
    id: str
    name: str
    wiki_url: str | None = Field(default=None)
    race: str | None = None
    birth: str | None = None
    gender: str | None = None
    death: str | None = None
    hair: str | None = None
    height: str | None = None
    realm: str | None = None
    spouse: str | None = None

    class Config:
        orm_mode = True

class MovieScheme(BaseModel):
    id: str
    name: str
    runtime_minutes: int
    budget_millions: int
    revenue_millions: int
    award_nominations: int
    award_wins: int
    rotten_tomatoes_score: float

    class Config:
        orm_mode = True

class QuoteScheme(BaseModel):
    id: str
    dialog: str | None
    movie: str
    character: str

    class Config:
        orm_mode = True