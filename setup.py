from os.path import join as pjoin
from setuptools import setup

setup(
    name='Codebase CLI',
    version='0.0.1',
    scripts=[pjoin('bin', 'cb')],
    requires=[],
)
