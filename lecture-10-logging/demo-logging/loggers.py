import logging
from logging import FileHandler, StreamHandler

file_handler = FileHandler(
    filename="another.log",
)

console_handler = StreamHandler()

logging.basicConfig(
    handlers=[
        console_handler,
        file_handler
    ],
    level=logging.DEBUG
)

logging.debug("This will also go to the file")

