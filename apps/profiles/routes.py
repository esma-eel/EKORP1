from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from urllib.parse import urlsplit
from apps.extensions import db
from apps.profiles import profiles
from apps.users.models import User
from .models import UserProfile
from .forms import UserProfileForm


@profiles.route("/profile/<username>/", methods=["GET", "POST"])
@login_required
def user_profile(username):
    user = db.session.scalar(sa.select(User).where(User.username == username))
    if not user:
        flash("User not found!")
        return redirect(url_for("pages.index"))

    profile = user.profile
    if profile is None:
        profile = UserProfile(user=current_user)
        db.session.add(profile)
        db.session.commit()

    form = UserProfileForm(obj=profile)
    if form.validate_on_submit():
        # send data from form to model
        form.populate_obj(profile)
        db.session.commit()
        flash(f"{username} profile is updated")
        return redirect(url_for("profiles.user_profile", username=username))

    return render_template(
        "profiles/profile_form.html",
        title=f"{profile.user.username} Profile",
        form=form,
        profile=profile,
    )
