from flask import Blueprint

users = Blueprint(
    "users", __name__, template_folder="templates", static_folder="statics"
)

from apps.users import models
