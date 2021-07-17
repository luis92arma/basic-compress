from django.conf.urls import url
from views import index, get_all_blogs, get_blog_detail

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^all/?', get_all_blogs, name='get_all_blogs'),
    url(r'^detail/(?P<blog_id>\d+)/$', get_blog_detail, name='get_blog_detail')
]
