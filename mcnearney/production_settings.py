# Live URL
BASE_URL = 'http://www.mcnearney.net'
SITE_ID = 1

# Compress css/js
COMPRESS = True

# Compiled CSS
COMPILER_FORMATS = {
    '.sass': {
        'binary_path': '/var/lib/gems/1.8/bin/sass',
        'arguments': '*.sass *.css'
    },
}

# Cache
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CACHE_MIDDLEWARE_SECONDS = 60 * 60
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True