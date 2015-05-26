

class Base(object):

    def save_session(self, request):
        raise NotImplementedError

    def get_session_store(self, request):
        """
        Retrieve the session object.
        """
        if hasattr(request, 'session'):
            return request.session
        return None

    def purge_for_user(self, user):
        raise NotImplementedError

    def clear_expired(self):
        raise NotImplementedError(
            'This backend does not support clearing expired sessions')
