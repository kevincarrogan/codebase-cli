from os.path import join as pjoin
from setuptools import setup

setup(
    name='codebase-cli',
    description='A CLI for codebasehq.com',
    author='Kevin Morgan',
    version='0.0.1',
    scripts=[pjoin('bin', 'cb')],
    requires=[],
)
