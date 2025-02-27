# Run this file once to create the database and tables

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from goalt_app.models import Base, User, Goal
from goalt_app.secrets import get_secret

# Creating the engine and connection programaticatlly
conf = {
    'host': 'resources.czmo2wqo0w7e.us-east-1.rds.amazonaws.com',
    'port': '5432',
    'database': 'resources',
    'user': 'Stephen',
    'password': get_secret['password']
}

# Added the URL to the engine
engine = create_engine('postgresql://{user}:{password}@{host}:{port}/{database}'.format(**conf))
#delete database if it already exists
Base.metadata.drop_all(engine)
# grab those models and create them in the local db file
Base.metadata.create_all(engine)

