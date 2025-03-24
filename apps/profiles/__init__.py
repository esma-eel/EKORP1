from flask import Blueprint

profiles = Blueprint(
    "profiles", __name__, template_folder="templates", static_folder="statics"
)


from apps.profiles import models
