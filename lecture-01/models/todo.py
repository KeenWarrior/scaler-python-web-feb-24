from uuid import uuid4


class Todo:

    def __init__(self, title, completed):
        self.id = None
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }
