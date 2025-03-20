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
        "sqlite:///" + os.path.join(BASE_DIR, "boilerplate_default.db"),
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": 10,
        "pool_recycle": 3600,
        "pool_pre_ping": True,
    }

    # Login
    REMEMBER_COOKIE_DURATION = timedelta(days=7)


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
