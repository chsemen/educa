from decouple import config
from .base import *

DEBUG = False

ADMINS = [
    ('Semen Chefranov', 'ch-semen@rambler.ru'),
]

ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com', 
                 '127.0.0.1', '172.27.22.112']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}

REDIS_URL = 'redis://cache:6379'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]

CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True
SECURE_SSL_REDIRECT=True

# C:\bin\Git\mingw64\bin\openssl.exe req -x509 -newkey rsa:2048 -sha256 -days 3650 -nodes -keyout ssl/educa.key -out ssl/educa.crt -subj '/CN=*.educaproject.com' -addext 'subjectAltName=DNS:*.educaproject.com'