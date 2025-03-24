import os
from datetime import timedelta
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
env_path = os.path.join(BASE_DIR, "envs", ".env")
load_dotenv(env_path)


class BaseConfig:
    # FLASK - Used in WTF too
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")

    # SQL ALCHEMY
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "ekorp1_default.db"),
    )
    # this variable is for tracking changes of CRUD on objects
    # it has overhead on system so many people recommed to turn it off
    # and i do it too
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": 10,
        "pool_recycle": 3600,
        "pool_pre_ping": True,
    }

    # Login
    # this options are for remember me part in login page
    # this is for flask-login
    REMEMBER_COOKIE_DURATION = timedelta(days=7)
    # this is in case above options was buggy and did not work
    # this is for flask itself
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    # flask mail
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = int(os.getenv("MAIL_PORT") or 25)
    MAIL_USE_TLS = int(os.getenv("MAIL_USE_TLS") or 0)
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    ADMINS = ["test@ekorp1.ig"]


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


def get_config():
    """Get config based on FLASK_ENV environment variable"""
    env = os.getenv("FLASK_ENV", "production").lower()
    config_class = (
        ProductionConfig if env == "production" else DevelopmentConfig
    )
    return config_class
