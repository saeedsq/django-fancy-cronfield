#######################
Django Fancy Cron Field
#######################
.. image:: https://travis-ci.org/saeedsq/django-fancy-cronfield.svg?branch=develop
    :target: http://travis-ci.org/saeedsq/django-fancy-cronfield
.. image:: https://img.shields.io/pypi/v/django-fancy-cronfield.svg
    :target: https://pypi.python.org/pypi/django-fancy-cronfield/
.. image:: https://img.shields.io/pypi/dm/django-fancy-cronfield.svg
    :target: https://pypi.python.org/pypi/django-fancy-cronfield/
.. image:: https://img.shields.io/badge/wheel-yes-green.svg
    :target: https://pypi.python.org/pypi/django-fancy-cronfield/
.. image:: https://img.shields.io/pypi/l/django-fancy-cronfield.svg
    :target: https://pypi.python.org/pypi/django-fancy-cronfield/
.. image:: https://codeclimate.com/github/saeedsq/django-fancy-cronfield/badges/gpa.svg
   :target: https://codeclimate.com/github/saeedsq/django-fancy-cronfield
   :alt: Code Climate
.. image:: https://codeclimate.com/github/saeedsq/django-fancy-cronfield/badges/coverage.svg
    :target: https://codeclimate.com/github/saeedsq/django-fancy-cronfield/coverage

A nice and customizable cron field with great, easy to use UI.

.. ATTENTION:: To propose features, always open pull requests on the **develop** branch.
   It's the branch for features that will go into the next django fancy cronfield feature release.

   For fixes for 0.1.x releases, please work on **support/0.1.x** which contains
   the next patch release for 0.1.x series.

   The **master** branch is the current stable release, the one released on PyPI.
   Changes based on **master** will not be accepted.


********
Features
********

- Cron format validation
- Custom django field
- Gentle select UI
- Ability to specify a daily run limit

************
Requirements
************

Fancy cron field requires Django 1.5, Python 2.6 and python-crontab 1.9.3

************
Installation
************

.. code:: shell

    pip install django-fancy-cronfield

***********
Basic usage
***********

Use it like any regular model field:

.. code:: python

    from django.db import models

    from fancy_cronfield.fields import CronField


    class MyModel(models.Model):
        timing = CronField()

************
Getting Help
************

Please Write to our `mailing list <https://groups.google.com/forum/#!forum/django-fancy-cronfield>`_.