import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
env_path = os.path.join(BASE_DIR, "envs", ".env")
load_dotenv(env_path)


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
    # DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")


class DevelopmentConfig(BaseConfig):
    pass
    # DATABASE_URL = os.getenv("DEV_DATABASE_URL", "sqlite:///dev.db")


class ProductionConfig(BaseConfig):
    pass
    # DATABASE_URL = os.getenv("PROD_DATABASE_URL", "postgresql://user:pass@localhost/prod_db")


def get_config():
    """Get config based on FLASK_ENV environment variable"""
    env = os.getenv("FLASK_ENV", "production").lower()
    config_class = (
        ProductionConfig if env == "production" else DevelopmentConfig
    )
    return config_class
