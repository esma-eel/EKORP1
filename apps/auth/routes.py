from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa
from urllib.parse import urlsplit
from apps.extensions import db
from apps.auth import auth
from apps.users.models import User

from .forms import LoginForm


@auth.route("/login/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in!")
        return redirect(url_for("pages.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)
        )
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password!")
            return redirect(url_for("auth.login"))

        flash("Login requested for user {}".format(form.username.data))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        # urlsplit part is to check if there is not a url of other sites
        # next page should be relative path of our own not others
        if not next_page or urlsplit(next_page).netloc != "":
            next_page = url_for("pages.index")
        return redirect(next_page)

    return render_template("auth/login.html", title="Login", form=form)


@auth.route("/logout/")
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash("Logged you out!")
    else:
        flash("Did you even login ?")

    return redirect(url_for("pages.index"))
