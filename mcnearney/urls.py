from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', 'views.home'),
	(r'^contact/$', 'views.contact'),
	(r'^contact/(?P<sent>\w+)/$', 'views.contact'),
	(r'^portfolio/', include('portfolio.urls')),
	(r'^blog/', include('blog.urls')),
	(r'^comments/', include('django.contrib.comments.urls')),
	(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^robots.txt$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'path': 'root/robots.txt'}),
		(r'^favicon.ico$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'path': 'img/mcnearney.ico'}),
		(r'^media/admin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_PATH}),
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	)