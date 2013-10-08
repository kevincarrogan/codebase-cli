from os.path import join as pjoin
from setuptools import setup

setup(
    name='codebase-cli',
    description='A CLI for codebasehq.com',
    author='Kevin Morgan',
    author_email='kevin.d.morgan@gmail.com',
    url='http://github.com/kevindmorgan/codebase-cli',
    version='0.1.3',
    scripts=[pjoin('bin', 'cb')],
    requires=[],
)
