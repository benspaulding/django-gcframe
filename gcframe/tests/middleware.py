from django import http
from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase

from gcframe.middleware import GoogleChromeFrameIEMiddleware


class GCFrameTestCase(TestCase):
    """A concrete and subclass-able test case."""

    urls = 'gcframe.tests.urls'

    def setUp(self):
        # Add these as instance attrs because they are used in other methods
        # and subclasses.
        self.old_MIDDLEWARE_CLASSES = settings.MIDDLEWARE_CLASSES
        self.gcframe_middleware = 'gcframe.middleware.GoogleChromeFrameIEMiddleware'

        if self.gcframe_middleware not in settings.MIDDLEWARE_CLASSES:
            # TODO: Once it is determined if order of this middleware matters,
            # adjust this bit accordingly.
            # TODO: Account for the case where ``MIDDLEWARE_CLASSES`` is a list.
            settings.MIDDLEWARE_CLASSES += (self.gcframe_middleware,)

    def tearDown(self):
        settings.MIDDLEWARE_CLASSES = self.old_MIDDLEWARE_CLASSES

    def test_mware_classes(self):
        # A bit of a meta-test, but for sanity's sake I want to be sure that
        # the class has been added.
        self.assertIn(self.gcframe_middleware, settings.MIDDLEWARE_CLASSES)


class MiddlewareTestCase(GCFrameTestCase):

    # TODO: Test for the content of the header, not just its presence, including:
    #     - Custom compat_mode
    #     - No compat_mode
    #     - Custom act_method

    def test_header_added(self):
        response = self.client.get(reverse('gcframe-test-normal'))
        self.assertTrue(response.has_header('X-UA-Compatible'))

    def test_header_already_added(self):
        response = self.client.get(reverse('gcframe-test-framed'))
        self.assertTrue(response.has_header('X-UA-Compatible'))

    def test_response_exempted(self):
        response = self.client.get(reverse('gcframe-test-exempt'))
        self.assertFalse(response.has_header('X-UA-Compatible'))
