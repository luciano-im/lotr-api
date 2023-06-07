from pydantic import BaseModel, Field


class BookScheme(BaseModel):
    id: str = Field(alias='_id')
    name: str

    class Config:
        orm_mode = True

class ChapterScheme(BaseModel):
    id: str = Field(alias='_id')
    chapter_name: str = Field(alias='chapterName')
    book: str

    class Config:
        orm_mode = True

class CharacterScheme(BaseModel):
    id: str = Field(alias='_id')
    name: str
    wiki_url: str | None = Field(default=None, alias='wikiUrl')
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
    id: str = Field(alias='_id')
    name: str
    runtime_minutes: int = Field(alias='runtimeInMinutes')
    budget_millions: int = Field(alias='budgetInMillions')
    revenue_millions: int = Field(alias='boxOfficeRevenueInMillions')
    award_nominations: int = Field(alias='academyAwardNominations')
    award_wins: int = Field(alias='academyAwardWins')
    rotten_tomatoes_score: float = Field(alias='rottenTomatoesScore')

    class Config:
        orm_mode = True

class QuoteScheme(BaseModel):
    id: str = Field(alias='_id')
    dialog: str
    movie: str
    character: str

    class Config:
        orm_mode = True