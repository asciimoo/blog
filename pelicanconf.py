#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Adam Tauber'
SITENAME = 'asciiblog'
SITEURL = 'https://asciimoo.github.io/blog'
RELATIVE_URLS = True

SITELOGO = SITEURL + '/images/logo.png'
SITESUBTITLE = ""
COPYRIGHT_YEAR = "2017"

THEME = 'Flex'

PATH = 'content'

TIMEZONE = 'Europe/Budapest'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Code', 'https://github.com/asciimoo'),)

# Social widget
SOCIAL = (('github', 'https://github.com/asciimoo'),
          ('rss', SITEURL + '/' + FEED_ALL_ATOM))

DEFAULT_PAGINATION = 25
