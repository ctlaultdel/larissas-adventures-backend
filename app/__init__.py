from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)
    # enable cors
    CORS(app)
    # configure database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5433/larissas_adventures'

    db.init_app(app)
    migrate.init_app(app, db)

    # register models
    from app.models.Adventure import Adventure

    # register adventure routes
    from .routes import adventures_bp
    app.register_blueprint(adventures_bp)

    return app