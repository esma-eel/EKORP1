from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from urllib.parse import urlsplit
from apps.extensions import db
from apps.auth import auth
from apps.users.models import User
from apps.utils.email import send_password_reset_email
from apps.utils.tokens import verify_reset_password_token

from .forms import (
    LoginForm,
    ResetPasswordRequestForm,
    ResetPasswordForm,
    ChangePasswordForm,
)


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


@auth.route("/reset_password_request/", methods=["GET", "POST"])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for("pages.index"))

    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.email == form.email.data)
        )
        if user:
            send_password_reset_email(user)
        flash("Check your email for instructions to reset your password!")
        return redirect(url_for("auth.login"))
    return render_template(
        "auth/reset_password_request.html", title="Reset Password", form=form
    )


@auth.route("/reset_password/<token>/", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for("pages.index"))

    user = verify_reset_password_token(token)
    if not user:
        return redirect(url_for("pages.index"))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash("Your password has been reset!")
        return redirect(url_for("auth.login"))
    return render_template(
        "auth/reset_password.html",
        title="Reset Password",
        form=form,
    )


@auth.route("/change_password/", methods=["GET", "POST"])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if form.password.data == form.current_password.data:
            form.password.errors.append(
                "Your new password and current password are the same! change it plz"
            )
        elif current_user.check_password(form.current_password.data):
            current_user.set_password(form.password.data)
            db.session.commit()
            flash("Your password has been changed!")
            logout_user()
            return redirect(url_for("auth.login"))
        else:
            form.current_password.errors.append(
                "Check your current password again!"
            )

    return render_template(
        "auth/change_password.html", title="Change Password", form=form
    )
