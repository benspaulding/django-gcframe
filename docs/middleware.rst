.. _middleware:
.. module:: gcframe.middleware

Middleware
==========

Overview
--------

The ``GoogleChromeFrameIEMiddleware`` middleware adds an
``X-UA-Compatible`` HTTP header to the response of all views. When using
default settings (which you should), this header activates
:abbr:`GCF (Google Chrome Frame)` in all versions of Microsoft Internet
Explorer that have it installed. Those that do not have GCF installed
will instead use the highest `compatibility mode`_ available to them.

.. _note:

Views can be exempt from the header addition by using the
``gcframe_exempt`` decorator.


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

.. _note:

For more information on middleware ordering, see the Django
documentation’s `middleware reference`_ and `middleware topic`_.

.. _compatibility mode: http://msdn.microsoft.com/library/cc817574.aspx
.. _middleware reference: https://docs.djangoproject.com/en/dev/ref/middleware/
.. _middleware topic: https://docs.djangoproject.com/en/1.2/topics/http/middleware/#activating-middleware
