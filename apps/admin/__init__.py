from flask import Blueprint

admin = Blueprint(
    "admin",
    __name__,
    template_folder="templates",
    static_folder="statics",
    url_prefix="/admin",
)

from .profiles import routes as profile_routes
