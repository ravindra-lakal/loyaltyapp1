# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='loyaltyapp1',
    version=version,
    description='Gives Loyalty apps to customers',
    author='New Indictrans Technologies PVT LTD',
    author_email='ravindra.l@indictranstech.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
