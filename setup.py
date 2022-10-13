#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = [
    "coloredlogs",
    "Flask",
]

setup_requirements = [
]

test_requirements = [
]

description = "A simple random quote generator"
# In case of long description
# description +=

setup(
    author="Ludovic Rivallain",
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description=description,
    long_description_content_type = "text/markdown",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='cestpasle_generator',
    name='cestpasle_generator',
    packages=find_packages(include=['cestpasle_generator', 'cestpasle_generator.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/lrivallain/cestpasle_generator',
    version='0.1.0',
    zip_safe=False,
)
