#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import sys

try:
    from django.conf import settings

    settings.configure(
        DEBUG=True,
        LANGUAGE_CODE='en-us',
        ALLOWED_HOSTS=[],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'fancy_cronfield',
            }
        },
        TIME_ZONE='Asia/Tehran',
        USE_I18N=True,
        USE_L10N=True,
        USE_TZ=True,
        ROOT_URLCONF='',
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sites',
            'fancy_cronfield',
        ),
        SITE_ID=1,
        MIDDLEWARE_CLASSES=(
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        ),
    )

    try:
        import django

        setup = django.setup
    except AttributeError:
        pass
    else:
        setup()

except ImportError:
    import traceback

    traceback.print_exc()
    raise ImportError('To fix this error, run: pip install -r test_requirements/base.txt')


def main(*test_args):
    if not test_args:
        test_args = ['fancy_cronfield']

    # Run tests
    try:
        # Django <= 1.8
        from django.test.simple import DjangoTestSuiteRunner
        test_runner = DjangoTestSuiteRunner(verbosity=1)
    except ImportError:
        # Django >= 1.8
        from django.test.runner import DiscoverRunner
        test_runner = DiscoverRunner(verbosity=1)

    failures = test_runner.run_tests(test_args)
    sys.exit(failures)


if __name__ == '__main__':
    main(*sys.argv[1:])
