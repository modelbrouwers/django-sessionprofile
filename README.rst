=====================
Django Sessionprofile
=====================

Keep track of Django user sessions.

|build-status| |code-quality| |black| |coverage| |docs|

|python-versions| |django-versions| |pypi-version|

django-sessionprofile is a library to track which user a django session belongs to.
Possible useful scenario's for this information include:

* Single-Sign-On (SSO) between different applications that can read Django's session
  cookie (same-origin setup)
* Single Logout (SLO) initiated in another application, triggering logout in yours
* Audit trail and security - allowing you to manage user sessions on other devices.

Usage and installation
======================

**Cheat sheet**

#. ``pip install django-sessionprofile``
#. Add ``"sessionprofile"`` to your ``INSTALLED_APPS``
#. Add ``"sessionprofile.middleware.SessionProfileMiddleware"`` to the ``MIDDLEWARE``
   setting, before Django's ``SessionMiddleware``
#. ``python manage.py migrate``

**Full instructions**

See the `documentation <https://django-sessionprofile.readthedocs.io/en/latest/>`_
for more information, with more code-examples and context.


Credits
-------

Many thanks go to Resolver Systems Ltd (now part of PythonAnywhere) who
made the initial version of this library, specifically aimed at phpBB3.


.. |build-status| image:: https://github.com/modelbrouwers/django-sessionprofile/workflows/Run%20CI/badge.svg
    :alt: Build status
    :target: https://github.com/modelbrouwers/django-sessionprofile/actions?query=workflow%3A%22Run+CI%22

.. |code-quality| image:: https://github.com/modelbrouwers/django-sessionprofile/workflows/Code%20quality%20checks/badge.svg
     :alt: Code quality checks
     :target: https://github.com/modelbrouwers/django-sessionprofile/actions?query=workflow%3A%22Code+quality+checks%22

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. |coverage| image:: https://codecov.io/gh/modelbrouwers/django-sessionprofile/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/modelbrouwers/django-sessionprofile
    :alt: Coverage status

.. |docs| image:: https://readthedocs.org/projects/django-sessionprofile/badge/?version=latest
    :target: https://django-sessionprofile.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |python-versions| image:: https://img.shields.io/pypi/pyversions/django-sessionprofile.svg

.. |django-versions| image:: https://img.shields.io/pypi/djversions/django-sessionprofile.svg

.. |pypi-version| image:: https://img.shields.io/pypi/v/django-sessionprofile.svg
    :target: https://pypi.org/project/django-sessionprofile/
