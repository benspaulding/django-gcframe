Getting Started
===============

Overview
--------

`Google Chrome Frame`_ is a plug-in for Internet Explorer that causes
the browser to behave like Google Chrome, using the Webkit rendering
engine.

Because many sites are made to work for Internet Explorer and rely on
its proprietary or broken technologies, :abbr:`GCF (Google Chrome Frame)`
is not activated by default. Rather, it is activated when the requested
resource has a particlar ``X-UA-Compatible`` HTTP response header. 

This application does not install the GCF plug-in. It merely allows for
simple and configurable sending of the necessary header to activate the
plug-in for those Internet Explorer users with it installed, and for
those who don’t it makes use of the highest compatibility mode available.

For further information on GCF, see the `developer documentation`_,
particularly the `Getting Started`_ article. More information
regarding IE compatibility modes can be found on MSDN_.

.. _Google Chrome Frame: http://en.wikipedia.org/wiki/Google_Chrome_Frame
.. _developer documentation: https://code.google.com/chrome/chromeframe/
.. _Getting Started: http://www.chromium.org/developers/how-tos/chrome-frame-getting-started
.. _MSDN: http://msdn.microsoft.com/library/cc817574.aspx


Requirements
------------

``django-gcframe`` requires Python 2.4 or newer and a functional
installation of Django 1.2 or newer.


Installation & Usage
--------------------

To install this package, run the following command at the root of the
package directory::

    python setup.py install

If you have the Python ``easy_install`` utility available, you can
also type the following to download and install in one step::

   easy_install django-gcframe

Or if you're using ``pip``::

    pip install django-gcframe

Or if you’d prefer you can simply place the included ``gcframe``
directory somewhere on your Python path, or symlink to it from
somewhere on your Python path; this is useful if you’re working from a
Git checkout.

You can then begin using the middleware and/or decorators in your
Django project.

Middleware
~~~~~~~~~~

To send the default ``X-UA-Compatible`` HTTP header site-wide simply add
the middleware to your ``MIDDLEWARE_CLASSES`` setting::

    MIDDLEWARE_CLASSES = (
        …
        'gcframe.middleware.GoogleChromeFrameIEMiddleware',
        …
    )

For further details, see :doc:`middleware`.

Decorators
~~~~~~~~~~

There is a decorator for adding or overriding the ``X-UA-Compatible``
HTTP header on individual views. There is also one for removing it from
individual views when the middleware is adding it site-wide.

For further details, see :doc:`decorators`.

Configuration
~~~~~~~~~~~~~

There are two settings that allow for modification of the
``X-UA-Compatible`` HTTP header. Find them at :doc:`settings`.

Support
-------

Bugs and feature requests can be submitted to the `GitHub issue
tracker`_.

.. _GitHub issue tracker: https://github.com/benspaulding/django-gcframe/issues/

This package does not yet have a test suite, but one will be written in
the near future.

Features Not Yet Included
~~~~~~~~~~~~~~~~~~~~~~~~~

There are a few things that this middleware could do which it does not.
This is because I know of no data indicating that the features are
worth the time they would take to implement, and they could be difficult
to do properly because they involve inspecting the User Agent string.

    * Sending the header only to IE.
    * Requiring all IE users to have GCF installed.
    * Requiring only IE users matching the condition of activation to
      have GCF installed.

I am not opposed to these features, I just don’t feel like implementing
them right now. Feel free to do it yourself or try to convince me to.

There is one more feature that I do think could be useful. It would be a
set of tools that would allow a site to gracefully prompt IE users to
install GCF. It would likely involve some User Agent string inspection,
a context processor that would set a context variable to indicate the
state of the IE, and session fu that would allow an IE user to be
prompted once to install the plug-in. If you are interested in pursuing
this yourself, see the Chrome developer guide for `detecting and
prompting to install`_.

.. _detecting and prompting to install: http://www.chromium.org/developers/how-tos/chrome-frame-getting-started#TOC-Detecting-Google-Chrome-Frame-and-P
