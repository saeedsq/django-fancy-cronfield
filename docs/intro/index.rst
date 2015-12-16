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

Django fancy cronfield extend Field, so all options available at
Field can be used with CronField as well. Here is a list of
kwargs which CronField has added or altered:

 - `max_length`: is set to 120 by default, however you can override it at will.
 - `daily_limit`: Specifies maximum value which cron frequency per day can be.
   `None` means no limit.

Please see :doc:`/reference/fields` for an inside look into CronField.

**************
Widget Options
**************

Django fancy cronfield comes with a useful custom widget which provides a
gentle select UI for specifying cron strings at administration panel. However
you can customize the widget UI behaviour by passing `options` dictionary to
``CronWidget`` constructor.

For example, if you want to customize the ``CronWidget`` for the timing
``CronField`` of ``Schedule`` to use <select> instead of the default gentle
select, you can override the field’s widget and pass your desired options:

.. code-block:: django

    from django import forms
    from fancy_cronfield.widgets import CronWidget

    from myapp.models import Schedule


    class ScheduleForm(forms.ModelForm):
        class Meta:
            model = Schedule
            fields = ('name', 'timing')
            widgets = {
                'timing': CronWidget(
                    attrs={'class': 'special'},
                    options={'use_gentle_select': True}
                ),
            }

.. note::

    Please note that `options` parameter differs from `attrs` which is used
    to specify html attributes. `options` are limited to a list of predefined
    items which are described below.

Here are the list of options that you can use to customize UI behaviour:

.. attribute:: use_gentle_select

    :default: ``True`` means using gentle select UI by default

    Boolean that determines if the widget should use gentle select UI or simple
    select input.

.. attribute:: allow_multiple_all

    :default: ``False``

    Boolean that decides if the widget should allow multiple selection on all
    cron parts. When this is `True`, the user can select multiple values for
    each cron part. `False` meant that cron parts are not forced to allow
    multiple selection, and each cron part's individual option will decide
    about the behaviour.

.. attribute:: allow_multiple_dom

    :default: ``True``

    Boolean that decides if the widget should allow multiple selection on
    `day of month` cron part.

.. attribute:: allow_multiple_month

    :default: ``True``

    Boolean that decides if the widget should allow multiple selection on
    `month` cron part.

.. attribute:: allow_multiple_dow

    :default: ``True``

    Boolean that decides if the widget should allow multiple selection on
    `day of week` cron part.

.. attribute:: allow_multiple_hour

    :default: ``True``

    Boolean that decides if the widget should allow multiple selection on
    `hour` cron part.

.. attribute:: allow_multiple_minute

    :default: ``True``

    Boolean that decides if the widget should allow multiple selection on
    `minute` cron part.

Below you can find an example options dictionary, these options indicates that
the widget should use gentle select to render itself, allow multiple selection
on day of month, month and day of week. However multiple selection is not
allowed for hour and minute part.

Example::

    options = {
        'use_gentle_select': True,
        'allow_multiple_all': False,
        'allow_multiple_dom': True,
        'allow_multiple_month': True,
        'allow_multiple_dow': True,
        'allow_multiple_hour': False,
        'allow_multiple_minute': False
    }


.. note::

    There might be a case where you need to use the default ``TextInput``
    widget instead of ``CronWidget``. It could easily be done by overriding
    the field’s widget in ModelForm.

Please see :doc:`/reference/widgets` for an inside look into CronWidget.