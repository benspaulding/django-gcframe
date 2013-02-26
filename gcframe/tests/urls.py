# -*- coding: utf-8 -*-

""" Simple urls for use in testing the gcframe app. """

from __future__ import unicode_literals

from django.conf.urls.defaults import *

from .views import normal, framed, exempt


urlpatterns = patterns('',
    url(r'normal/$', normal, name='gcframe-test-normal'),
    url(r'framed/$', framed, name='gcframe-test-framed'),
    url(r'exempt/$', exempt, name='gcframe-test-exempt'),
)
