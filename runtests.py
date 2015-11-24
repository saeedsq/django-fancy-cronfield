#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import os
import sys
import django
from django.conf import settings

from fancy_cronfield.utils.compat import DJANGO_1_5, DJANGO_1_6


def main(*test_args):
    if not test_args:
        test_args = ['fancy_cronfield']

    os.environ['DJANGO_SETTINGS_MODULE'] = 'fancy_cronfield.tests.settings'
    from django.test.utils import get_runner

    if not (DJANGO_1_5 or DJANGO_1_6):
        django.setup()

    test_runner_class = get_runner(settings)
    test_runner = test_runner_class()
    failures = test_runner.run_tests(test_args)
    sys.exit(bool(failures))

if __name__ == '__main__':
    main(*sys.argv[1:])
