import sys

from django.core.management import call_command
from django.test import SimpleTestCase

try:  # Py 2.x
    from StringIO import StringIO
except ImportError:  # Py 3.x
    from io import StringIO

try:
    from django.test import override_settings
except ImportError:
    from django.test.utils import override_settings


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
