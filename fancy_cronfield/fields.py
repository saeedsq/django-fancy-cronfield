#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.db import models

from fancy_cronfield.validators import CronValidator


class CronField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update({'max_length': 20})
        self._daily_limit = kwargs.pop('daily_limit', None)
        super(CronField, self).__init__(*args, **kwargs)
        self.validators.append(CronValidator(self._daily_limit))
