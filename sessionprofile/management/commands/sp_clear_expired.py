from django.core.management.base import NoArgsCommand

from sessionprofile.backends import get_backend


class Command(NoArgsCommand):
    help = "Purge expired sessions"

    def handle_noargs(self, **options):
        store = get_backend()()
        try:
            store.clear_expired()
        except NotImplementedError as e:
            self.stderr.write(e.args[0])
