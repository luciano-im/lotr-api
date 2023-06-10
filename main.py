from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from schemas import BookScheme, ChapterScheme, CharacterScheme, MovieScheme, QuoteScheme
from enumerations import Gender, Realm, Race
from crud import get_books, get_book, get_chapters, get_characters, get_movies, get_quotes
from database import SessionLocal


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
    return {"message": "Welcome to The Lord Of The Rings API"}


@app.get("/books/", response_model=list[BookScheme])
async def books(db: Session = Depends(get_db)):
    books = get_books(db)
    return list(books)


@app.get("/chapters/{book}", response_model=list[ChapterScheme])
async def chapters(book: str, db: Session = Depends(get_db)):
    book_exists = get_book(db, book)
    if len(list(book_exists)) == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    chapters = get_chapters(db, book=book)
    return list(chapters)


@app.get("/characters/", response_model=list[CharacterScheme])
async def characters(name: str = "", realm: Realm = None, gender: Gender = None, race: Race = None, db: Session = Depends(get_db)):
    realm_value = realm.value if realm else None
    gender_value = gender.value if gender else None
    race_value = race.value if race else None
    characters = get_characters(db, name=name, realm=realm_value, gender=gender_value, race=race_value)
    return list(characters)


@app.get("/movies/", response_model=list[MovieScheme])
async def movies(db: Session = Depends(get_db)):
    movies = get_movies(db)
    return list(movies)


@app.get("/quotes/", response_model=list[QuoteScheme])
async def quotes(dialog: str = None, movie: str = None, character: str = None, db: Session = Depends(get_db)):
    quotes = get_quotes(db, dialog=dialog, movie=movie, character=character)
    return list(quotes)


@app.get("/realm/", response_model=list[str])
async def realm():
    realm = [r.value for r in Realm]
    return realm


@app.get("/gender/", response_model=list[str])
async def gender():
    gender = [r.value for r in Gender]
    return gender


@app.get("/race/", response_model=list[str])
async def race():
    race = [r.value for r in Race]
    return race