from django.conf import settings
from django.http import HttpRequest
from django.utils import timezone

from ..models import SessionProfile
from .base import Base


class SessionProfileStore(Base):
    """
    Backend that saves the link between session_key and user in the databse.
    """

    def save_session(self, request: HttpRequest) -> None:
        if not hasattr(request, "user"):
            return

        store = self.get_session_store(request)
        if store is not None and store.session_key is not None:
            sp, _ = SessionProfile.objects.get_or_create(session_key=store.session_key)
            user = request.user if request.user.is_authenticated else None
            if sp.user != user:
                sp.user = user
                sp.save()

    def purge_for_user(self, user) -> None:
        SessionProfile.objects.filter(user=user).delete()

    def clear_expired(self):
        if settings.SESSION_ENGINE in [
            "django.contrib.sessions.backends.db",
            "django.contrib.sessions.backends.cached_db",
        ]:
            from django.contrib.sessions.models import Session

            all_sessions = Session.objects.values_list("session_key")
            expired = all_sessions.filter(expire_date__lte=timezone.now())
            SessionProfile.objects.filter(session_key__in=expired).delete()
            SessionProfile.objects.exclude(session_key__in=all_sessions).delete()
        else:
            raise NotImplementedError(
                f"The session engine {settings.SESSION_ENGINE} is not supported"
            )
