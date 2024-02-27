from d_injector_demo.models import User
from abc import ABC


class UserService(ABC):

    def create_user(self, name, email):
        pass


class UserServiceImpl(UserService):

    def create_user(self, name, email):
        user = User(name=name, email=email)
        user.save()
        return user



