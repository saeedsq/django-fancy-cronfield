#########
Tutorials
#########

The pages in this section of the documentation are aimed at the newcomer.
They're designed to help you get started quickly, and show how
easy it is to work with it as a developer who wants to customise it and
get it working according to their own requirements.

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

*************
Field Options
*************

Django fancy cronfield extend CharField, so all options available at
CharField can be used with CronField as well. Here is a list of
kwargs which CronField has added or altered:

 - `max_length`: is set to 120 by default, however you can override it at will.
 - `daily_limit`: Specifies maximum value which cron frequency per day can be.
   None means no limit.