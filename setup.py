#!/usr/bin/env python3
# coding: utf-8

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='setOp',
    version='0.1.1',
    author='wws',
    author_email='onewesong@gmail.com',
    url='https://github.com/onewesong/setOp',
    description='Compared files with through python set operations.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['setop'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'setop=setop:main',
        ]
    }
)
