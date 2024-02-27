from django.apps import AppConfig

from d_injector_demo import containers


class Config(AppConfig):
    name = "d_injector_demo"

    def ready(self):
        container = containers.Container()
        container.wire(
            packages=[
                "d_injector_demo.controllers"
            ]
        )
