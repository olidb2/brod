#!/usr/bin/env python

import setuptools

install_requires = [
    "zc.zk==0.5.2",
]

setuptools.setup(
    name = 'brod',
    version = '0.3.2',
    license = 'MIT',
    description = open('README.md').read(),
    author = "Datadog, Inc.",
    author_email = "packages@datadoghq.com",
    url = 'https://github.com/datadog/brod',
    platforms = 'any',
    packages = ['brod'],
    zip_safe = True,
    verbose = False,
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'broderate = brod.util:broderate'
        ]
    }
)
