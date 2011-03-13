# -*- coding: utf-8 -*-
AUTHOR = u'Justin Dugger'
SITENAME = u"Justin Dugger" 
SITEURL = '//pwnguin.net'

OUTPUT_PATH = "/var/www/www.pwnguin.net/"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = 'en_US.utf8'

WITH_PAGINATION = True
DEFAULT_PAGINATION = 5

FEED_RSS = 'rss20.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

STATIC_PATHS = ["pictures",]

# theme settings
THEME = "./borrowedidea/"
DISQUS_SITENAME = "jlduggersblog"
GOOGLE_ANALYTICS = "UA-10247293-1"
CSS_FILE = "wide.css"

MENUITEMS = (('Projects','//pwnguin.net/websvn/'),
             ('Albums','//pwnguin.net/albums/')
            )

LINKS = (('John Cantrell', 'http://notsoevil.net'),
            ('Toby Murray', 'http://ksmapper.blogspot.com/'),
            ('sgstair', "http://blog.akkit.org/"),
            ('zanshin',"http://zanshin.net/"),)

SOCIAL = (('twitter', 'http://twitter.com/WildPwnguin'),
          )

