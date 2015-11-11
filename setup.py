# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '1.0.0'

setup(
    name='fleet',
    version=version,
    description='Fleet Management Application',
    author='Revant Nandgaonkar',
    author_email='revant.one@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
