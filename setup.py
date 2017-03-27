#!/usr/bin/env python

import sys
from distutils.core import setup

if sys.version_info < (3, 0):
    sys.exit('Python 2 is not supported')

setup(
    name='connect_api',
    version='0.0.1',
    description='Resilio Connect API',
    author='Resilio Inc.',
    author_email='support@resilio.com',
    url='https://resilio.com'
)