from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import config

## instantiate the app object
app = Flask(__name__)
cf = config.DevelopmentConfig()
app.config.from_object(cf)

db = SQLAlchemy(app)
from src import views
from src.models import user_ingredients
