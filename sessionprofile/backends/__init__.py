from importlib import import_module

from ..settings import BACKEND
from .db import DatabaseBackend


def get_backend():
    backend = import_module(BACKEND)
    return backend
