#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Copyright © 2021 sanbo Inc. All rights reserved.
@Description: 
@Version: 1.0
@Create: 2021-01-15 12:32:21
@author: sanbo

'''
import setuptools

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="IuKey",
    version="1.2.0",
    author="sanbo",
    author_email="sanbo.xyz@gmail.com",
    description="Idea key Update. support:LanZouCloud API-2.5.8.2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hhhaiai/IuKey",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
        "requests_toolbelt"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
