from flask import Flask
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://master:Sucesso_24@localhost:3306/goal_tracker')