#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.core.validators import MaxLengthValidator
from django.db import models
from django.utils import six
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _

from fancy_cronfield.validators import CronValidator
from fancy_cronfield.widgets import CronWidget


class CronField(models.Field):
    """
    Custom cron field which extends CharField and does extra initializations:

     - Enforcing maximum length of 120 by default, using `max_length`
     - Checks if daily limit is provided via `daily_limit` option
     - Appends `CronValidator` to field validators

    """
    _("String (up to %(max_length)s)")

    def __init__(self, *args, **kwargs):
        kwargs.update({'max_length': kwargs.get('max_length', 120)})
        self.daily_limit = kwargs.pop('daily_limit', None)
        super(CronField, self).__init__(*args, **kwargs)
        self.validators.append(MaxLengthValidator(self.max_length))
        self.validators.append(CronValidator(self.daily_limit))

    def get_internal_type(self):
        """
        It is most similar to Django CharField class

        :return: string `CharField`
        """
        return "CharField"

    def to_python(self, value):
        if isinstance(value, six.string_types) or value is None:
            return value
        return smart_text(value)

    def get_prep_value(self, value):
        value = super(CronField, self).get_prep_value(value)
        return self.to_python(value)

    def formfield(self, **kwargs):
        """ Returns a django.forms.Field instance for this database field
        which uses CronWidget for supporting gentle select UI.

        Passing max_length to widgets.CronWidget means that the value's length
        will be validated twice. This is considered acceptable since we want
        the value in the form field (to pass into widget for example).

        :param kwargs: dict, form field key word arguments
        :return: django.forms.Field instance
        """
        defaults = {'max_length': self.max_length, 'widget': CronWidget}
        defaults.update(kwargs)
        return super(CronField, self).formfield(**defaults)
