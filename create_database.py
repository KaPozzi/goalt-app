# Run this file once to create the database and tables

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from goalt_app.models import Base, User, Goal


engine = create_engine('sqlite:///test.db')

# grab those models and create them in the local db file
Base.metadata.create_all(engine)