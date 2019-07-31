# -*- coding: utf-8 -*-

from setuptools import setup

name = '{{ cookiecutter.package_name }}'
description = (
    '{{ cookiecutter.description }}'
)
version = '0.0.0'


def get_long_description():
    readme = open('README.rst').read()
    history = open('HISTORY.rst').read()

    # cut the part before the description to avoid repetition on pypi
    readme = readme[readme.index(description) + len(description):]

    return '\n'.join((readme, history))


setup(
    name=name,
    version=version,
    description=description,
    long_description=get_long_description(),
    url='http://github.com/seantis/{{ cookiecutter.package_name }}',
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.author_email }}',
    license='MIT',
    packages=['{{ cookiecutter.package_name }}'],
    namespace_packages=name.split('.')[:-1],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[

    ],
    extras_require=dict(
        test=[
            'coverage',
            'pytest',
        ],
    ),
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT LIcense',
    ]
)
