# Django Project Template

## Settings folder

Settings for different environments have been isolated in different files, which inherit from 'base.py', another file that contains shared settings.

Manage.py will import development.py by default, but this behavior can be customized by specifying which module to import through the 'DJANGO_SETTINGS_MODULE' environment variable.

## Example Project Structure

* apps
  * inventory
    * \_\_init\_\_.py
    * admin.py
    * apps.py
    * models.py
    * test.py
    * views.py
  * customers
  * billing
* project
  * \_\_init\_\_.py
  * urls.py
  * wsgi.py
* settings
  * \_\_init\_\_.py
  * base.py
  * development.py
  * staging.py
  * production.py
* templates
  * base.html
  * ...
* static
  * css
  * js
  * ...
* media
