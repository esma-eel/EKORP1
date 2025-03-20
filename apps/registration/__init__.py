from flask import Blueprint

registration = Blueprint(
    "registration",
    __name__,
    template_folder="templates",
    static_folder="statics",
    url_prefix="/registration",
)

from apps.registration import routes
