# The Lord Of The Rings API

This is a side project I've developed to learn to use FastAPI, Pydantic and Poetry

## Poetry

https://python-poetry.org/docs/

Steps:

1. Install poetry
2. Add poetry to $PATH environment variable
3. Setup poetry to create virtual envs in project folder: poetry config virtualenvs.in-project true
4. Initialize poetry project with: poetry init
5. Install dependencies with: poetry add package-name
6. Activate the virtual environment with: poetry shell
7. Run the script with: poetry run python script_file.py


## SQLAlchemy

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper (ORM) that gives application developers the full power and flexibility of SQL.

SQLAlchemy is the ORM I use to communicate with SQLite. The automap_base() function automatically generates mapped classes and relationships from a database schema.


## Pydantic

Data validation and settings management using Python type annotations. pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid.

Pydantic models receive data, and after parsing and validation pydantic guarantees that the fields of the resultant model instance will conform to the field types defined on the SQLAlchemy model.