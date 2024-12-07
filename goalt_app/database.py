from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from goalt_app.models import Base, User, Goal
from flask import current_app
from . import db



def create_session():
    engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
    Base.metadata.bind = engine
    session = sessionmaker(bind=engine)
    return session()

def create_user(username, password):
    session = create_session()
    user = User(username=username, password=password)
    session.add(user)
    session.commit()
    session.close()

def create_goal(title, description, user_id):
    session = create_session()
    goal = Goal(title=title, description=description, user_id=user_id)
    session.add(goal)
    session.commit()
    session.close()

def get_user(username):
    session = create_session()
    user = session.query(User).filter_by(username=username).first()
    session.close()
    return user

def get_users():
    session = create_session()
    users = session.query(User).all()
    session.close()
    return users