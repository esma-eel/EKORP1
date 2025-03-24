from flask import Blueprint

groups = Blueprint(
    "groups", __name__, template_folder="templates", static_folder="statics"
)

from apps.groups import models