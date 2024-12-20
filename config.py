import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    @classmethod
    def load_env_files(cls):
        env_dir = os.path.join(BASE_DIR, "envs")

        main_env = os.path.join(env_dir, ".env")
        if os.path.exists(main_env):
            load_dotenv(main_env)

        current_env = os.getenv("FLASK_ENV", "production")

        env_files = [
            ".secrets.env",  # secrets
            f".{current_env}.env",  # environment setting
            ".local.env",  # local settings
        ]

        for env_file in env_files:
            env_file_path = os.path.join(env_dir, env_file)
            if os.path.exists(env_file_path):
                load_dotenv(env_file_path, override=True)
                print(f"Loaded {env_file}")
            else:
                print(f"File not found: {env_file}")

    @classmethod
    def init_config(cls):
        cls.load_env_files()


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass

def get_config():
    BaseConfig.init_config()

    env = os.getenv("FLASK_ENV", "production")
    if env == "production":
        return ProductionConfig
    return DevelopmentConfig
