#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'pythonwood'
SITENAME = '一个Linux迷,Python粉——在Linux中折腾Python的行者。'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['static','favicon.ico','google2f77d410527d7bc1.html']

GOOGLE_ANALYTICS = 'UA-109845932-1'
DISQUS_SITENAME = "pythonwood-github-io"
THEME = "./pelican-clean-blog-theme"

DEFAULT_DATE_FORMAT = '%b%d, %H:%M'
READERS = {'html': None}

# for pelican-clean-blog

# HEADER_COVER = './static/img/header_cover.png'

GITHUB_URL = 'http://github.com/pythonwood'
TWITTER_URL = 'http://twitter.com/myprofile'
FACEBOOK_URL = 'http://facebook.com/myprofile'

COLOR_SCHEME_CSS = 'monokai.css'
