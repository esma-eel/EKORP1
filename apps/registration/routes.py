from flask import redirect, flash, url_for, render_template
from flask_login import current_user
from apps.extensions import db
from apps.users.models import User
from apps.registration import registration
from apps.registration.forms import RegistrationForm


@registration.route("/signup/", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("You are already registered!")
        return redirect(url_for("pages.index"))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f"User {form.username.data} signup completed!")
        return redirect(url_for("auth.login"))

    return render_template(
        "registration/register.html", title="Registration", form=form
    )
