#!/usr/bin/env python

import sys
from setuptools import setup

setup(
    name='connect-api',
    version='0.1.0',
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