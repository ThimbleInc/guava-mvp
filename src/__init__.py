from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
from src import views
from src.models import user_ingredients
