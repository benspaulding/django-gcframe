# -*- coding: utf-8 -*-

"""
Django utilities for working with Google Chrome Frame.

This package provides configurable middleware and decorators for adding
and removing the ``X-UA-Compatible`` HTTP header in view responses. Said
header conditionally activates Google Chrome Frame when installed on
Microsoft Internet Explorer, and conditionally enables a compatibility
mode when GCF is not activated.

Refer to the documentation_ for further information.

.. _documentation: http://readthedocs.org/docs/django-gcframe/

"""

from __future__ import unicode_literals


__version__ = '1.0'
