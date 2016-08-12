from sessionprofile.backends import get_backend

from .compat import MiddlewareMixin


class SessionProfileMiddleware(MiddlewareMixin):

    def __init__(self, get_response=None):
        super(SessionProfileMiddleware, self).__init__(get_response=get_response)
        self.store = get_backend()()

    def process_response(self, request, response):
        if hasattr(request, 'session'):
            self.store.save_session(request)
        return response
