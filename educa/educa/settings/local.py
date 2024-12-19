from .base import *

# python.exe .\manage.py runserver --settings=educa.settings.local

DEBUG = True

ALLOWED_HOSTS = ['.educaproject.com', 
                 '127.0.0.1', '172.27.22.112']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}