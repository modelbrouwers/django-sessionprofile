from sessionprofile.backends import get_backend


class SessionProfileMiddleware(object):

    def __init__(self):
        self.store = get_backend()()

    def process_response(self, request, response):
        if hasattr(request, 'session'):
            self.store.save_session(request)
        return response
