from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField
from wtforms.validators import InputRequired, Email
from wtforms.fields.html5 import EmailField
from app.models import User

class OrderForm(FlaskForm):
    email = EmailField("email", [InputRequired(), Email()])
    recaptcha = RecaptchaField()

    def validate(self):
        return (self.email.data.endswith("@princeton.edu")
                or self.email.data == "jessejesse123@gmail.com")