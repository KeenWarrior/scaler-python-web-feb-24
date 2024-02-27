from dependency_injector.containers import DeclarativeContainer
from dependency_injector import providers
from d_injector_demo.services import UserServiceImpl


class Container(DeclarativeContainer):

    user_service = providers.Singleton(
        UserServiceImpl
    )
