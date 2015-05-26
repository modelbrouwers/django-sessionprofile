import os


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',

    'sessionprofile',
]

ROOT_URLCONF = 'tests.urls'

DEBUG = True
STATIC_URL = '/static/'
SECRET_KEY = '&t = qu_de!+ih0gq9a+v3bjd^f@ulb7ioy_!o = gi^k12aebt7+i'

MIDDLEWARE_CLASSES = (
    'sessionprofile.middleware.SessionProfileMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'database.db'),
    }
}
