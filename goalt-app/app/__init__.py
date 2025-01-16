from flask import Flask
from database import engine, Base
from routes import register_routes

def create_app():
    app = Flask(__name__)

    # Register application routes
    register_routes(app)

    # Initialize the database
    with app.app_context():
        Base.metadata.create_all(bind=engine)

    return app
