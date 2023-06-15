import os
import shutil
from fastapi import Depends, FastAPI, HTTPException, UploadFile
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from schemas import BookScheme, ChapterScheme, CharacterScheme, MovieScheme, QuoteScheme
from enumerations import Gender, Realm, Race
from crud import get_books, get_book, get_chapters, get_characters, get_character, update_character_picture, get_movies, get_quotes
from database import SessionLocal


app = FastAPI()

STATIC_FILES_DIRECTORY = os.path.join(os.path.dirname(__file__), 'static')
CHARACTER_PICTURE_DIRECTORY = os.path.join(STATIC_FILES_DIRECTORY, 'img', 'character-picture')

# Mount static files instance
app.mount("/static", StaticFiles(directory=STATIC_FILES_DIRECTORY), name="static")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_not_existing_object(db, function, entity, status_code, message):
    entity_exists = function(db, entity)
    if len(list(entity_exists)) == 0:
        raise HTTPException(status_code=status_code, detail=message)


def create_pictures_directory_if_not_exists():
    if not os.path.exists(CHARACTER_PICTURE_DIRECTORY):
        try:
            os.makedirs(CHARACTER_PICTURE_DIRECTORY)
        except OSError:
            raise HTTPException(status_code=500, detail="Pictures directory don't exists")


@app.get("/")
async def root():
    return {"detail": "Welcome to The Lord Of The Rings API"}


@app.get("/books/", response_model=list[BookScheme])
async def books(db: Session = Depends(get_db)):
    books = get_books(db)
    return list(books)


@app.get("/chapters/{book}", response_model=list[ChapterScheme])
async def chapters(book: str, db: Session = Depends(get_db)):
    check_not_existing_object(db=db, function=get_book, entity=book, status_code=404, message="Book not found")
    chapters = get_chapters(db, book=book)
    return list(chapters)


@app.get("/characters/", response_model=list[CharacterScheme])
async def characters(name: str = "", realm: Realm = None, gender: Gender = None, race: Race = None, db: Session = Depends(get_db)):
    realm_value = realm.value if realm else None
    gender_value = gender.value if gender else None
    race_value = race.value if race else None
    characters = get_characters(db, name=name, realm=realm_value, gender=gender_value, race=race_value)
    return list(characters)


# Return a 204 status code (No Content)
@app.post("/characters/{character}/picture", status_code=204)
async def upload_character_picture(character: str, file: UploadFile, db: Session = Depends(get_db)):
    check_not_existing_object(db=db, function=get_character, entity=character, status_code=404, message="Character not found")
    create_pictures_directory_if_not_exists()
    
    filename = character + os.path.splitext(file.filename)[1]
    file_path = os.path.join(CHARACTER_PICTURE_DIRECTORY, filename)
    with open(file_path, 'wb') as destination:
        try:
            shutil.copyfileobj(file.file, destination)
            update_character_picture(db, character, filename)
        except:
            raise HTTPException(status_code=500, detail="Picture couldn't be uploaded")


@app.delete("/characters/{character}/picture", status_code=204)
async def delete_character_picture(character: str, db: Session = Depends(get_db)):
    check_not_existing_object(db=db, function=get_character, entity=character, status_code=404, message="Character not found")
    create_pictures_directory_if_not_exists
    
    filename = f'{character}.jpg'
    file_path = os.path.join(CHARACTER_PICTURE_DIRECTORY, filename)
    try:
        os.remove(file_path)
        update_character_picture(db, character, None)
    except:
        raise HTTPException(status_code=500, detail="Picture couldn't be deleted")


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