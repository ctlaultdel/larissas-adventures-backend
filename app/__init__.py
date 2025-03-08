from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)
    # enable cors
    CORS(app)
    
    # configure database
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    db.init_app(app)
    migrate.init_app(app, db)

    # register models
    from app.models.Adventure import Adventure
    from app.models.Blog import Blog
    from app.models.Content import Content

    # register adventure routes
    from .routes import adventures_bp, blog_bp
    app.register_blueprint(adventures_bp)
    app.register_blueprint(blog_bp)

    return app