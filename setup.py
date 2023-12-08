#!/usr/bin/env python
from admin_honeypot import __description__, __license__, __version__


try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import find_packages, setup

setup(
    name='django-admin-honeypot',
    version=__version__,
    description=__description__,
    long_description=open('./README.rst', encoding='utf-8').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    keywords='django admin honeypot trap',
    maintainer='Derek Payton',
    maintainer_email='derek.payton@gmail.com',
    url='https://github.com/dmpayton/django-admin-honeypot',
    download_url='https://github.com/dmpayton/django-admin-honeypot/tarball/v%s' % __version__,
    license=__license__,
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'django-ipware',
    ],
)
