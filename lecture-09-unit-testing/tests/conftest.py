import pytest
from models import User


@pytest.fixture
def first_user():
    return User(
        name="First User",
        age=20
    )


@pytest.fixture
def second_user():
    return User(
        name="Second User",
        age=20
    )
