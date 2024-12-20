from flask import Blueprint

pages = Blueprint("pages", __name__, template_folder="templates", static_folder="statics")

from apps.pages import routes