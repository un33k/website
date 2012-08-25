import os
import django

ADMINS = (
	('Lance McNearney', 'lance@mcnearney.net'),
)

MANAGERS = ADMINS

# Key
SECRET_KEY = 'secret_key_goes_here'

# SMTP
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'email_username'
EMAIL_HOST_PASSWORD = 'email_password'
EMAIL_PORT = 587

# Database
DATABASE_ENGINE = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'database_name'             # Or path to database file if using sqlite3.
DATABASE_USER = 'database_user'             # Not used with sqlite3.
DATABASE_PASSWORD = 'database_password'         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Time and locale
TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
USE_I18N = True

# Overrides the form used for comments
COMMENTS_APP = 'comments'

# Absolute path to the project directory
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# URL that handles the media served from MEDIA_ROOT
MEDIA_URL = '/media/'
MEDIA_ROOT = '%s/media/' % os.path.dirname(BASE_PATH)

# URL prefix for admin media -- CSS, JavaScript and images.
ADMIN_MEDIA_PREFIX = "%sadmin/" % MEDIA_URL

TEMPLATE_DIRS = (
	'%s/templates' % BASE_PATH
)

# Generated thumbnails
THUMBNAIL_SUBDIR = 'generated'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.cache.UpdateCacheMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
	'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.comments',
	'django.contrib.contenttypes',
	'django.contrib.markup',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.flatpages',
	'sorl.thumbnail',
	'blog',
	'blog.templatetags',
	'portfolio',
	'comments',
	'customtags',
	'compressor',
)

# Import local settings (if available)
try:
    from local_settings import *
except ImportError:
    pass