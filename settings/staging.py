import os
from settings.base import (
    AUTH_PASSWORD_VALIDATORS, BASE_DIR, INSTALLED_APPS, LANGUAGE_CODE, MIDDLEWARE, ROOT_URLCONF,
    STATIC_URL, TEMPLATES, TIME_ZONE, USE_I18N, USE_L10N, USE_TZ, WSGI_APPLICATION)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.setdefault('DJANGO_SETTINGS_SECRET_KEY', '(redacted)')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
