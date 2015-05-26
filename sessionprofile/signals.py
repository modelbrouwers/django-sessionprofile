from django.dispatch import receiver
from django.contrib.models import post_delete

from .models import SessionProfile


@receiver(post_delete, dispatch_uid='delete-sessionprofile')
def delete_sessionprofile(self, **kwargs):
    import bpdb; bpdb.set_trace()
    SessionProfile.objects.filter(user=1).delete()
