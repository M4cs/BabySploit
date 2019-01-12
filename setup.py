#!/usr/bin/env python3

import sys, requests
from setuptools import setup, find_packages

with open('PYPIREADME.md', encoding='utf-8') as f:
    long_description = f.read()
long_description += '\n\n'

setup(
    name='babysploit',
    version='1.2',
    author='Max Bridgland',
    author_email='mabridgland@protonmail.com',
    description='Beginner Pentesting Toolkit/Framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/M4cs/BabySploit',
    packages=['babysploit'],
    install_requires=[
        'netifaces',
        'urllib3',
        'humanfriendly',
        'terminaltables',
        'pyfiglet',
        'requests',
        'raccoon-scanner'
    ],
    project_urls={
        'Wiki': 'https://github.com/M4cs/BabySploit/wiki',
        'Discord Server': 'https://discordapp.com/invite/7VN9VZe'
    },
    license='GNU General Public License v3 (GPLv3) (GPL)',
    zip_safe=True,
    entry_points={
        'console_scripts':[
            'babysploit = babysploit.__main__:main',
        ],
    },
    tests_require=[
        'mock;python_version<"3"',
        'pytest',
        'pytest-cov'
    ],
    classifiers=[  # Used by PyPI to classify the project and make it searchable
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: IronPython',
        'Programming Language :: Python :: Implementation :: Jython',

        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ]
)
