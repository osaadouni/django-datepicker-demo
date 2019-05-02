from django.urls import path, re_path
from . import views


app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^post/\d+/$', views.handle_post, name='myapp-post' ),
    re_path(r'^blog/(?P<slug>[\w-]+)/$', views.handle_blog, name='myapp-blog' ),
    re_path(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', views.handle_archive, name='myapp-archive'),
    re_path(r'^user/(?P<username>[\w.@+-]+)/$', views.handle_user, name="myapp-user"),

    re_path(r'^books/$', views.book_category, name='book_category'),
    re_path(r'^books/(?P<category>[\w-]+)/$', views.book_category, name='book_category'),

    re_path(r'^extra/$', views.extra_args, {'arg1': 1, 'arg2': (10, 20, 30), 'foo': 'bar'}, name='extra_args'),
    re_path(r'^custom/$', views.custom_response,  name='custom_response'),
]
