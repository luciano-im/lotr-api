from sqlalchemy import select
from sqlalchemy.orm import Session

from database import Book, Chapter, Character, Movie, Quote


def get_books(db: Session):
    query = select(Book)
    return db.scalars(query)


def get_book(db: Session, book: str):
    query = select(Book).where(Book._id == book)
    return db.scalars(query)


def get_chapters(db: Session, book: str):
    query = select(Chapter).where(Chapter.book == book)
    return db.scalars(query)


def get_characters(db: Session, name: str = None, realm: str = None, gender: str = None, race: str = None):
    filters = []
    if name:
        filters.append(Character.name.contains(name))
    if realm:
        filters.append(Character.realm.contains(realm))
    if gender:
        filters.append(Character.gender == gender)
    if race:
        filters.append(Character.race == race)
    query = select(Character).where(*filters)
    return db.scalars(query)


def get_character(db: Session, character: str):
    query = select(Character).where(Character._id == character)
    return db.scalars(query)


def get_movies(db: Session):
    query = select(Movie)
    return db.scalars(query)


def get_quotes(db: Session, dialog: str = None, movie: str = None, character: str = None):
    filters = []
    if dialog:
        filters.append(Quote.dialog.contains(dialog))
    if movie:
        filters.append(Quote.movie == movie)
    if character:
        filters.append(Quote.character == character)
    query = select(Quote).where(*filters)
    return db.scalars(query)
