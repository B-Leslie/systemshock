__author__ = 'Simon Ruffle'

from django.conf.urls import patterns, include, url
from shockindexhome import BasicPage

urlpatterns = patterns('',
    url(r'^$', BasicPage.as_view()),

)

