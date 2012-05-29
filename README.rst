============================
 Django Google Chrome Frame
============================

|Build status|_

.. |Build status| image::
   https://secure.travis-ci.org/benspaulding/django-gcframe.png
.. _Build status: http://travis-ci.org/benspaulding/django-dcframe

Django utilities for working with Google Chrome Frame.

This package provides configurable middleware and decorators for adding and
removing the ``X-UA-Compatible`` HTTP header in view responses. Said header
conditionally activates Google Chrome Frame when installed on Microsoft
Internet Explorer, and conditionally enables a compatibility mode when GCF is
not activated.

Refer to the documentation_ for further information.

.. _documentation: http://readthedocs.org/docs/django-gcframe/
