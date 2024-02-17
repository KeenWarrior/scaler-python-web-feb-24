import dataclasses
from enum import Enum
from typing import Dict

from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.containers import WiringConfiguration
from dependency_injector.wiring import inject, Provide

from faker import Faker

fake = Faker()


class Role(Enum):
    USER = 1
    ADMIN = 2


@dataclasses.dataclass
class User:
    role: Role = dataclasses.field(default=Role.USER)
    name: str = dataclasses.field(default_factory=fake.name)
    street: str = dataclasses.field(default_factory=fake.street_address)


class Container(DeclarativeContainer):

    user = providers.Singleton(
        User
    )

    users = providers.List(
        user,
        user,
        user,
        user
    )

    audience = providers.Dict(
        admin=providers.Object(
            User(
                name="Anuj Garg",
                street="Hoodi Circle",
                role=Role.ADMIN
            )
        ),
        users=users
    )


@inject
def hello(audience: Dict = Provide("audience")):
    # admin = audience["admin"]
    # users = audience["users"]
    print(audience)


if __name__ == "__main__":
    container = Container()
    container.wire(
        modules=["__main__"],
        packages=[]
    )
    hello()

