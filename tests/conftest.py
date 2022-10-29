import pytest


@pytest.fixture
def sp_settings(settings):
    settings.SESSIONPROFILE_BACKEND = "sessionprofile.backends.db"
    settings.SESSION_SAVE_EVERY_REQUEST = True
    return settings
