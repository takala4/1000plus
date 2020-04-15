#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime

AUTHOR = 'takala4'
SITENAME = '1000plus'
SITEURL = '.'

LOAD_CONTENT_CACHE = False


PATH = 'content'
OUTPUT_PATH = 'diary'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'
DEFAULT_DATE_FORMAT = ('%Y-%b-%d')

USER_LOGO_URL = 'https://github.com/takala4/cv/blob/master/image/4-black.png?raw=true'

THEME = "pelican-themes/pelican-hss-takala"




# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# To create previous/next article link
DAY1 = datetime.timedelta(days=1)

# Plugin
PLUGIN_PATHS = ["pelican-plugins",]
PLUGINS = ["render_math",
           "tag_cloud",
           "sitemap"]

SITEMAP = {
    'format': 'xml'
}

#
USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = True


# Blogroll
# LINKS = (('Twitter', ''),
#         ('GitHub', ''),
#         ('Personal Home Page', ''),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

SOCIAL_SHARE_BUTTONS = (
    'twitter', 'facebook', 'hatebu', 'pocket', 'googleplus'
)

SHOW_SOCIAL_SHARE_BUTTON = True

# DEFAULT_PAGINATION = 10

DIRECT_TEMPLATES = ['index', 'tags', 'archives', 'top_index']


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True




