.. _settings:
.. module:: gcframe.settings
   :synopsis: Configurable settings that affect the behavior of the middleware
              and decorators.

Settings
========

Overview
--------

There are a couple of configurable settings that define the content of the
``X-UA-Compatible`` HTTP response header. Realistically, virtually no one will
need to modify these. But if you do, simply set a custom value for them in your
:file:`settings.py`.


Available Settings
------------------

.. _GCF_IE_COMPATIBILITY_MODE:

GCF_IE_COMPATIBILITY_MODE
~~~~~~~~~~~~~~~~~~~~~~~~~

The default value is ``'Edge'``. This means that if :abbr:`GCF (Google Chrome
Frame)` is not activated :abbr:`IE (Internet Explorer)` will use the highest
compatibility mode available. Other values include:

* ``None``
* ``'5'``
* ``'6'``
* ``'7'``
* ``'EmulateIE7'``
* ``'8'``

A value of ``None``, will turn off compatibility mode changing. Other values
correspond to various Internet Explorer browser modes. Virtually everyone will
be best served by using the default value of ``'Edge'``.

.. seealso::

   More information on compatibility modes can be found in the MSDN article
   `META Tags and Locking in Future Compatibility`_.

.. _META Tags and Locking in Future Compatibility: http://msdn.microsoft.com/library/cc817574.aspx


.. _GCF_IE_ACTIVATION_METHOD:

GCF_IE_ACTIVATION_METHOD
~~~~~~~~~~~~~~~~~~~~~~~~

Default value is ``'1'``. This means that all versions of IE with GCF installed
will activate it. Other options include:

* ``'IE6'``
* ``'IE7'``
* ``'IE8'``

These values activate GCF only on the named IE version and older. Newer
versions will behave according to the value of :ref:`GCF_IE_COMPATIBILITY_MODE`.
Again, few people will need to change this setting. A value of ``'1'``
will likely serve you best.

.. seealso::

   The `GCF developer documentation`_ has more information regarding activation
   methods.

.. _GCF developer documentation: http://www.chromium.org/developers/how-tos/chrome-frame-getting-started
