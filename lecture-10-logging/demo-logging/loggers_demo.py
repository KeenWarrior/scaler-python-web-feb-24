import logging
from logging import Logger, FileHandler, StreamHandler

logger1 = Logger(
    name="first"
)

logger2 = Logger(
    name="second"
)

file_handler = FileHandler(
    filename="another.log",
)

console_handler = StreamHandler()

logger1.addHandler(file_handler)
logger1.addHandler(console_handler)
logger1.setLevel(level=logging.DEBUG)

logger2.addHandler(file_handler)
logger2.setLevel(level=logging.WARNING)


logger1.warning("Message from logger 1")
logger2.warning("Message from logger 2")