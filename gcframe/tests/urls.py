""" Simple urls for use in testing the gcframe app. """

from django.conf.urls.defaults import *

from gcframe.tests.views import normal, framed, exempt

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^tests/', include('tests.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    url(r'normal/$', normal, name='gcframe-test-normal'),
    url(r'framed/$', framed, name='gcframe-test-framed'),
    url(r'exempt/$', exempt, name='gcframe-test-exempt'),
)
