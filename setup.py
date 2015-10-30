#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import io
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

import fancy_cronfield


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


long_description = read('README.rst', 'CHANGES.rst')


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(
    name="django-fancy-cronfield",
    version=fancy_cronfield.__version__,
    url='https://github.com/saeedsq/django-fancy-cronfield',
    license="The BSD 3-Clause License",
    author="Saeed Salehian",
    # tests_require=['pytest'],
    install_requires=[
        'django==1.5',
        'python-crontab==1.9.3',
    ],
    # cmdclass={'test': PyTest},
    author_email="saeed.sq@gmail.com",
    description="A nice and customizable cronfield with great, easy to use UI.",
    long_description=long_description,
    packages=["fancy_cronfield"],
    include_package_data=True,
    zip_safe=False,
    platforms=['OS Independent'],
    # test_suite='fancy_cronfield.test.test_fancy_cronfield',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django :: 1.5',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        "Programming Language :: Python :: 2.6",
    ],
    extras_require={
        # 'testing': ['pytest'],
    }
)
