from sqlalchemy import select
from sqlalchemy.orm import Session

from database import Book, Chapter, Character, Movie, Quote


def get_books(db: Session):
    query = select(Book)
    return db.scalars(query)


def get_chapters(db: Session, book: str):
    query = select(Chapter).where(Chapter.book == book)
    return db.scalars(query)


def get_characters(db: Session, name: str = None, realm: str = None, gender: str = None):
    query = select(Character)
    if name:
        query.where(Character.name.contains(name))
    if realm:
        query.where(Character.realm.contains(realm))
    if gender:
        query.where(Character.gender.contains(gender))
    return db.scalars(query)


def get_movies(db: Session):
    query = select(Movie)
    return db.scalars(query)


def get_quotes(db: Session, dialog: str = None, movie: str = None, character: str = None):
    query = select(Quote)
    if dialog:
        query.where(Quote.dialog.contains(dialog))
    if movie:
        query.where(Quote.movie == movie)
    if character:
        query.where(Quote.character == character)
    return db.scalars(query)
