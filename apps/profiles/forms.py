from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp, Optional


class UserProfileForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=64)])
    phone_number = StringField(
        "Phone Number",
        validators=[
            DataRequired(),
            Length(max=11),
            Regexp(r"^\d{11}$", message="phone number must be 11 digits"),
        ],
    )
    gender = SelectField("Gender", choices=(("m", "Male"), ("f", "Female")))
    birth_date = DateField(
        "Birth Date", validators=[DataRequired()], format="%Y-%m-%d"
    )
    address = TextAreaField("Address", validators=[Optional(), Length(max=256)])
    submit = SubmitField("Save")
