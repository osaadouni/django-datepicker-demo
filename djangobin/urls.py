from django.urls import path, re_path
from . import views

app_name='djangobin'

urlpatterns = [
    re_path(r'^time/$', views.today_is, name='time' ),
    path('', views.index, name='index'),
    re_path(r'^user/(?P<username>[A-Za-z0-9]+)/$', views.profile, name="profile"),
    re_path(r'^trending/$', views.trending_snippets, name='trending_snippets'),
    re_path(r'^trending/(?P<language_slug>[\w]+)/$', views.trending_snippets, name='trending_snippets'),
    re_path(r'^(?P<snippet_slug>[\d]+)/$', views.snippet_detail, name='snippet_detail'),
    re_path(r'^tag/(?P<tag>[\w-]+)/$', views.tag_list, name='tag_list'),
    re_path(r'^author/(?P<author_id>[\d]+)/$', views.author_detail, name='author_detail'),

    re_path(r'^books/$', views.book_category, name='book_category'),
    re_path(r'^books/(?P<category>[\w-]+)/$', views.book_category, name='book_category'),
    re_path(r'^extra/$', views.extra_args, name='extra_args'),


]