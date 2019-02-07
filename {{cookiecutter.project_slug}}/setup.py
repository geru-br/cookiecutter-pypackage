#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [{%- if cookiecutter.command_line_interface|lower == 'click' %}'Click>=6.0',{%- endif %} ]

setup_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest-runner',{%- endif %} ]

test_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest',{%- endif %} ]

{%- set license_classifiers = {
    'GERU Intelectual Property': 'License :: Other/Proprietary',
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

{%- set language_classifiers = {
        'English': 'Natural Language :: English',
        'Portuguese (Brazilian)': 'Natural Language :: Portuguese (Brazilian)',
} %}

setup(
    author="{{ cookiecutter.author_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    url='{{ cookiecutter.project_github_url }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.license] }}',
{%- endif %}
{%- if cookiecutter.language in language_classifiers %}
        '{{ language_classifiers[cookiecutter.language] }}',
{%- endif %}
{%- if cookiecutter.python_version in ["2", "6"] %}
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
{%- endif %}
{%- if cookiecutter.python_version in ["3", "6"] %}
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
{%- endif %}
    ],
    description="{{ cookiecutter.project_short_description }}",
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main',
        ],
    },
    {%- endif %}
    install_requires=requirements,
{%- if cookiecutter.license in license_classifiers %}
    license="{{ cookiecutter.license }}",
{%- endif %}
    long_description=readme,
    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }}',
    name='{{ cookiecutter.project_slug }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    version='{{ cookiecutter.version }}',
    zip_safe=False,
)
