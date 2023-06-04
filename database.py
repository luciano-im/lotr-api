from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

DATABASE_URL = 'sqlite+pysqlite:///db/lotr.db'

# Declare the SQLite database engine
engine = create_engine(DATABASE_URL, echo=True, connect_args={'check_same_thread': False})

# Session to interact with the database
# Each instance of the SessionLocal class will be a database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Class to autoload the existing database tables
Base = automap_base()

# Reflect the tables
Base.prepare(autoload_with=engine)

# Map a model to each table
Book = Base.classes.books
Chapter = Base.classes.chapters
Character = Base.classes.characters
Movie = Base.classes.movies
Quote = Base.classes.quotes