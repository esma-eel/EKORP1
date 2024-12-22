from flask import Blueprint

auth = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    static_folder="statics",
    url_prefix="/auth",
)

from apps.auth import routes
