from django.conf.urls import url, include
from libraryapi import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^author/$', views.AuthorList.as_view()),
    url(r'^author/(?P<pk>[0-9]+)/$', views.AuthorDetails.as_view()),
    url(r'^work/$', views.WorkList.as_view()),
    url(r'^work/(?P<pk>[0-9]+)/$', views.WorkDetails.as_view()),
    url(r'^tag/$', views.TagList.as_view()),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
