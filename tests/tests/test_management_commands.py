import sys
from StringIO import StringIO

from django.core.management import call_command
from django.test import SimpleTestCase, override_settings


class CommandTests(SimpleTestCase):

    @override_settings(SESSIONPROFILE_BACKEND='tests.tests.mock')
    def test_cleanup_inactive(self):
        call_command('sp_clear_expired')

    @override_settings(
        SESSION_ENGINE='django.contrib.sessions.backends.cache',
        SESSIONPROFILE_BACKEND='sessionprofile.backends.db'
    )
    def test_unsupported_backend(self):
        old_stderr = sys.stderr
        sys.stderr = StringIO()
        call_command('sp_clear_expired')
        sys.stderr.seek(0)
        output = sys.stderr.read()
        self.assertEqual(output, 'The session engine django.contrib.sessions.backends.cache is not supported\n')
        sys.stderr = old_stderr
