from sessionprofile.backends import get_backend

engine = get_backend()()


class SessionProfileMiddleware(object):

    def process_response(self, request, response):
        if hasattr(request, 'session'):
            engine.save_session(request)
        return response
