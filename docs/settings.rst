.. _settings:
.. module:: gcframe.settings

Configurable Settings
=====================

Overview
--------

There are a couple of configurable settings that define the content of
the ``X-UA-Compatible`` HTTP header.

Realistically, virtually no one will need to modify these. But if you
do, here they are.


.. _settings-list:

List of Settings
----------------

.. _GCF_IE_COMPATIBILITY_MODE:

GCF_IE_COMPATIBILITY_MODE
~~~~~~~~~~~~~~~~~~~~~~~~~

Default: ``'Edge'`` (If :abbr:`GCF (Google Chrome Frame)` is not
activated, use the highest compatibility mode available.)

Other options include:

    * ``None``
    * ``'5'``
    * ``'6'``
    * ``'7'``
    * ``'EmulateIE7'``
    * ``'8'``

Before using any of these options, please consult the `MSDN META Tags`_
article. Be sure they do what you think they do. Virtually everyone will
be best served by using the default ``'Edge'`` value.

Note that the first option listed, ``None``, will turn off compatibility
mode changing.

.. _MSDN META Tags: http://msdn.microsoft.com/library/cc817574.aspx


.. _GCF_IE_ACTIVATION_METHOD:

GCF_IE_ACTIVATION_METHOD
~~~~~~~~~~~~~~~~~~~~~~~~

Default: ``'1'`` (Activate GCF on all version of Internet Explorer that
have it installed.)

Other options include:

    * ``IE6``
    * ``IE7``
    * ``IE8``

These values activate GCF only on the named Internet Explorer version
and older. Newer versions will behave according to the given
:ref:`compatibility mode <GCF_IE_COMPATIBILITY_MODE>`.

For further information, see the GCF `developer documentation`_.

Again, few people will need to change this setting. A value of ``'1'``
will likely serve you best.

.. _developer documentation: http://www.chromium.org/developers/how-tos/chrome-frame-getting-started
