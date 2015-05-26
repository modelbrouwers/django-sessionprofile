from django.conf import settings


DEFAULT_BACKEND = 'sessionprofile.backends.db'

BACKEND = getattr(settings, 'SESSIONPROFILE_BACKEND', DEFAULT_BACKEND)
