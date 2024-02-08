from flask.blueprints import Blueprint
from flask import request
from sqlalchemy.exc import NoResultFound

from models.user_model import User
from engine import engine
from sqlalchemy.orm import Session
from sqlalchemy import select

users_blueprint = Blueprint("users_blueprint", __name__)


@users_blueprint.post("/")
def create_user():
    body = request.json
    with Session(engine) as session:
        user = User(name=body["name"], email=body["email"])
        session.add(user)
        session.commit()
        return user.to_dict()


@users_blueprint.get("/")
def get_users():
    with Session(engine) as session:
        stm = select(User)
        rows = session.execute(stm).all()
        return [user.to_dict() for user, in rows]


@users_blueprint.get("/<int:id>")
def get_user(id):
    try:
        with Session(engine) as session:
            stm = select(User).where( User.id==id )
            user, = session.execute(stm).one()
            return user.to_dict()
    except NoResultFound:
        return {
            "message": "No user with id: {}".format(id)
        }, 404




