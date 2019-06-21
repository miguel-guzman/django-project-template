import os
from settings.base import (
    BASE_DIR, INSTALLED_APPS, MIDDLEWARE, ROOT_URLCONF, TEMPLATES,
    WSGI_APPLICATION, AUTH_PASSWORD_VALIDATORS, LANGUAGE_CODE, TIME_ZONE,
    USE_I18N, USE_L10N, USE_TZ, STATIC_URL)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.setdefault('DJANGO_SETTINGS_SECRET_KEY', '@-79#*u6(541vm#&67a_08sc7v$*0e!loiiiqgng2@jj#6%h%a')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
