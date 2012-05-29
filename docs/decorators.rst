.. _decorators:
.. module:: gcframe.decorators
   :synopsis: Decorators that alter the ``X-UA-Compatible`` header on a
              per-view basis.

Decorators
==========

Overview
--------

These decorators allow you to apply or remove the ``X-UA-Compatible`` HTTP
header on individual views.

Available Decorators
--------------------


.. _gcframe:

gcframe
~~~~~~~

This decorator applies the ``X-UA-Compatible`` HTTP header to individual views,
rather than site-wide as :doc:`GoogleChromeFrameIEMiddleware <middleware>`
does.

::

    from gcframe.decorators import gcframe

    @gcframe()
    def some_view(request):
        …

.. note::

   The trailing ``()`` are required on this decorator, even when no arguments
   are passed.

It accepts the key-word arguments ``compat_mode`` and ``act_method``. These
arguments correspond to :ref:`GCF_IE_COMPATIBILITY_MODE` and
:ref:`GCF_IE_ACTIVATION_METHOD`, respectively.

Using these arguments is useful when you wish to set the ``X-UA-Compatible``
HTTP header to something different than the default that is being used by this
decorator on other views or by the middleware site-wide.

::

    from gcframe.decorators import gcframe

    @gcframe(act_method='IE7')
    def some_view(request):
        …


.. _gcframe_exempt:

gcframe_exempt
~~~~~~~~~~~~~~

This decorator instructs the :doc:`GoogleChromeFrameIEMiddleware <middleware>`
to **not** set the ``X-UA-Compatible`` HTTP header.

::

    from gcframe.decorators import gcframe_exempt

    @gcframe_exempt
    def some_view(request):
        …

Obviously this will only affect change when the middleware is installed. It is
harmless if the middleware is not installed.
