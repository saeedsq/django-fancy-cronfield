#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

"""
Tests for `fancy_cronfield` widgets
"""
import copy

from django.test import SimpleTestCase

from fancy_cronfield.widgets import CronWidget


class CronWidgetTests(SimpleTestCase):
    widget = CronWidget()

    def check_html(self, widget, name, value, html='', attrs=None, **kwargs):
        output = widget.render(name, value, attrs=attrs, **kwargs)
        self.assertHTMLEqual(output, html)

    def test_render(self):
        html = '<input data-fancy="cron" type="hidden" name="timing"'
        html += ' id="id_timing" data-allow_multiple_dom="1"'
        html += ' data-allow_multiple_dow="1" data-allow_multiple_hour="1"'
        html += ' data-allow_multiple_minute="1" data-allow_multiple_month="1"'
        html += ' data-use_gentle_select="1" />'

        self.check_html(
            widget=self.widget, name='timing', value='', html=html,
            attrs={'id': 'id_timing'}
        )

    def test_render_none(self):
        html = '<input data-fancy="cron" type="hidden" name="timing"'
        html += ' id="id_timing" data-allow_multiple_dom="1"'
        html += ' data-allow_multiple_dow="1" data-allow_multiple_hour="1"'
        html += ' data-allow_multiple_minute="1" data-allow_multiple_month="1"'
        html += ' data-use_gentle_select="1" />'

        self.check_html(
            widget=self.widget, name='timing', value=None,
            html=html, attrs={'id': 'id_timing'}
        )

    def test_render_custom_attrs(self):
        html = '<input data-fancy="cron" type="hidden" name="timing"'
        html += ' id="id_timing" data-allow_multiple_dom="1"'
        html += ' data-allow_multiple_dow="1" data-allow_multiple_hour="1"'
        html += ' data-allow_multiple_minute="1" data-allow_multiple_month="1"'
        html += ' data-use_gentle_select="1" class="fun"/>'

        self.check_html(
            widget=self.widget, name='timing', value='',
            html=html, attrs={'id': 'id_timing', 'class': 'fun'},
        )

    def test_constructor_attrs(self):
        self.maxDiff = None
        widget = CronWidget(attrs={'id': 'id_timing', 'class': 'fun'})
        html = '<input data-fancy="cron" type="hidden" name="timing"'
        html += ' id="id_timing" data-allow_multiple_dom="1"'
        html += ' data-allow_multiple_dow="1" data-allow_multiple_hour="1"'
        html += ' data-allow_multiple_minute="1" data-allow_multiple_month="1"'
        html += ' data-use_gentle_select="1" class="fun"/>'
        self.check_html(widget=widget, name='timing', value='', html=html)

    def test_attrs_precedence(self):
        """
        `attrs` passed to render() get precedence over those passed to the
        constructor
        """
        widget = CronWidget(attrs={'id': 'id_timing', 'class': 'pretty'})
        html = '<input data-fancy="cron" type="hidden" name="timing"'
        html += ' id="id_timing" data-allow_multiple_dom="1"'
        html += ' data-allow_multiple_dow="1" data-allow_multiple_hour="1"'
        html += ' data-allow_multiple_minute="1" data-allow_multiple_month="1"'
        html += ' data-use_gentle_select="1" class="special"/>'
        self.check_html(
            widget=widget, name='timing', value='',
            html=html, attrs={'id': 'id_timing', 'class': 'special'},
        )

    def check_boolean_option(self, name):
        widget = CronWidget(options={name: True})
        widget_html = widget.render('timing', '')
        self.assertTrue(name in widget_html)

        widget = CronWidget(options={name: False})
        widget_html = widget.render('timing', '')
        self.assertFalse(name in widget_html)

    def test_option_use_gentle_select(self):
        self.check_boolean_option('use_gentle_select')

    def test_option_allow_multiple_all(self):
        self.check_boolean_option('allow_multiple_all')

    def test_option_allow_multiple_dom(self):
        self.check_boolean_option('allow_multiple_dom')

    def test_option_allow_multiple_month(self):
        self.check_boolean_option('allow_multiple_month')

    def test_option_allow_multiple_dow(self):
        self.check_boolean_option('allow_multiple_dow')

    def test_option_allow_multiple_hour(self):
        self.check_boolean_option('allow_multiple_hour')

    def test_option_allow_multiple_minute(self):
        self.check_boolean_option('allow_multiple_minute')

    def test_deepcopy(self):
        """
        __deepcopy__() should copy all attributes properly
        """
        widget = CronWidget()
        obj = copy.deepcopy(widget)
        self.assertIsNot(widget, obj)
        self.assertEqual(widget.options, obj.options)
        self.assertIsNot(widget.options, obj.options)
        self.assertEqual(widget.attrs, obj.attrs)
        self.assertIsNot(widget.attrs, obj.attrs)
