.. _decorators:
.. module:: gcframe.decorators

Decorators
==========

Overview
--------

These decorators allow you to apply or remove the ``X-UA-Compatible``
HTTP header from individual views.

gcframe
-------

:func:`gcframe(compat_mode='Edge', act_method='1')`

.. _function:: gcframe(compat_mode='Edge', act_method='1')
    :module: gcframe.decorators

The ``@gcframe()`` decorator allows the ``X-UA-Compatible`` HTTP
header to be added to individual views, rather than site-wide as the
middleware does.

::

    from gcframe.decorators import gcframe

    @gcframe()
    def some_view(request):
        …

.. _note:

Note that the ``()`` are required on this decorator, even when no
arguments are being passed.

Arguments
~~~~~~~~~

This decorator can be passed two arguments. They correspond to
configurable settings, and default to those settings when no arguments
are passed. They are useful if you wish to set the ``X-UA-Compatible``
HTTP header to something different than the default that is being used
widely by this decorator on other views or by the middleware site-wide.

compat_mode
^^^^^^^^^^^

See the :ref:`GCF_IE_COMPATIBILITY_MODE` setting.

act_method
^^^^^^^^^^

See the :ref:`GCF_IE_ACTIVATION_METHOD` setting.


gcframe_exempt
--------------

The ``@gcframe_exempt`` decorator instructs the
:doc:`GoogleChromeFrameIEMiddleware <middleware>` to **not** set the
``X-UA-Compatible`` HTTP header.

::

    from gcframe.decorators import gcframe_exempt

    @gcframe_exempt
    def some_view(request):
        …

Obviously this will only do anything when the middleware is installed.
But it is harmless if it’s not installed.
