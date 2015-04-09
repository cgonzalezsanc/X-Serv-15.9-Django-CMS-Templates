from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/logout/&', "django.contrib.auth.views.logout"),
    url(r'^annotated/css/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_URL
        }),
    url(r'^annotated/(.*)$', "cms_templates.views.show_annotated"),
    url(r'^(.*)$', "cms_templates.views.show"),
)
