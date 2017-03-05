import os
from config import basedir

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)

mail = Mail(app)

csrf_protect = CSRFProtect(app)

from app import views, api
