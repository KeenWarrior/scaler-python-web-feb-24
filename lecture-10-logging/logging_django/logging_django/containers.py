from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton, Configuration

import logging


class Container(DeclarativeContainer):

    config = Configuration()

    logger = Singleton(
        logging.getLogger,
        "basic"
    )
