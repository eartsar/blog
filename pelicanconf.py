#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Eitan Romanoff'
SITENAME = 'Lap One'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Lap One', '/'),
    ("The Map", 'https://roadtrippers.com/map?a2=t!10381588&lat=36.40037&lng=-110.68699&utm_campaign=trip&utm_medium=share&utm_source=copy&z=4'),
    ("Eitan's Posts", '/category/eitan-posts.html'),
    ("Aron's Posts", '/category/aron-posts.html'),
    ("Eitan's Instagram", 'https://www.instagram.com/eitanromanoff/'),
    ("Aron's Instagram", 'https://www.instagram.com/ar0ney/'))

# Social widget
# SOCIAL = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = None

THEME = "./FlexTheme"
