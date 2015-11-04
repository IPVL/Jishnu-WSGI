#! /usr/bin/env python

[app:greeting]
paste.app_factory = configured:app_factory
name = Bharney
greeting = Bienvenu

[filter:caseless]
paste.filter_app_factory = configured:filter_factory

[pipeline:main]
pipeline =
    caseless
    greeting
