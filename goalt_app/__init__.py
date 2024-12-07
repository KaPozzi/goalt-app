from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://master:Sucesso_24@localhost/goal_tracker'
    app.secret_key = 'b20a61da639d856a1ba0079df2b26c87'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # with app.app_context():
    #     from . import routes, models
    #     db.create_all()

    #     return app
    with app.app_context():


        from .routes import routes
        
        app.register_blueprint(routes, url_prefix='/')

        return app