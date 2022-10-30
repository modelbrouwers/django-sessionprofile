from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .backends import get_backend


@receiver(post_save, dispatch_uid="delete-sessionprofile")
def purge_sessionprofile(sender, **kwargs):
    if sender is not get_user_model() or kwargs.get("raw"):
        return

    user = kwargs["instance"]
    if user.is_active:
        return

    store = get_backend()()
    store.purge_for_user(user)
