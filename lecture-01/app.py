from flask import Flask, request

from controllers.todo_controller import todos_blueprint

app = Flask(__name__)

print(__name__)

app.register_blueprint(todos_blueprint, url_prefix="/todos")

