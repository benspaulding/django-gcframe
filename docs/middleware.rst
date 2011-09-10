.. _middleware:
.. module:: gcframe.middleware
   :synopsis: Middleware that adds the ``X-UA-Compatible`` header site-wide.

Middleware
==========

Overview
--------

The ``GoogleChromeFrameIEMiddleware`` middleware adds an
``X-UA-Compatible`` HTTP header to the response of all views. When using
default settings (which you should), this header activates
:abbr:`GCF (Google Chrome Frame)` in all versions of Internet Explorer
that have it installed. Those that do not have GCF installed will
instead be directed to use the highest `compatibility mode`_ available
to them.

.. tip::

   Views can be exempt from the header addition by using the
   :func:`gcframe_exempt` decorator.


Installation
------------

Install the middleware by adding it your ``MIDDLEWARE_CLASSES`` setting::

    MIDDLEWARE_CLASSES = (
        …
        'gcframe.middleware.GoogleChromeFrameIEMiddleware',
        …
    )

Put it somewhere in the middle-ish of the list. An exact ordering
position is not necessary (to my knowledge), but putting in the middle
will at least ensure that it’s not outside of other middleware that
require being near the start or end.

.. tip::
   The content of the ``X-UA-Compatible`` header can be altered using by
   overriding settings in :mod:`gcframe.settings`.

.. _compatibility mode: http://msdn.microsoft.com/library/cc817574.aspx
