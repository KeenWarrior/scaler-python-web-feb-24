from django.apps import AppConfig
from logging_django import container


class LoggingApp(AppConfig):
    name = "logging_django"

    def ready(self):
        container.wire(packages=[
            "logging_django.views"
        ])
