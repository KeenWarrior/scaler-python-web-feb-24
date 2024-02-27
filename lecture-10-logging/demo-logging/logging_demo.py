import logging

logging.basicConfig(
    filename='hello.log',
    level=logging.WARNING,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logging.warning("This is just a debug")


