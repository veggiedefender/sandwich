from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField
from wtforms.validators import InputRequired, Email
from wtforms.fields.html5 import EmailField
from app.models import User

def validate_email(email):
    return (email.endswith("@princeton.edu") or 
            email == "jessejesse123@gmail.com")

class OrderForm(FlaskForm):
    email = EmailField("email", [InputRequired(), Email()])
    recaptcha = RecaptchaField()

    def validate(self):
        return validate_email(self.email.data)