from fancy_cronfield.utils.compat import DJANGO_1_5

if DJANGO_1_5:
    import unittest


    def suite():
        return unittest.TestLoader().discover("fancy_cronfield.tests", pattern="*.py")
