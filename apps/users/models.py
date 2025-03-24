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


class User(TimestampMixin, UserMixin, db.Model):
    __tablename__ = "users"
    # user fields
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(
        sa.String(64), index=True, unique=True
    )
    email: so.Mapped[str] = so.mapped_column(
        sa.String(120), index=True, unique=True
    )
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    # foreign keys
    # 1:1
    profile: so.Mapped["UserProfile"] = db.relationship(
        back_populates="user", uselist=False
    )

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
