from django.conf import settings


def _get_backend():
    return getattr(settings, "SESSIONPROFILE_BACKEND", "sessionprofile.backends.db")
