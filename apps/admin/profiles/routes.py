from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
import sqlalchemy as sa

from apps.core.extensions import db
from apps.core.db.users import User
from apps.common.utils.groups import (
    get_groups_name,
    remove_user_from_group,
    add_user_to_group,
    get_users_current_group,
    user_is_member,
)
from apps.core.db import UserProfile, GroupMembership, UserGroup

from .forms import UserProfileForm
from .. import admin


@admin.route("/profile/<username>/", methods=["GET", "POST"])
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

    current_group = get_users_current_group(profile)
    group_names = get_groups_name()

    form = UserProfileForm(obj=profile)
    form.role_group.choices = [
        (group_name, group_name.title()) for group_name in group_names
    ]
    if request.method == "GET" and current_group:
        form.role_group.data = current_group.name

    if form.validate_on_submit():
        # send data from form to model
        selected_group = form.role_group.data
        if selected_group and not user_is_member(profile, selected_group):
            if current_group:
                remove_user_from_group(profile, current_group.name)
            add_user_to_group(profile, selected_group)

        form.populate_obj(profile)
        db.session.commit()
        flash(f"{username} profile is updated")
        return redirect(url_for("admin.user_profile", username=username))

    return render_template(
        "profiles/profile_form.html",
        title=f"{profile.user.username} Profile",
        form=form,
        profile=profile,
    )
