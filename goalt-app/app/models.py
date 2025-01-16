from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base, engine

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(80), nullable=False, unique=True)
    password = Column(String(120), nullable=False)


    def __init__(self, username, password):
        self.username = username
        self.password = password


Base.metadata.create_all(bind=engine)
