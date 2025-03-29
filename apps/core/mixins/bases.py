import sqlalchemy as sa
import sqlalchemy.orm as so
from apps.core.extensions import db
from .timestamps import TimestampMixin


# we use this when we do not have flask sqlalchemy
# from datetime import datetime, timezone
# class Base(TimestampMixin, so.DeclarativeBase):
#     pass


class BaseFieldMixin(TimestampMixin):
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)


class Base(BaseFieldMixin, db.Model):
    __abstract__ = True
