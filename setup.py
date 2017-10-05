#!/usr/bin/env python

import sys
from setuptools import setup

if sys.version_info < (2, 7):
    sys.exit('Python 2.7 or higher is required')

setup(
    name='connect-api',
    version='0.0.3',
    description='Resilio Connect API',
    author='Resilio Inc.',
    author_email='support@resilio.com',
    url='https://resilio.com',
    packages=[
        'connect_api',
        'connect_api.models'
    ],
    install_requires=[
        'requests'
    ]
)