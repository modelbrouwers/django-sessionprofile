from .base import Base
from ..models import SessionProfile


class SessionProfileStore(Base):
    """
    Backend that saves the link between session_key and user in the databse.
    """

    def save_session(self, request):
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
