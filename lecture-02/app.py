from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from engine import engine
from models.base import Base
from flask import Flask
from controllers.user_controller import users_blueprint

# postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase"
#  driver+dialect://username:password@host:port/database

# sqlite:///db.sqlite

Base.metadata.create_all(engine)

app = Flask(__name__)

app.register_blueprint(users_blueprint, url_prefix="/users")




