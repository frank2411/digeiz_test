import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.getcwd()}/test_api.db"


class DevelopConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.getcwd()}/test_api.db"


class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.getcwd()}/test_api.db"


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.getcwd()}/test_api_test.db"
