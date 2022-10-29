from io import StringIO

from django.core.management import call_command


def test_cleanup_inactive(settings):
    settings.SESSIONPROFILE_BACKEND = "tests.mock"

    call_command("sp_clear_expired")


def test_unsupported_backend(settings):
    settings.SESSION_ENGINE = "django.contrib.sessions.backends.cache"
    settings.SESSIONPROFILE_BACKEND = "sessionprofile.backends.db"
    stderr = StringIO()

    call_command("sp_clear_expired", stderr=stderr)

    output = stderr.getvalue()
    assert output == (
        "The session engine django.contrib.sessions.backends.cache is "
        "not supported\n"
    )
