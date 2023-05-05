=========
Changelog
=========

3.0.0 (2023-05-05)
==================

Periodic version compatibility release.

**Breaking changes 💥**

* Dropped support for Python 3.7
* Dropped support for Django 4.0

The library likely still works on those versions, but they are no longer tested.

**Other changes**

* Confirmed support for Python 3.11
* Confirmed support for Django 4.2

2.0.0 (2022-10-30)
==================

Maintenance release

While the library has continued working without issues since 1.0 more than 6 years ago,
it was time for some cleanup. A new major version is released because of the dropped
support for older Python and Django versions, functionally nothing has changed and
upgrading should be straight-forward on modern Python/Django versions.

* Dropped Python 2 support
* Dropped support for Django older than 3.2 (= any end-of-life Django versions)
* Migrated from Travis CI to Github actions
* Restructured project tests and adopted pytest
* Dropped unused dependencies
* Moved from coveralls to Codecov
* Overhauled/restructured documentation and README
* Formatted code with black and isort
* Updated package metadata


1.0.0 (2016-08-13)
==================

Initial stable release
