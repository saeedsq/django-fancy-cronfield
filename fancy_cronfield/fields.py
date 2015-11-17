#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.db import models

from fancy_cronfield.validators import CronValidator


class CronField(models.CharField):
    """ Custom cron field which extends CharField and does extra initializations:

     - Enforcing maximum length of 120 using `max_length`
     - Checks if daily limit is provided via `daily_limit` option
     - Appends `CronValidator` to field validators

    """
    def __init__(self, *args, **kwargs):
        kwargs.update({'max_length': kwargs.get('max_length', 120)})
        self._daily_limit = kwargs.pop('daily_limit', None)
        super(CronField, self).__init__(*args, **kwargs)
        self.validators.append(CronValidator(self._daily_limit))
