#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import find_packages
from distutils.core import setup


version_tuple = __import__('django_js_reverse').VERSION
version = '.'.join([str(v) for v in version_tuple])
setup(
    name='django-js-reverse',
    version=version,
    license='MIT',
    description='Javascript url handling for Django that doesn\'t hurt.',
    author='Bernhard Janetzki',
    author_email='boerni@gmail.com',
    url='https://github.com/version2/django-js-reverse',
    download_url='http://pypi.python.org/pypi/django-js-reverse/',
    packages=find_packages(),
    package_data={
        'django_js_reverse': [
            'templates/django_js_reverse/*',
        ]
    },
    install_requires=[
        'Django >= 1.3',
    ],
)