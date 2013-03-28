================
Django Stopwatch
================

api metrics collector middleware for django

.. image:: https://api.travis-ci.org/z4r/django-stopwatch.png?branch=master
    :target: http://travis-ci.org/z4r/django-stopwatch

.. image:: https://coveralls.io/repos/z4r/django-stopwatch/badge.png?branch=master
    :target: https://coveralls.io/r/z4r/django-stopwatch

This package provides a django middleware to collect API metrics.


.. contents::
    :local:

.. _installation:

Installation
============
::

    $ pip install django-stopwatch


.. _usage:

Usage
=====
::

    MIDDLEWARE_CLASSES += (
        'stopwatch.middleware.StopWatchMiddleware',
    )

.. _keybuilder:

Configuration and Default
=========================

::

    STOPWATCH_KEYBUILDER = 'stopwatch.keybuilders.RestApiKeyBuilder'
    STOPWATCH_BACKENDS = (
        'stopwatch.backends.StatsDStopWatchBackend',
    )
    STOPWATCH_STATSD_PREFIX = stopwatch
    STOPWATCH_STATSD_HOST = None
    STOPWATCH_STATSD_PORT = None

.. _license:

License
=======

This software is licensed under the ``Apache License 2.0``. See the ``LICENSE``
file in the top distribution directory for the full license text.
