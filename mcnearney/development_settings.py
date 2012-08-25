# Turn debugging on
DEBUG = True
COMPRESS = False
TEMPLATE_DEBUG = True
THUMBNAIL_DEBUG = True

# No cache
CACHE_BACKEND = 'dummy://'

# Compiled CSS
COMPILER_FORMATS = {
    '.sass': {
        'binary_path': 'sass',
        'arguments': '*.sass *.css'
    },
}

# URL for site
BASE_URL = 'http://127.0.0.1:8000'

# Needed to serve media from built-in server
ADMIN_MEDIA_PATH = 'c:/Program Files/Python 2.6/Lib/site-packages/django/contrib/admin/media/'