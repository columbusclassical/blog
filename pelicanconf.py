AUTHOR = 'Daniel Gibson'
SITENAME = 'CCA Blog'
SITEURL = 'https://columbusclassical.org/blog'
TIMEZONE = 'US/Eastern'
DEFAULT_LANG = 'en'

SUBTITLE = 'Columbus Classical Academy Blog'
SUBTEXT = '''Welcome to the Columbus Classical Academy blog.<br>
 Here we will share news and reflections on classical education.<br>
 <i>Veritas et Virtus</i>
'''
COPYRIGHT = '©2022 Columbus Classical Academy'
PATH = 'content'
OUTPUT_PATH = 'docs/'
THEME = 'themes/Papyrus'
THEME_STATIC_PATHS = ['static']
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'search', 'neighbors', 'pelican-toc']

DISPLAY_PAGES_ON_MENU = True
DIRECT_TEMPLATES = (('index', 'search', 'tags', 'categories', 'archives',))
PAGINATED_TEMPLATES = {'index':None,'tag':None,'category':None,'author':None,'archives':24,}

# Site search plugin
SEARCH_MODE = "output"
SEARCH_HTML_SELECTOR = "main"
# Table of Content Plugin
TOC = {
    'TOC_HEADERS'       : '^h[1-3]', # What headers should be included in
                                     # the generated toc
                                     # Expected format is a regular expression
    'TOC_RUN'           : 'true',    # Default value for toc generation,
                                     # if it does not evaluate
                                     # to 'true' no toc will be generated
    'TOC_INCLUDE_TITLE': 'false',    # If 'true' include title in toc
}

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None
# RSS_FEED_SUMMARY_ONLY = True

# Social widgets
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/company/columbus-classical-academy'),
    ('facebook', 'https://m.facebook.com/Columbus-Classical-Academy-104983085549840/'),
)

# Article share widgets
SHARE = (
    ("twitter", "https://twitter.com/intent/tweet/?text=Features&amp;url="),
    ("linkedin", "https://www.linkedin.com/sharing/share-offsite/?url="),
    ("facebook", "https://facebook.com/sharer/sharer.php?u="),
)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# DISQUS_SITENAME = ''
# GOOGLE_ANALYTICS = ''
