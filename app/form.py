from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import (
    DataRequired,
    Length,
    ValidationError,
    EqualTo,
    InputRequired,
)

from app.models import User


class SignUpForm(FlaskForm):
    code = StringField(
        "Code",
        validators=[DataRequired(), Length(min=6, message=("Your code is too short."))],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8, message=("Your password is too short.")),
        ],
    )
    rePassword = PasswordField(
        "reType Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match"),
        ],
    )
    submit = SubmitField("Sign Up")

    def validate_code(self, code):
        code = User.query.filter_by(code=code.data).first()
        if code is not None:
            raise ValidationError(
                "Code has been already used! Please use a different code."
            )


class LoginForm(FlaskForm):
    code = StringField("code", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Sign In")
