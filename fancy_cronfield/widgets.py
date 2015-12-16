#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
import copy

from django import forms


# FIXME Issue #17 - z-index issue for CronField UI in inline admins
class CronWidget(forms.TextInput):
    """ CronWidget class providing gentle select UI for cron fields """
    input_type = 'hidden'

    def __init__(self, attrs=None, options=None):
        options = options or {}
        self.options = {
            'use_gentle_select': True,
            'allow_multiple_all': False,
            'allow_multiple_dom': True,
            'allow_multiple_month': True,
            'allow_multiple_dow': True,
            'allow_multiple_hour': True,
            'allow_multiple_minute': True,
        }
        for key in self.options.keys():
            self.options.update({
                key: options.get(key, self.options.get(key))
            })

        attrs = attrs if attrs is not None else {}
        attrs.update({'data-fancy': 'cron'})
        for key in self.options.keys():
            attrs.update({
                'data-%s' % key: self.options.get(key)
            })
        super(CronWidget, self).__init__(attrs)

    def __deepcopy__(self, memo):
        obj = copy.copy(self)
        obj.attrs = self.attrs.copy()
        obj.options = copy.copy(self.options)
        memo[id(self)] = obj
        return obj

    class Media:
        css = {
            'all': (
                'fancy_cronfield/css/cronfield.min.css',
                'fancy_cronfield/css/jquery-cron.min.css',
                'fancy_cronfield/css/jquery-gentleSelect.min.css',
            )
        }
        js = (
            'fancy_cronfield/js/jquery-1.4.1.min.js',
            'fancy_cronfield/js/jquery-cron.min.js',
            'fancy_cronfield/js/jquery-gentleSelect.min.js',
            'fancy_cronfield/js/cronfield.min.js',
        )
