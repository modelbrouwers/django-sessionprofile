from django.conf import settings
from django.utils import timezone

from .base import Base
from ..models import SessionProfile


class SessionProfileStore(Base):
    """
    Backend that saves the link between session_key and user in the databse.
    """

    def save_session(self, request):
        if not hasattr(request, 'user'):
            return

        store = self.get_session_store(request)
        if store is not None and store.session_key is not None:
            sp, _ = SessionProfile.objects.get_or_create(session_key=store.session_key)
            if request.user.is_authenticated():
                if sp.user != request.user:
                    sp.user = request.user
                    sp.save()
            elif sp.user is not None:
                sp.user = None
                sp.save()

    def purge_for_user(self, user):
        SessionProfile.objects.filter(user=user).delete()

    def clear_expired(self):
        if settings.SESSION_ENGINE in [
                'django.contrib.sessions.backends.db', 'django.contrib.sessions.backends.cached_db']:
            from django.contrib.sessions.models import Session
            all_sessions = Session.objects.values_list('session_key')
            expired = all_sessions.filter(expire_date__lte=timezone.now())
            SessionProfile.objects.filter(session_key__in=expired).delete()
            SessionProfile.objects.exclude(session_key__in=all_sessions).delete()
        else:
            raise NotImplementedError('The session engine %s is not supported' % settings.SESSION_ENGINE)
