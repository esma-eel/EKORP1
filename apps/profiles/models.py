from typing import Optional, TYPE_CHECKING

import sqlalchemy as sa
import sqlalchemy.orm as so

from apps.extensions import db
from apps.mixins.timestamps import TimestampMixin


# to prevent circular import only import when type hinting
if TYPE_CHECKING:
    from users.models import User


class UserProfile(TimestampMixin, db.Model):
    __tablename__ = "user_profiles"
    # user profile fields
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    name: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    address: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    phone_number: so.Mapped[Optional[str]] = so.mapped_column(sa.String(11))
    # from views or forms we send m as male or f as female in this
    gender: so.Mapped[Optional[str]] = so.mapped_column(sa.String(1))
    birth_date: so.Mapped[Optional[sa.Date]] = so.mapped_column(sa.Date)

    # foreign keys
    # users is name of User model table
    # 1:1
    user_id: so.Mapped[int] = so.mapped_column(
        sa.ForeignKey("users.id"), unique=True
    )
    user: so.Mapped["User"] = db.relationship(back_populates="profile")
