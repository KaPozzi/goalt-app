import sqlalchemy
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False)
    password = Column(String(50), nullable=False)

class Goal(Base):
    __tablename__ = 'goal'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=True)
    description = Column(String, nullable=True)
    progress = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

# from . import db

# class User(db.model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), nullable=False, unique=True)
#     password = db.Column(db.String(50), nullable=False)

# class Goal(db.model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50), nullable=False)
#     description = db.Column(db.Text(200), nullable=False)
#     progress = db.Column(db.Integer, default=0)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)