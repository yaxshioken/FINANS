import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

load_dotenv()

app = Flask(__name__)

class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost:5432/{os.getenv('POSTGRES_DB')}"
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
