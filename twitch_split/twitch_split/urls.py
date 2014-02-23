from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from splitter import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twitch_split.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(\w+)$', views.one_full, name="one_full"),
    url(r'^(\w+)/(\w+)$', views.two_horiz, name="two_horiz"),
)

# For Development ONLY. Remove when in production...
urlpatterns += staticfiles_urlpatterns()