#!/bin/env python
# -*- coding: utf8 -*-


from setuptools import setup, find_packages

version = "0.5.0"

setup(
    name="hackshackersrocsite",
    version=version,
    description="website for hacks/hackers rochester",
    classifiers=[
        "Intended Audience :: Education",
        "Topic :: Education :: Computer Aided Instruction (CAI)",
    ],
    keywords="",
    author="Remy DeCausemaker",
    author_email="remyd@civx.us",
    url="http://hackshackers-rochester.rhcloud.com",
    license="Apache2.0",
    packages=find_packages(
    ),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "flask",
        "mako",
        "flask-mako",
        "flask-markdown",
    ],
    #TODO: Deal with entry_points
    #entry_points="""
    #[console_scripts]
    #pythong = pythong.util:parse_args
    #"""
)
