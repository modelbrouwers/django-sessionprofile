from django.core.management.base import NoArgsCommand

from sessionprofile.backends import get_backend


class Command(NoArgsCommand):
    help = "Purge expired sessions"

    def handle_noargs(self, **options):
        store = get_backend()()
        store.clear_expired()
