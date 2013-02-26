# -*- coding: utf-8 -*-

""" Simple urls for use in testing the gcframe app. """

from __future__ import unicode_literals

# The defaults module is deprecated in Django 1.5, but necessary to
# support Django 1.3. drop ``.defaults`` when dropping 1.3 support.
from django.conf.urls.defaults import patterns, url

from .views import normal, framed, exempt


urlpatterns = patterns('',
    url(r'normal/$', normal, name='gcframe-test-normal'),
    url(r'framed/$', framed, name='gcframe-test-framed'),
    url(r'exempt/$', exempt, name='gcframe-test-exempt'),
)
