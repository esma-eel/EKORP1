from flask import render_template
from apps.pages import pages

@pages.route("/")
@pages.route("/index/")
def index():
    return render_template("pages/index.html", title="Test title")
