from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import (
    DataRequired,
    Length,
    ValidationError,
    EqualTo,
    InputRequired,
)

# from app.models import User


# class SignUpForm(FlaskForm):
#     code = StringField(
#         "Code",
#         validators=[DataRequired(), Length(min=6, message=("Your code is too short."))],
#     )
#     password = PasswordField(
#         "Password",
#         validators=[
#             DataRequired(),
#             Length(min=8, message=("Your password is too short.")),
#         ],
#     )
#     rePassword = PasswordField(
#         "reType Password",
#         validators=[
#             DataRequired(),
#             EqualTo("password", message="Passwords must match"),
#         ],
#     )
#     submit = SubmitField("Sign Up")

#     def validate_code(self, code):
#         code = User.query.filter_by(code=code.data).first()
#         if code is not None:
#             raise ValidationError(
#                 "Code has been already used! Please use a different code."
#             )


# class LoginForm(FlaskForm):
#     code = StringField("code", validators=[DataRequired()])
#     password = PasswordField("Password", validators=[DataRequired()])
#     remember_me = BooleanField("Remember me")
#     submit = SubmitField("Sign In")


class FormUpdateTranscripts(FlaskForm):
    score_C = StringField("Điểm C", validators=[DataRequired()])
    score_B = StringField("Điểm B", validators=[DataRequired()])
    score_A = StringField("Điểm A", validators=[DataRequired()])
    submit = SubmitField("Xác nhận")

    def validate_score_C(self, score_C):
        score_C = float(score_C.data)
        if score_C < 0 or score_C > 100:
            raise ValidationError("Vui lòng nhập giá trị của điểm từ 0 đến 10")

    def validate_score_B(self, score_B):
        score_B = float(score_B.data)
        if score_B < 0 or score_B > 100:
            raise ValidationError("Vui lòng nhập giá trị của điểm từ 0 đến 10")

    def validate_score_A(self, score_A):
        score_A = float(score_A.data)
        if score_A < 0 or score_A > 100:
            raise ValidationError("Vui lòng nhập giá trị của điểm từ 0 đến 10")
