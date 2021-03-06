
import os
import glob

from setuptools import setup, find_packages

VERSION='1.6.2'

setup(
    name = 'ansiblereporter',
    keywords = 'system management ansible automation reporting',
    description = 'Scripts for ansible to report host output data',
    author = 'Ilkka Tuohela',
    author_email = 'hile@iki.fi',
    version = VERSION,
    url = 'https://github.com/codento/ansiblereporter/',
    license = 'PSF',
    packages = find_packages(),
    scripts = glob.glob('bin/*'),
    install_requires = (
        'ansible>=1.8.4',
        'systematic>=4.2.6',
        'seine>=3.0.0',
        'boto',
        'termcolor',
    ),
)

