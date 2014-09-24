#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'galgeek'
SITENAME = u'galgeek'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('github','http://github.com/galgeek'),
          ('linkedin','www.linkedin.com/in/baramiller/'),
          ('twitter', 'http://twitter.com/galgeek'),
          ('phone','tel:1-503-616-5427'),)

DEFAULT_PAGINATION = 10

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'cerulean'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_CATEGORIES_ON_MENU = False
OUTPUT_RETENTION = ('.git', 'CNAME')
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
DATE_FORMATS = {
        'en': '%A, %d %B %Y',
}
TWITTER_USERNAME = 'galgeek'
GITHUB_URL = 'http://github.com/galgeek'
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}