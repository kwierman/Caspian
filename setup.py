#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name="caspian",
    version="0.1.0",
    description="Dask Design Patterns for Data Lakes",
    long_description=""" Caspian provides advances tooling for setting up and implementing datalakes using Dask as the primary compute engine.""",
    author="Kevin Wierman",
    author_email="kwierman@gmail.com",
    url="https://github.com/kwierman/caspian",
    packages=find_packages(exclude=['tests', 'docs', 'examples']),
    package_dir={"caspian": "caspian"},
    entry_points={"console_scripts": ["caspian=caspian.cli:main"]},
    include_package_data=True,
    install_requires=[
        'dask',
        'distributed',
        'fastapi',
        'SQLAlchemy',
        'uvicorn'
    ],
    license="MIT license",
    zip_safe=False,
    keywords="caspian",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    test_suite="tests",
    tests_require=[],
)
