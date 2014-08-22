import os

from setuptools import setup

setup(
    name='codebase-cli',
    description='A CLI for codebasehq.com',
    author='Kevin Carrogan',
    author_email='kevin.carrogan@gmail.com',
    url='http://github.com/kevindmorgan/codebase-cli',
    version='0.1.7',
    scripts=[os.path.join('bin', 'cb')],
    requires=[],
)
