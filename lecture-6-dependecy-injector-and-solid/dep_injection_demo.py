from dependency_injector.containers import DeclarativeContainer
from dependency_injector import providers
from dependency_injector.wiring import inject, Provide


class UserRepo:
    pass


class SessionRepo:
    pass


class UserServie:
    user_repo: UserRepo
    session_repo: SessionRepo

    @inject
    def __init__(
            self,
            user_repo: UserRepo = Provide("user_repo"),
            session_repo: SessionRepo = Provide("session_repo")
    ):
        self.user_repo = user_repo
        self.session_repo = session_repo


class UserController:
    user_service: UserServie

    @inject
    def __init__(
            self,
            user_service: UserServie = Provide("user_service")
    ):
        self.user_service = user_service


class Container(DeclarativeContainer):
    user_repo = providers.Factory(
        UserRepo
    )

    session_repo = providers.Factory(
        SessionRepo
    )

    user_service = providers.Factory(
        UserServie,
        user_repo=user_repo,
        session_repo=session_repo
    )

    user_controller = providers.Factory(
        UserController,
        user_service=user_service
    )


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[
        __name__
    ])

    controller1 = container.user_controller()
    controller2 = container.user_controller()
    controller3 = container.user_controller()
    controller4 = container.user_controller()
    controller5 = container.user_controller()
    controller6 = container.user_controller()
    print(type(controller))

