#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name="django-template-test",
    version="0.1.1",
    license='BSD',
    description="A basic django template used for testing.",
    author='Ivan Diao',
    author_email='adieu@adieu.me',
    url='http://github.com/adieu/django-template-test',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
