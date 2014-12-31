#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os 

AUTHOR = 'Dylan Gregersen'
SITENAME = AUTHOR 
SITESUBTITLE = '"You are something the whole Universe is doing, the same way a wave is something the whole ocean is doing" ― Alan W. Watts'
SITEURL = ''
TIMEZONE = 'US/Mountain'
DEFAULT_LANG = 'en'

WHOAMI_IMAGE = "static/img/avatar.jpg"
WHOAMI_TEXT = """
<ul class="whoami">
    <li>Astronomer,</li>
    <li>Python Programmer,</li>
    <li>Data Scientist,</li>
    <li>Musician,</li>
    <li>Vegan</li>    
</ul>
"""

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS =  (\
#     ('Pelican', 'http://getpelican.com/'),
#     ('Python.org', 'http://python.org/'),
#     ('Jinja2', 'http://jinja.pocoo.org/'),
#     )

GITHUB_URL = 'http://github.com/astrodsg'

# Social widget
SOCIAL = (\
    ('twitter', 'http://twitter.com/astrdsg'),
    #('linkedin', 'http://www.linkedin.com/in/XXXXXXX'),
    ('github', GITHUB_URL),
    )

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 100
TYPOGRIFY = False

SIDEBAR_IMAGE = "static/img/avatar.jpg"
SIDEBAR_IMAGE_ALT = 'dsg'
SIDEBAR_IMAGE_WIDTH = 300

#FAVICON = 'images/favicon.png'

#PLUGIN_PATHS = 'pelican-plugins'
#PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
#           'liquid_tags.youtube', 'liquid_tags.include_code']
PLUGIN_PATHS = ["plugins"]
PLUGINS = [\
    'tag_cloud',
    'page_content',
    'pandoc_reader',    
    'named_pages',
    "multi_neighbors",
    ]

MULTI_NEIGHBORS = 3 # number to each side of current


_pandoc_filter = os.path.join(os.path.dirname(__file__),"plugins/pandoc_reader","highlighter_pygments_filter.py")
PANDOC_ARGS = [\
    #'--filter={}'.format(_pandoc_filter),
    "--mathjax",
    '--smart',
    '--toc',
    '--toc-depth=2',
    '--highlight-style=pygments',
]

PANDOC_EXTENSIONS = [\
    '+grid_tables',
    '+raw_html',
    '+markdown_in_html_blocks',
    ]

# below is the dir for the 'include_code' plugin
# CODE_DIR = 'files'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# --------------------------------------------------------------------------- #
# Paths 
PROJECT_ABSPATH = os.path.abspath(os.path.dirname(__file__))
projectp = lambda fn : os.path.join(PROJECT_ABSPATH,fn)

# ----------------------- 

OUTPUT_PATH = 'output'
PATH = 'content'

STATIC_PATHS = [\
    'README.md',
    'blog',
    'static/img',
    'static/css',
    'static/js',        
    'static/files',            
    ]

INCLUDE_CSS="static/css"
INCLUDE_JS="static/js"

# ----------------------- 

PAGE_PATHS = ['pages']
DIRECT_PAGE_TEMPLATES = 'pages/direct'
PAGE_EXCLUDES = [DIRECT_PAGE_TEMPLATES]

# ----------------------- 

ARTICLE_PATHS = ['blog']
ARTICLE_EXCLUDES = []
ARTICLE_URL = 'blog/{category}/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{category}/{date:%Y}/{date:%m}/{slug}.html' #'blog/{date:%Y}/{date:%Y}-{date:%m}-{date:%d}-{slug}'
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'misc'
SUMMARY_MAX_LENGTH = 80


# TAG_CLOUD_SORT_KEY = lambda item:item[0].name.lower() # sort alphabetically 
TAG_CLOUD_MAX_ITEMS = 10 # maximun number of items, truncates after sorting
TAG_CLOUD_SCALE_FXN = "lambda x,_:x" # scale the number associated with each tag 
# TAG_CLOUD_STEPS = 20 # if TAG_CLOUD_SCALE_FXN is none then uses a scaled value
# TAG_CLOUD_RANDOMIZE = False # randomize the tags as a final step

SIDEBAR_TITLE = "My Blog"

DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False 
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

NUMBER_ARTICLES_PER_PAGE = 10

# 

# --------------------------------------------------------------------------- #

THEME = "themes/pelican-boots"
#THEME = "notmyidea"
#THEME = "themes/waterspill-en"
#THEME = "themes/pelican-elegant"
#THEME = "themes/pelican-octopress-theme"
#THEME = "themes/journal"

THEME_STATIC_DIR = 'theme'
# TEMPLATE_PAGES = {\
#     'blog/index.html': 'blog/index.html',
#     }

EXTRA_TEMPLATES_PATHS = [\
    os.path.join(PROJECT_ABSPATH,PATH,DIRECT_PAGE_TEMPLATES),
    ]

DIRECT_TEMPLATES = [\
    # "name" -> `/name.html` unless NAME_SAVE_AS=
    "research", 
    "programming",
    "adventures",
    "contact",
    ]

MENUITEMS = (\
    ('Home', ''), 
    ('Blog', 'blog/index.html'),     
    ('Research', 'research.html'), 
    ('Programming', 'programming.html'), 
    #('Adventures', 'adventures.html'),     
    ('Contact', 'contact.html'),
    )

# Search box
SEARCH_BOX = True

RESEARCH_ARTICLES = [\
    'pages/direct/research/phat.md',    
    'pages/direct/research/hi_res.md',
    'pages/direct/research/astro_tools.md',  
    #'pages/direct/research/research_cv.md',
    ]

PROGRAMMING_ARTICLES = [\
    'pages/direct/programming/latbin.md',  
    'pages/direct/programming/thimbles.md',  
    'pages/direct/programming/dsgSPECTRE.md',  
    'pages/direct/programming/astropy.md',  
    ]

ADVENTURE_ARTICLES = [\
    ]

INCLUDE_ARTICLES =  RESEARCH_ARTICLES + PROGRAMMING_ARTICLES #+ ADVENTURE_ARTICLES


