.. _index:
.. module:: gcframe.tests
   :synopsis: How to check current build status, run tests locally.

Development
===========

Tests
-----

|Build status|_

.. |Build status| image::
   https://secure.travis-ci.org/benspaulding/django-gcframe.png
.. _Build status: http://travis-ci.org/benspaulding/django-dcframe

``gcframe`` has a decent test suite, which can and will improve in time.

Current build status can be found at `Travis CI`_.

.. _Travis CI: http://travis-ci.org/benspaulding/django-gcframe

To run tests, be sure Django is installed, then run::

    django-admin.py test gcframe --settings="gcframe.tests.settings"

If you have not installed ``gcframe``, but are working from a Git checkout, you
will need to either have it on your ``PYTHONPATH`` or run the above command from
the root of the repository.

.. note:: In order for ``gcframe`` tests to run in your project, you will need
          to add ``gcframe`` to your ``INSTALLED_APPS``. (Mentioned here because
          no other ``gcframe`` functionality requires this.)

Documentation
-------------

The documentation is written in plain text, viewable practially anywhere. An
HTML version of the docs can be found online at `Read the Docs`_. If you want
to build a local version of these, you can install Sphinx_, and then from the
``doc`` directory in this repository, run::

    make html

You will find the built docs in the ``docs/_build/html`` directory.

.. _Read The Docs: http://readthedocs.org/docs/django-gcframe/
.. _Sphinx: http://sphinx.pocoo.org/
