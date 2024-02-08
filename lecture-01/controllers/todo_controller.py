from flask import Blueprint
from flask import request
from typing import Dict
from services import todo_service

todos_blueprint = Blueprint("todos_blueprint", __name__)


@todos_blueprint.get("/")
def get_todos():
    return [todo.to_dict() for todo in todo_service.get_todos()]


@todos_blueprint.get("/<id>")
def get_todo(id):

    try:
        todo = todo_service.get_todo(id)
        return todo.to_dict()
    except Exception:
        return {"message": "Todo not found with id " + id}, 404


@todos_blueprint.post("/")
def create_todo():
    data: Dict = request.json
    todo = todo_service.create_todo(data["title"], data["completed"])
    return todo.to_dict(), 201

def update_todo(id, updates):
    pass


def delete_todo(id):
    pass