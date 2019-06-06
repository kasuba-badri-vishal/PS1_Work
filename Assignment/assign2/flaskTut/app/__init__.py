from flask import Flask
from config import Config
# app.config['SECRET_KEY'] = '1973'
# # ... add more variables here as needed
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models