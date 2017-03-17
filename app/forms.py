from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField
from app.models import User

def validate_email(email):
    return (email.endswith("@princeton.edu") or
            email.endswith(".princeton.edu") or
            email == "jessejesse123@gmail.com")

class OrderForm(FlaskForm):
    email = EmailField("email", [DataRequired(), Email()])
    recaptcha = RecaptchaField()

class AdminForm(FlaskForm):
    recaptcha = RecaptchaField()
    email = EmailField("email", [DataRequired(), Email()])
    def validate(self):
        if not super().validate():
            return False
        return validate_email(self.email.data)