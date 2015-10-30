from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^user/', include('registration.backends.simple.urls')),
    url(r'^user/', include('django.contrib.auth.urls')),
    url(r'^candidates/$', Candidate.as_view(), name='candidates'),
    url(r'^question/create/$', QuestionCreateView.as_view(), name='question_create'),
)