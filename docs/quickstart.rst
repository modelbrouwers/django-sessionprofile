==========
Quickstart
==========

Installation
============

Install from PyPI:

.. code-block:: bash

    pip install django-sessionprofile


Then edit your project settings and add the app to your ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = [
        ...,
        "sessionprofile",
        ...,
    ]

and make sure to add the middleware (BEFORE Django's session middleware):

.. code-block:: python
    :linenos:
    :emphasize-lines: 4,5

    MIDDLEWARE = [
        ...,
        "django.middleware.security.SecurityMiddleware",
        "sessionprofile.middleware.SessionProfileMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        ...,
    ]

Finally, run ``migrate`` to create the tables:

.. code-block:: bash

    python manage.py migrate

Usage
=====

Nothing special is required - the middleware takes care of relating sessions and users
for easy lookup.

From time to time you'll want to call the ``sp_clear_expired`` management command to
remove stale data though.

Backends
========

Currently one backend is available: :class:`sessionprofile.backends.db.essionProfileStore`.
There are currently no plans to implement additional backends, but third parties should
be able to figure this out from the source code.

You can control the backend to use via the ``SESSIONPROFILE_BACKEND`` setting, which
is a dotted path to the module implementing a ``SessionProfileStore`` class.
