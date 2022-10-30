from django.core.management.base import BaseCommand

from ...backends import get_backend


class Command(BaseCommand):
    help = "Purge expired sessions"

    def handle(self, **options):
        store = get_backend()()
        try:
            store.clear_expired()
        except NotImplementedError as e:
            self.stderr.write(e.args[0])
