from django import VERSION

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:  # Django < 1.10

    class MiddlewareMixin(object):
        def __init__(self, get_response=None):
            pass


def is_authenticated(user):
    if VERSION < (1, 10):
        return user.is_authenticated()
    return user.is_authenticated
