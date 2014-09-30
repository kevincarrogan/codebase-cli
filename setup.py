import os

from setuptools import setup

setup(
    name='codebase-cli',
    description='A CLI for codebasehq.com',
    author='Kevin Carrogan',
    author_email='kevin.carrogan@gmail.com',
    url='http://github.com/kevincarrogan/codebase-cli',
    version='0.1.8',
    scripts=[os.path.join('bin', 'cb')],
    requires=[],
)
