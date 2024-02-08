from models.todo import Todo

todos = []


def find():
    pass


def save(todo: Todo):

    for idx, current in enumerate(todos):
        if current.id == todo.id:
            todos[idx] = todo

    todos.append(todo)


def find_by_id(id):
    pass

