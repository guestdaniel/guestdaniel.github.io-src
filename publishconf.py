#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Guest'
SITENAME = 'Daniel Guest'
SITEURL = 'https://guestdaniel.github.io'
SITETITLE = 'Daniel Guest'
SITESUBTITLE = 'PhD student<br>Department of Psychology<br>University of Minnesota'
SITELOGO = SITEURL + '/images/profile.jpg'

ROBOTS = 'index, follow'

THEME = "pelican-themes/Flex"
PATH = 'content'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
COPYRIGHT_YEAR = True

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

STATIC_PATHS = ['images', 'download', 'pages']

#MENUITEMS = (('Archives', '/archives.html'),
#             ('Categories', '/categories.html'),
#             ('Tags', '/tags.html'),)

LINKS = ()

SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

#PLUGIN_PATHS = ['pelican-plugins']
#PLUGINS = ['assets']

#DELETE_OUTPUT_DIRECTORY = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
