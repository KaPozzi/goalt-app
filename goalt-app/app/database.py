from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=Config.SQLALCHEMY_ECHO)

Base = declarative_base

SessionLocal = sessionmaker(bind=engine)