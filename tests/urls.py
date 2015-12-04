from __future__ import unicode_literals

from django.conf.urls import patterns, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import SimpleSessionView

admin.autodiscover()


urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    (r'^session/', SimpleSessionView.as_view()),
)

urlpatterns += staticfiles_urlpatterns()
