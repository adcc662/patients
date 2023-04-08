from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'patients',
        'USER': 'user',
        'PASSWORD': 'user123',
        'HOST': 'db',
        'PORT': 5432,
    }
}

STATIC_URL = 'static/'
DEBUG = True

ALLOWED_HOSTS = []