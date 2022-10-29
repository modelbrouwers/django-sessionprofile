from django.apps import AppConfig


class SessionProfileConfig(AppConfig):
    name = "sessionprofile"

    def ready(self):
        from . import signals  # noqa
