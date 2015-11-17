#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from distutils.version import LooseVersion
import django

# These means "less than or equal to DJANGO_FOO_BAR"
DJANGO_1_5 = LooseVersion(django.get_version()) < LooseVersion('1.6')
DJANGO_1_6 = LooseVersion(django.get_version()) < LooseVersion('1.7')
DJANGO_1_7 = LooseVersion(django.get_version()) < LooseVersion('1.8')
DJANGO_1_8 = LooseVersion(django.get_version()) < LooseVersion('1.9')
DJANGO_1_9 = LooseVersion(django.get_version()) < LooseVersion('2.0')
