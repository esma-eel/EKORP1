from flask_wtf import FlaskForm
import sqlalchemy as sa
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from apps.core.extensions import db
from apps.core.db import User


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password_confirmation = PasswordField(
        "Password COnfirmation",
        validators=[DataRequired(), EqualTo("password")],
    )
    submit = SubmitField("Register")

    def validate_username(self, username_field):
        # i used username_field instead of username to remember this is not
        # an string value
        user = db.session.scalar(
            sa.select(User).where(User.username == username_field.data)
        )

        if user is not None:
            raise ValidationError(
                "The username did not match the rules, enter another username"
            )

    def validate_email(self, email_field):
        user = db.session.scalar(
            sa.select(User).where(User.email == email_field.data)
        )
        if user is not None:
            raise ValidationError(
                "The email did not validated, enter another email"
            )
