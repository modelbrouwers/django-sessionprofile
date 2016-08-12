from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import SimpleSessionView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^session/', SimpleSessionView.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
