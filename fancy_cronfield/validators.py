#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from crontab import CronTab

from django.utils.translation import ugettext as _
from django.core.validators import BaseValidator
from django.core.exceptions import ValidationError


class CronValidator(BaseValidator):
    """ Cron format validator which does the following actions:

        - Ensures that the cron string is a valid cron format
        - Ensures that the cron frequency per day is less than `limit_value`

    """
    code = "cron"
    message = ' '.join([
        _("Ensure that your selected timing runs at most %(limit_value)s times per day."),
        _("It runs %(show_value)s times per day.")
    ])
    error_messages = {
        'invalid_cron': _("Ensure that your selected timing is valid."),
    }

    def clean(self, value):
        """ Ensures that the given value is a valid cron format
        and strips it.

        :param value: cron string
        :return: Stripped value string
        """
        cron = CronTab().new()
        if value and not cron.setall(value.strip()):
            raise ValidationError(self.error_messages['invalid_cron'])
        return value.strip()

    def __call__(self, value):
        cleaned_value = self.clean(value)

        if self.limit_value is not None:
            cron = CronTab().new()
            cron.setall(cleaned_value)

            if cron.frequency_per_day() > self.limit_value:
                params = {
                    'limit_value': self.limit_value,
                    'show_value': cron.frequency_per_day()
                }
                raise ValidationError(
                    self.message % params,
                    code=self.code,
                    params=params,
                )

        return cleaned_value
