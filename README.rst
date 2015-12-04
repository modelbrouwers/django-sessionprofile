Django Sessionprofile
=====================

.. image:: https://travis-ci.org/modelbrouwers/django-sessionprofile.svg?branch=master
    :target: https://travis-ci.org/modelbrouwers/django-sessionprofile


.. image:: https://coveralls.io/repos/modelbrouwers/django-sessionprofile/badge.svg
  :target: https://coveralls.io/r/modelbrouwers/django-sessionprofile


.. image:: https://readthedocs.org/projects/django-sessionprofile/badge/?version=latest
  :target: https://readthedocs.org/projects/django-sessionprofile/?badge=latest


.. image:: https://img.shields.io/pypi/v/django-sessionprofile.svg
  :target: https://pypi.python.org/pypi/django-sessionprofile


django-sessionprofile is the bridge between any software with customizable
auth backends and Django. If you want to use Django for Single-Sign-On, this
package does the Django heavy lifting.


Installation - Django
---------------------

    $ pip install django-sessionprofile

Add `sessionprofile` to INSTALLED_APPS, and run `python manage.py migrate`.

Add the sessionprofile middleware (`sessionprofile.middleware.SessionProfileMiddleware`) to your middleware settings - make sure it comes before the `SessionMiddleware`.

Additionally, the session cookie must be available for the third party application,
this should not be a problem if it lives on the same domain.

Backend
-------
Currently one backend is available: `'sessionprofile.backends.DatabaseBackend'`.
In the future, alternative backends will be possible, like `'sessionprofile.backends.CachedDatabaseBackend'`.

Installation - third party application
--------------------------------------
This depends on which backend you decided to use, the example assumes the db
backend.

When authenticating in the third party application, you should read the session
cookie (SESSION_COOKIE_NAME), and query the sessionprofile table:

    SELECT users_user.username, users_user.email FROM
    users_user, sessionprofile_sessionprofile sp WHERE
    sp.session_id = '<sessionid_from_cookie>'
    AND users_user.id = sp.user_id

It's up to you to implement the rest of the authentication flow. An example for phpBB 3.0.x is provided in the docs.

Thanks
------
Many thanks go to Resolver Systems Ltd (now part of PythonAnywhere) who
made the initial version of this library, specifically aimed on phpBB3.

Todo
----
Django 1.9 will ship with customizable DB Session Backends, we might provide
such a backend which would reduce the need for the middleware.

See `Github PR`_.

.. _`Github PR`: https://github.com/sergeykolosov/django/commit/e9b913f1213f8debbc7692b37df637e6143a54c0
