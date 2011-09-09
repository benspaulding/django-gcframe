import os

from distutils.core import setup

from gcframe import VERSION


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-gcframe',
    version=VERSION,
    description='Django middleware and decorators for working with Google Chrome Frame.',
    url='https://github.com/benspaulding/django-gcframe/',
    author='Ben Spaulding',
    author_email='ben@benspaulding.us',
    license='BSD',
    download_url='https://github.com/benspaulding/django-gcframe/tarball/v%s' % VERSION,
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
