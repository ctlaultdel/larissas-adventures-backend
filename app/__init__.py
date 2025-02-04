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
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://u2i2rismuiuj8b:p7ded7056f8a5b619d314093ed009d1202146c174a7e74171eba49ba53d238c3f@c67okggoj39697.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d31ken5f8jmkr5"

    db.init_app(app)
    migrate.init_app(app, db)

    # register models
    from app.models.Adventure import Adventure

    # register adventure routes
    from .routes import adventures_bp
    app.register_blueprint(adventures_bp)

    return app