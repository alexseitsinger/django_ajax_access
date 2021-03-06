#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages
from setup_utils import read, read_markdown

PACKAGE_NAME = "django-ajax-access"
SOURCE_DIR_NAME = "ajax_access"
GITHUB_URL = "https://github.com/alexseitsinger/{}".format(PACKAGE_NAME)
HOMEPAGE_URL = "https://www.alexseitsinger.com/packages/python/{}".format(PACKAGE_NAME)
README_NAME = "README.md"

setup(
    name=PACKAGE_NAME,
    version=read(("src", SOURCE_DIR_NAME, "__init__.py"), "__version__"),
    description=read_markdown((README_NAME,), "Description", (0,)),
    long_description=read((README_NAME,)),
    long_description_content_type="text/markdown",
    author="Alex Seitsinger",
    author_email="software@alexseitsinger.com",
    url=HOMEPAGE_URL,
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["tests"]),
    include_package_data=True,
    license="BSD 2-Clause License",
    keywords=["django", "ajax", "login", "logout"],
    install_requires=["Django", "django-ratelimit"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Content Management System",
    ],
    project_urls={
        "Documentation": HOMEPAGE_URL,
        "Source": GITHUB_URL,
        "Tracker": "{}/issues".format(GITHUB_URL),
    },
)
