import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from .api import api_blueprint
from .models.db import db


load_dotenv()

migrate = Migrate()


def create_app(testing=False):
    app = Flask('digeiz_api')

    config_path = os.getenv("TESTAPI_CONFIG_PATH", "digeiz_api.config.LocalConfig")
    app.config.from_object(config_path)

    if testing is True:
        app.config['TESTING'] = True

    db.init_app(app)
    migrate.init_app(app, db)

    CORS(app)

    app.register_blueprint(api_blueprint)

    return app
