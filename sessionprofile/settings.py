from django.conf import settings


DEFAULT_BACKEND = 'sessionprofile.backends.DatabaseBackend'

BACKEND = getattr(settings, 'SESSIONPROFILE_BACKEND', DEFAULT_BACKEND)
