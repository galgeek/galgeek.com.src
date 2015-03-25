#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'galgeek'
SITENAME = u'galgeek'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
FEED_DOMAIN = 'http://www.galgeek.com'

# Blogroll
LINKS = (('cool tools', 'http://kk.org/cooltools/'),
         ('pelican', 'http://getpelican.com/'),
         ('python.org', 'http://python.org/'),
         ('jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('github','http://github.com/galgeek'),
          ('linkedin','http://www.linkedin.com/in/baramiller/'),
         #('mozillians','https://mozillians.org/u/galgeek/'),
         # ('ravelry', 'http://www.ravelry.com/projects/baraherself'),
          ('twitter', 'http://twitter.com/galgeek'),
          ('flickr', 'https://www.flickr.com/photos/bara77'),
          ('phone','tel:1-503-616-5427'),
        )

DEFAULT_PAGINATION = 10

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'readable'
CUSTOM_CSS = 'static/custom.css'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_CATEGORIES_ON_MENU = False
OUTPUT_RETENTION = ('.git', 'CNAME', 'README.md')
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
DATE_FORMATS = {
        'en': '%A, %d %B %Y',
}
TWITTER_USERNAME = 'galgeek'
TWITTER_WIDGET_ID = 580613804570079232
GITHUB_URL = 'http://github.com/galgeek'
STATIC_PATHS = ['images', 'bjm', 'extra/CNAME', 'extra/README.md', 'extra/custom.css']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/README.md': {'path': 'README.md'},
                       'extra/custom.css': {'path': 'static/custom.css'},
                       }
AVATAR = 'images/FairDaffodils.jpg'
ABOUT_ME = 'it generalist<br />Portland, Oregon, USA<br />formerly of Prague... San&nbsp;Francisco... New&nbsp;York... Chagrin&nbsp;Falls'
SHOW_ARTICLE_AUTHOR = False
SHOW_ARTICLE_CATEGORY = False
CC_LICENSE = 'CC-BY-SA'

USE_OPEN_GRAPH = False

PYGMENTS_STYLE = 'friendly'

SHARIFF = True
