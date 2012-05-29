# -*- coding: utf-8 -*-

import os

from distutils.core import setup


here = os.path.dirname(__file__)

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# Function borrowed from carljm.
def get_version():
    fh = open(os.path.join(here, "gcframe", "__init__.py"))
    try:
        for line in fh.readlines():
            if line.startswith("__version__ ="):
                return line.split("=")[1].strip().strip("'")
    finally:
        fh.close()

setup(
    name='django-gcframe',
    version=get_version(),
    description='Django middleware and decorators for working with Google Chrome Frame.',
    url='https://github.com/benspaulding/django-gcframe/',
    author='Ben Spaulding',
    author_email='ben@benspaulding.us',
    license='BSD',
    download_url='https://github.com/benspaulding/django-gcframe/tarball/v%s' % get_version(),
    long_description = read('README.rst'),
    packages = [
        'gcframe',
        'gcframe.tests',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
)
