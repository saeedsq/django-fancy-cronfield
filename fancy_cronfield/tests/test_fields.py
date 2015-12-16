#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import six
from django.utils.functional import lazy

from fancy_cronfield.fields import CronField
from fancy_cronfield.utils.compat import DJANGO_1_6, DJANGO_1_5
from fancy_cronfield.widgets import CronWidget


class CronFieldTests(TestCase):
    def test_get_internal_type(self):
        field = CronField()
        self.assertEqual(field.get_internal_type(), 'CharField')

    def test_to_python(self):
        field = CronField()
        self.assertEqual(field.to_python('0 0 1 1 *'), '0 0 1 1 *')

    def test_get_prep_value(self):
        field = CronField()

        if DJANGO_1_5 or DJANGO_1_6:
            value = field.get_prep_value(six.text_type('0 0 1 1 *'))
        else:
            lazy_func = lazy(lambda: u'0 0 1 1 *', six.text_type)
            value = field.get_prep_value(lazy_func())

        self.assertIsInstance(value, six.string_types)

    def test_get_prep_value_int(self):
        field = CronField()

        if DJANGO_1_5 or DJANGO_1_6:
            value = field.get_prep_value(int(0))
        else:
            lazy_func = lazy(lambda: 0, int)
            value = field.get_prep_value(lazy_func())

        self.assertIsInstance(value, six.text_type)

    def test_max_length_passed_to_formfield(self):
        """
        Test that CronField pass its max_length attributes to
        form fields created using its .formfield() method.
        """
        cf1 = CronField()
        cf2 = CronField(max_length=256)
        self.assertEqual(cf1.formfield().max_length, 120)
        self.assertEqual(cf2.formfield().max_length, 256)

    def test_widget_passed_to_formfield(self):
        f = CronField()
        self.assertEqual(f.formfield().widget.__class__, CronWidget)

    def test_raises_error_on_empty_string(self):
        f = CronField()
        self.assertRaises(ValidationError, f.clean, "", None)

    def test_cleans_empty_string_when_blank_true(self):
        f = CronField(blank=True)
        self.assertEqual('', f.clean('', None))

    def test_raises_error_on_invalid_input(self):
        f = CronField()
        self.assertRaises(ValidationError, f.clean, 'test', None)

    def test_raises_error_on_empty_input(self):
        f = CronField(null=False)
        self.assertRaises(ValidationError, f.clean, None, None)
