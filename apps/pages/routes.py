from flask import render_template, flash
from flask_login import login_required, current_user

from . import pages


@pages.route("/index/")
@pages.route("/")
def index():
    return render_template("pages/index.html", title="Test title")


@pages.route("/test-login-required/")
@login_required
def test_login_required():
    flash(f"Hi user {current_user}")
    return render_template(
        "pages/test-login-required.html", title="login required"
    )
