from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.urls import urlpatterns as blog_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include(blog_urls))
)
