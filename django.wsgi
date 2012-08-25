import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'mcnearney.settings'
sys.path.append('/srv/www/mcnearney.net')
sys.path.append('/srv/www/mcnearney.net/mcnearney')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()