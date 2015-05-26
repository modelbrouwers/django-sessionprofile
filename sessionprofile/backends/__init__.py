from importlib import import_module

from ..settings import _get_backend


def get_backend():
    backend = import_module(_get_backend())
    return backend.SessionProfileStore
