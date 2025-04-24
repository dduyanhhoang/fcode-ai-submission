# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='supply_chain_manager',
    version='0.1.0',
    description='F-Code python final project',
    long_description=readme,
    author='Anh Hoang, Triet Nguyen',
    author_email='dduyanhhoang@gmail.com',
    url='https://github.com/dduyanhhoang/supply_chain_manager',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
