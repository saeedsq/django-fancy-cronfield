#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import sys
from fancy_cronfield.utils.compat import DJANGO_1_5

if DJANGO_1_5:
    if sys.version_info < (2, 7):
        import unittest2 as unittest_module
    else:
        import unittest as unittest_module

    def suite():
        loader = unittest_module.TestLoader()
        return loader.discover("fancy_cronfield.tests", pattern="*.py")
