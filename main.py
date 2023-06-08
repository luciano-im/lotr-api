from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from schemas import BookScheme, ChapterScheme, CharacterScheme, MovieScheme, QuoteScheme
from crud import get_books, get_chapters, get_characters, get_movies, get_quotes
from database import SessionLocal

from enum import Enum

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/books/", response_model=list[BookScheme])
async def books(db: Session = Depends(get_db)):
    books = get_books(db)
    return list(books)


@app.get("/chapters/{book}", response_model=list[ChapterScheme])
async def chapters(book: str, db: Session = Depends(get_db)):
    chapters = get_chapters(db, book=book)
    return list(chapters)


@app.get("/characters/", response_model=list[CharacterScheme])
async def characters(name: str = "", realm: str = None, gender: str = None, race: str = None, db: Session = Depends(get_db)):
    characters = get_characters(db, name=name, realm=realm, gender=gender, race=race)
    return list(characters)


@app.get("/movies/", response_model=list[MovieScheme])
async def movies(db: Session = Depends(get_db)):
    movies = get_movies(db)
    return list(movies)


@app.get("/quotes/", response_model=list[QuoteScheme])
async def quotes(dialog: str = None, movie: str = None, character: str = None, db: Session = Depends(get_db)):
    quotes = get_quotes(db, dialog=dialog, movie=movie, character=character)
    return list(quotes)