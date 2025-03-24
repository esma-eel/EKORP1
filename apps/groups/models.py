from datetime import datetime, timezone
from typing import Optional, TYPE_CHECKING

import sqlalchemy as sa
import sqlalchemy.orm as so
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from apps.extensions import db
from apps.mixins.timestamps import TimestampMixin


# to prevent circular import only import when type hinting
if TYPE_CHECKING:
    from apps.profiles.models import UserProfile


class UserGroup(TimestampMixin, db.Model):
    __tablename__ = "user_groups"
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(length=32), unique=True)
    group_memberships: so.Mapped[list["GroupMembership"]] = db.relationship(
        back_populates="group"
    )


class GroupMembership(TimestampMixin, db.Model):
    __tablename__ = "group_memberships"
    id: so.Mapped[int] = so.mapped_column(primary_key=True)

    # N:N
    profile_id: so.Mapped[int] = so.mapped_column(
        sa.ForeignKey("user_profiles.id")
    )
    group_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("user_groups.id"))

    profile: so.Mapped["UserProfile"] = db.relationship(
        back_populates="group_memberships"
    )
    group: so.Mapped["UserGroup"] = db.relationship(
        back_populates="group_memberships"
    )
