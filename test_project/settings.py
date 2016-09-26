import os

import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('SECRET_KEY', 'replace_me_please')

DEBUG = bool(os.environ.get('DEBUG', False))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

INSTALLED_APPS = (
    'test_project',

    'countries',
)

WSGI_APPLICATION = 'test_project.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost/countries')
}
