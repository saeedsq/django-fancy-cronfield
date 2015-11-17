#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

"""
Tests for `fancy_cronfield` validators
"""

from django.test import TestCase
from django.core.exceptions import ValidationError
from fancy_cronfield.validators import CronValidator


class CronValidatorTestCases(TestCase):
    def setUp(self):
        self.cron_validator = CronValidator(limit_value=None)

    def test_cron_format_validation(self):
        """
        Cron Format:
        * * * * *
        min (0 - 59)
        hour (0 - 23)
        day of month (1 - 31)
        month (1 - 12)
        day of week (0 - 6) (0 to 6 are Sunday to Saturday, or use names;
        7 is Sunday, the same as 0)

        Examples:
        30 0 1 1,6,12 * # 00:30 Hrs  on 1st of Jan, June & Dec.
        0 20 * 10 1-5 # 8.00 PM every weekday (Mon-Fri) only in Oct.
        0 0 1,10,5 * * # midnight on 1st, 10th & 15th of month
        5,10 0 10 * 1 # At 12.05,12.10 every Monday & on 10th of every month
        """
        crons = [
            "* * * * *", "0 0 12 * *", "0 15 10 * *",
            "0 0,12 1 */2 *", "0 2 1-10 * *", "0 4 15-21 * 1",
            "0 4 8-14 * *", "30 08 10 06 *", "00 11,16 * * *",
            "00 09-18 * * *", "00 09-18 * * 1-5", "0 2 * * *",
            "0 5,17 * * *", "0 17 * * sun", "*/10 * * * *",
            "* * * jan,may,aug *", "0 17 * * sun,fri", "0 2 * * sun",
            "0 */4 * * *", "0 4,17 * * sun,mon", "00 10 * * *",
            "30 0 * * *",
        ]

        try:
            for cron in crons:
                self.cron_validator(cron)
        except ValidationError:
            self.fail("CronValidator raised ValidationError for %s" % cron)

    def test_invalid_cron_format(self):
        """
        Tests that if CronValidator raises error for invalid cron strings
        """
        crons = [
            "* * 32 * *", "0- 0 12 * *", "60 15 10 * *",
            "0 24 1 */2 *", "0 2 1/10 * *", "04 15-21 * 1",
            "0 4 8-14 13 *", "30 08 10 07 8", "11,16 * * *",
            "00 09-18 * * * *", "00 09*18 * * 1-5", "0 2 0* * *",
            "0 5,-17 * * *", "0 17 ** * sun", "*/10 * * *-2 *",
            "* * * * jan,may,aug", "0 17 * sun,fri *", "0 2 sun * *",
            "0/2 */4 * * *", "0 4,17 * * sun,mun", "60 10 * * *",
            "30 0  * * *", "30 0 *  * *", "30 0 * *  *"
        ]

        for cron in crons:
            self.assertRaises(ValidationError, self.cron_validator, value=cron)

    def test_cron_daily_limit(self):
        """
        Tests that if the CronValidator checks daily frequency limit correctly
        """
        # Valid daily frequency
        crons = {
            # cron: daily_limit
            "1 12 * * *": 1,
            "0 8,15 * * *": 2,
            "0 9,14,19 * * *": 3,
            "0,30 10,17 2-10 1,2,3 7": 4,
            "*/10 20 * * *": 6,
            "15 */2 * * *": 12,
            "*/10 */1 * * *": 6 * 24,
            "10 * 9 4 6,1": None,
        }

        for (cron, daily_limit) in crons.items():
            cron_validator = CronValidator(limit_value=daily_limit)
            try:
                cron_validator(cron)
            except ValidationError:
                failure_message = "CronValidator raised ValidationError for %s with limit %s"
                self.fail(failure_message % (cron, daily_limit))

        # Cron string exceeds daily frequency limit
        crons = {
            "1 12 * * *": 0,
            "0 8,15 * * *": 1,
            "0 9,14,19 * * *": 2,
            "0,30 10,17 2-10 1,2,3 7": 3,
            "*/10 20 * * *": 3,
            "15 */2 * * *": 11,
            "*/10 */1 * * *": 6 * 24 - 1,
            "10 * 9 4, 6,1": 23,
        }

        for (cron, daily_limit) in crons.items():
            cron_validator = CronValidator(limit_value=daily_limit)
            self.assertRaises(ValidationError, cron_validator, value=cron)
