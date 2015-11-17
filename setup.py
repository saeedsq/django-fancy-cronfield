#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from setuptools import setup
import os
import fancy_cronfield

CLASSIFIERS = [
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
]

INSTALL_REQUIREMENTS = [
    'django>=1.5,<1.6',
    'python-crontab==1.9.3',
]

readme_path = os.path.join(os.path.dirname(__file__), 'README.rst')
long_description = open(readme_path).read()

setup(
    name="django-fancy-cronfield",
    author="Saeed Salehian",
    author_email="saeed.sq@gmail.com",
    version=fancy_cronfield.__version__,
    description="A nice and customizable cronfield",
    long_description=long_description,
    url='https://github.com/saeedsq/django-fancy-cronfield',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIREMENTS,
    extras_require={},
    packages=["fancy_cronfield"],
    include_package_data=True,
    zip_safe=False,
    test_suite='runtests.main',
)
