.. _index:
.. module:: gcframe.tests
   :synopsis: How to check current build status and run tests locally.

Tests
=====

|Build status|_

.. |Build status| image::
   https://secure.travis-ci.org/benspaulding/django-gcframe.png
.. _Build status: http://travis-ci.org/benspaulding/django-dcframe

``gcframe`` has a decent test suite, though it can and will be improved in time.

Current build status can be found at
http://travis-ci.org/benspaulding/django-gcframe.

To run tests, be sure Django is installed, then run::

    django-admin.py test gcframe --settings="gcframe.tests.settings"

If you have not installed ``gcframe``, but are working from a Git checkout, you
will need to either have it on your ``PYTHONPATH`` or run the above command from
the root of the repository.

.. note:: In order for ``gcframe`` tests to run in your project, you will need
          to add ``gcframe`` to your ``INSTALLED_APPS``. (Mentioned here because
          no other ``gcframe`` functionality requires this.)
