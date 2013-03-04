# -*- coding: utf-8 -*-
# ===============
# Basic settings
# ===============
AUTHOR = u'Yangjiandong'
DEFAULT_CATEGORY = 'blog'
SITENAME = u'yangjandong github blog'
SITEURL = 'http://yangjiandong.github.com/myblog'
SITE_URL = SITEURL
STATIC_PATHS = ['images', ]
TIMEZONE = 'Asia/Shanghai'#'Asia/Singapore'

#DATE_FORMATS = {
#    'en':('usa','%a, %d %b %Y'),
#    'zh':('chs','%Y-%m-%d, %a'),
#    'jp':('jpn','%Y/%m/%d (%a)'),
#}
# windows locale: http://msdn.microsoft.com/en-us/library/cdax410z%28VS.71%29.aspx
LOCALE = ['usa', 'chs', 'jpn',        # windows
          'en_US', 'zh_CN', 'ja_JP']  # Unix/Linux
DEFAULT_LANG = 'zh'

# =============
# URL settings
# =============
PERMALINK_STRUCTURE = '{date:%Y}/{date:%m}/'
ARTICLE_URL = '%s{slug}.html' % PERMALINK_STRUCTURE
ARTICLE_LANG_URL = '%s{slug}-{lang}.html' % PERMALINK_STRUCTURE
PAGE_URL = '%spages/{slug}.html' % PERMALINK_STRUCTURE
PAGE_LANG_URL = '%spages/{slug}-{lang}.html' % PERMALINK_STRUCTURE
ARTICLE_SAVE_AS = '%s{slug}.html' % PERMALINK_STRUCTURE
ARTICLE_LANG_SAVE_AS = '%s{slug}-{lang}.html' % PERMALINK_STRUCTURE
PAGE_SAVE_AS = '%spages/{slug}.html' % PERMALINK_STRUCTURE
PAGE_LANG_SAVE_AS = '%spages/{slug}-{lang}.html' % PERMALINK_STRUCTURE


# ===========
# Pagination
# ===========
WITH_PAGINATION = True
DEFAULT_PAGINATION = 10


# =================
# Ordering content
# =================
REVERSE_ARCHIVE_ORDER = True


# =================
# Theming
# =================
THEME = 'notmyidea'

DISQUS_SITENAME = 'martinbrochhauscom'
FLATTR = True
GITHUB_URL = 'http://github.com/yangjiandong/myblog'
GOOGLE_ANALYTICS = 'UA-1147761-33'
MENUITEMS = (
    ('Archives', '{0}/archives.html'.format(SITEURL)),
)
TWITTER_USERNAME = 'mbrochh'
