from datetime import datetime, timezone
from typing import Optional, TYPE_CHECKING

import sqlalchemy as sa
import sqlalchemy.orm as so
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from apps.core.extensions import db
from apps.core.mixins import Base


# to prevent circular import only import when type hinting
if TYPE_CHECKING:
    from apps.core.db import UserProfile


class User(UserMixin, Base):
    __tablename__ = "users"
    # user fields
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
