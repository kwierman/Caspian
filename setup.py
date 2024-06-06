#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages



setup(
    name='caspian',
    version='0.1.0',
    description="Dask Design Patterns for Data Lakes",
    long_description="TODO: Fill in",
    author="Kevin Wierman",
    author_email='kwierman@gmail.com',
    url='https://github.com/kwierman/caspian',
    packages=find_packages(),
    package_dir={'caspian':
                 'caspian'},
    entry_points={
        'console_scripts': [
            'caspian=caspian.cli:cli'
        ]
    },
    include_package_data=True,
    install_requires=[],
    license="MIT license",
    zip_safe=False,
    keywords='caspian',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=[]
)
