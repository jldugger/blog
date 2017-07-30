# -*- coding: utf-8 -*-
AUTHOR = u'Justin Dugger'
SITENAME = u"Justin Dugger"
# SITESUBTITLE = 'a blog of heartbreaking genius and staggering work'
SITEURL = 'https://www.pwnguin.net'

PATH = './content/'
OUTPUT_PATH = "./output"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = 'en_US.utf8'
TIMEZONE = 'America/Los_Angeles'

FRONT_PAGE_ITEM_COUNT = 10
WITH_PAGINATION = True
DEFAULT_PAGINATION = 5

# feed settings

FEED_RSS = 'rss20.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
FEED_DOMAIN = SITEURL

STATIC_PATHS = ["pictures", ]

# theme settings
THEME = "./borrowedidea/"
DISQUS_SITENAME = "jlduggersblog"
GOOGLE_ANALYTICS = "UA-10247293-1"
CSS_FILE = "wide.css"

# DISPLAY_PAGES_ON_MENU = True # (default)
MENUITEMS = (('Github', 'https://github.com/jldugger/'),
             ('Photos', '//www.pwnguin.net/albums/')
             )

LINKS = (('John Cantrell', 'http://notsoevil.net'),
         ('Toby Murray', 'http://ksmapper.blogspot.com/'),
         ('sgstair', "http://blog.akkit.org/"),
         ('zanshin', "http://zanshin.net/"),)

SOCIAL = (('twitter', 'http://twitter.com/WildPwnguin'),
          ('linkedin', 'http:/www.linkedin.com/in/justindugger'),
          )

# GITHUB_URL = 'https://github.com/jldugger'
# GITHUB_POSITION = "left" # (default)

# TWITTER_USERNAME = 'WildPwnguin'
