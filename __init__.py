import os
from flask_caching import Cache
from datetime import timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv



load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SESSION_TYPE"] = os.getenv("SESSION_TYPE")
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=5)

cache = Cache(app, config={"CACHE_TYPE": "SimpleCache"})
db = SQLAlchemy(app)

from . import routes