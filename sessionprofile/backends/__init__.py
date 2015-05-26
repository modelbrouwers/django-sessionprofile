from importlib import import_module

from ..settings import BACKEND


def get_backend():
    backend = import_module(BACKEND)
    return backend.SessionProfileStore
