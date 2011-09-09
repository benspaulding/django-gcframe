.. _index:
.. module:: gcframe

Django Google Chrome Frame
==========================

Overview
--------

``django-gcframe`` is a set of Django utilities for working with Google
Chrome Frame.

Specifically, the package provides configurable middleware and
decorators for adding and removing the ``X-UA-Compatible`` HTTP haeder
in view responses. Said header conditionally activates Google Chrome
Frame when installed on Microsoft Internet Explorer, and conditionally
enables a compatibility mode when :abbr:`GCF (Google Chrome Frame)` is
not activated.

This package does not install Google Chrome Frame, though in the future
it may have features that would promote installation.


Contents
--------

.. toctree::
    :maxdepth: 2

    getting_started
    middleware
    decorators
    settings


Indices, etc.
-------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
