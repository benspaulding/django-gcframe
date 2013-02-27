# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse

# Must use absolute import here so Django 1.3 does not choke.
from gcframe.decorators import gcframe, gcframe_exempt
from .middleware import GCFrameTestCase


class DecoratorTestCase(GCFrameTestCase):

    def test_gcframe(self):
        response = self.client.get(reverse('gcframe-test-framed'))
        self.assertTrue(response.has_header('X-UA-Compatible'))
        # TODO: Test that decorator overrides middleware.

    def test_exempt(self):
        response = self.client.get(reverse('gcframe-test-exempt'))
        self.assertTrue(hasattr(response, 'gcframe_exempt'))
        self.assertTrue(getattr(response, 'gcframe_exempt', False))
        # This test may be repetitive. (This assertion alread appears in
        # middleware tests.)
        self.assertFalse(response.has_header('X-UA-Compatible'))


class DecoratorSansGCFrameTestCase(DecoratorTestCase):
    """Case to test that decorators perform correctly without middleware."""

    def setUp(self):
        """ Remove the middleware, but keep all else the same. """

        super(DecoratorTestCase, self).setUp()

        # At this point we know that the middleware is in ``MIDDLEWARE_CLASSES``,
        # either because it was their in the first place, or because we added it
        # in a super class's setUp() methode, which we called above. Thus there
        # is no need to check for it.
        classes = list(settings.MIDDLEWARE_CLASSES)
        classes.remove(self.gcframe_middleware)
        settings.MIDDLEWARE_CLASSES = classes

    def test_mware_classes(self):
        # A bit of a meta-test, but for sanity's sake I want to be sure that
        # the middleware is not installed.
        self.assertNotIn(self.gcframe_middleware, settings.MIDDLEWARE_CLASSES)
