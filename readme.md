# Django Project Template

## Settings folder

Settings for different environments have been isolated in different files, which inherit from 'base.py', another file that contains shared settings.

Manage.py will import development.py by default, but this behavior can be customized by specifying which module to import through the 'DJANGO_SETTINGS_MODULE' environment variable.
