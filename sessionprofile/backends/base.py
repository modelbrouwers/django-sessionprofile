from importlib import import_module

from django.conf import settings


class Base(object):

    def __init__(self):
        engine = import_module(settings.SESSION_ENGINE)
        self.SessionStore = engine.SessionStore

    def get_session(self, request):
        """
        Retrieve the session object.
        """
        session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME, None)
        return self.SessionStore(session_key)

    def set_user(self):
        raise NotImplementedError
