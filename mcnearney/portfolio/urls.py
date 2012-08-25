from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('portfolio.views',
	(r'^$', 'index'),
	(r'^(?P<project_slug>.*?)/(?P<video_slug>.*)-video/$', 'video'),
	(r'^(?P<slug>.*)/$', 'detail'),
)