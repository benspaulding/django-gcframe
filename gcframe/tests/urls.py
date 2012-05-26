""" Simple urls for use in testing the gcframe app. """

from django.conf.urls.defaults import *

from gcframe.tests.views import normal, framed, exempt

urlpatterns = patterns('',
    url(r'normal/$', normal, name='gcframe-test-normal'),
    url(r'framed/$', framed, name='gcframe-test-framed'),
    url(r'exempt/$', exempt, name='gcframe-test-exempt'),
)
