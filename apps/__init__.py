import os
from importlib import import_module

from flask import Flask
from config import get_config

from .core.extensions import init_extensions


def register_blueprints(app):
    blueprint_directories = [
        directory
        for directory in os.listdir(os.path.dirname(__file__))
        if os.path.isdir(os.path.join(os.path.dirname(__file__), directory))
        and not directory.startswith("_")
    ]

    for blueprint in blueprint_directories:
        module = import_module(f"apps.{blueprint}")
        if hasattr(module, blueprint):
            app.register_blueprint(getattr(module, blueprint))


def create_app(config_class=None):
    if not config_class:
        config_class = get_config()

    app = Flask(__name__, template_folder="templates", static_folder="statics")
    app.config.from_object(config_class)

    # initialize extensions
    init_extensions(app)

    # register blueprints
    register_blueprints(app)

    return app
