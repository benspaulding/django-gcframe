# -*- coding: utf-8 -*-

"""Settings for running app tests when not part of another project."""

# Requred by Django, though we don't actually use the database.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

ROOT_URLCONF = 'gcframe.tests.urls'

INSTALLED_APPS = (
    'gcframe',
)

# Required for Django >= 1.4.
SECRET_KEY = 'super-secret!'
