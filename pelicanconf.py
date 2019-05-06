#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Guest'
SITENAME = 'Daniel Guest'
SITETITLE = 'Daniel Guest'
SITESUBTITLE = 'PhD student<br>Department of Psychology<br>University of Minnesota'
SITEURL = 'http://localhost:8000'
SITELOGO = SITEURL + '/images/profile.jpg'

#ROBOTS = 'index, follow'

THEME = "pelican-themes/Flex"
PATH = 'content'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

USE_FOLDER_AS_CATEGORY = True 
MAIN_MENU = False 
HOME_HIDE_TAGS = True

STATIC_PATHS = ['images', 'download', 'pages']

#MENUITEMS = (('Archives', '/archives.html'),
#             ('Categories', '/categories.html'),
#             ('Tags', '/tags.html'),)

SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

#PLUGIN_PATHS = ['pelican-plugins']
#PLUGINS = ['assets']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
