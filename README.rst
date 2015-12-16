#######################
Django Fancy Cron Field
#######################
.. image:: https://travis-ci.org/saeedsq/django-fancy-cronfield.svg?branch=develop
    :target: http://travis-ci.org/saeedsq/django-fancy-cronfield
.. image:: https://img.shields.io/pypi/v/django-fancy-cronfield.svg
    :target: https://pypi.python.org/pypi/django-fancy-cronfield/
.. image:: https://img.shields.io/pypi/pyversions/django-fancy-cronfield.svg
    :target: https://pypi.python.org/pypi/django-fancy-cronfield/
.. image:: https://img.shields.io/pypi/status/django-fancy-cronfield.svg
    :target: https://pypi.python.org/pypi/django-fancy-cronfield/
.. image:: https://img.shields.io/pypi/dm/django-fancy-cronfield.svg
    :target: https://pypi.python.org/pypi/django-fancy-cronfield/
.. image:: https://img.shields.io/badge/wheel-yes-green.svg
    :target: https://pypi.python.org/pypi/django-fancy-cronfield/
.. image:: https://img.shields.io/pypi/l/django-fancy-cronfield.svg
    :target: https://pypi.python.org/pypi/django-fancy-cronfield/
.. image:: https://codecov.io/github/saeedsq/django-fancy-cronfield/coverage.svg?branch=develop
    :target: https://codecov.io/github/saeedsq/django-fancy-cronfield?branch=develop
.. image:: https://readthedocs.org/projects/django-fancy-cronfield/badge/?version=latest
    :target: http://django-fancy-cronfield.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status
.. image:: https://landscape.io/github/saeedsq/django-fancy-cronfield/develop/landscape.svg?style=flat
   :target: https://landscape.io/github/saeedsq/django-fancy-cronfield/develop
   :alt: Code Health
.. image:: https://api.codacy.com/project/badge/grade/1c49af5cdb564cfe979d26384436c85f
    :target: https://www.codacy.com/app/saeed-sq/django-fancy-cronfield
.. image:: https://codeclimate.com/github/saeedsq/django-fancy-cronfield/badges/gpa.svg
   :target: https://codeclimate.com/github/saeedsq/django-fancy-cronfield
   :alt: Code Climate

A nice and customizable cron field with great, easy to use UI.

.. ATTENTION:: To propose features, always open pull requests on the **develop** branch.
   It's the branch for features that will go into the next django fancy cronfield feature release.

   For fixes for 0.1.x releases, please work on support/0.1.x which
   contains the next patch release for 0.1.x series.

   The **master** branch is the current stable release, the one released on PyPI.
   Changes based on **master** will not be accepted.


********
Features
********

- Cron widget providing nice gentle select UI
- Cron format validation
- Custom django field
- Ability to specify a daily run limit

************
Requirements
************

Fancy cron field requires Django version 1.5 up to 1.9, Python 2.6, 2.7, 3.3,
3.4 and python-crontab 1.9.3.

*************
Documentation
*************

Please head over to `documentation`_ for all the details on how to install,
customize and use the django fancy cronfield.

.. _documentation: http://django-fancy-cronfield.readthedocs.org/en/latest/

********
Tutorial
********

http://django-fancy-cronfield.readthedocs.org/en/latest/intro/index.html

************
Installation
************

.. code:: shell

    pip install django-fancy-cronfield

***********
Basic usage
***********

Add `'fancy_cronfield'` to your `INSTALLED_APPS`, then use `CronField` like
any regular model field:

.. code:: python

    from django.db import models

    from fancy_cronfield.fields import CronField


    class MyModel(models.Model):
        timing = CronField()

************
Getting Help
************

Please Write to our `mailing list
<https://groups.google.com/forum/#!forum/django-fancy-cronfield>`_.

*******
Credits
*******

* Crontab API features borrowed from
  `python-crontab <https://code.launchpad.net/python-crontab>`_.