from models.todo import Todo
from repositories import todo_repository


def get_todos():
    todo_repository.find()


def get_todo(id) -> Todo:
    return todo_repository.find_by_id(id)


def create_todo(title: str, completed: bool):
    todo = Todo(title, completed)
    saved = todo_repository.save(todo)
    return saved, 201


def update_todo(id, updates):
    todo = todo_repository.find_by_id(id)
    if not todo:
        raise Exception("No todo with id " + id)

    todo.title = updates.title
    todo.completed = updates.completed

    updated = todo_repository.save(todo)

    return updated


def delete_todo(id):
    pass