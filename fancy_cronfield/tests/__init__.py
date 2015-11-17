from fancy_cronfield.utils.compat import DJANGO_1_5

if DJANGO_1_5:
    import unittest

    def suite():
        loader = unittest.TestLoader()
        return loader.discover("fancy_cronfield.tests", pattern="*.py")
