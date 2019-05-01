from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'^time/$', views.today_is, name='djangobin-time' ),
    #re_path(r'user/(?P<username>\w+)/$', views.profile, name="djangobin-profile"),
    re_path(r'user/(?P<username>[A-Za-z0-9]+)/$', views.profile, name="djangobin-profile"),
    path('', views.index, name='djangobin-index'),
]