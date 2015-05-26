from django.core.management import call_command
from django.test import SimpleTestCase, override_settings


class CommandTests(SimpleTestCase):

    @override_settings(SESSIONPROFILE_BACKEND='tests.tests.mock')
    def test_cleanup_inactive(self):
        call_command('sp_clear_expired')
