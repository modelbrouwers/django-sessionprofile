from typing import Optional

from django.contrib.sessions.backends.base import SessionBase
from django.http import HttpRequest


class Base:
    def save_session(self, request: HttpRequest) -> None:
        raise NotImplementedError

    def get_session_store(self, request: HttpRequest) -> Optional[SessionBase]:
        """
        Retrieve the session object.
        """
        if hasattr(request, "session"):
            return request.session
        return None

    def purge_for_user(self, user) -> None:
        raise NotImplementedError

    def clear_expired(self) -> None:
        raise NotImplementedError(
            "This backend does not support clearing expired sessions"
        )
