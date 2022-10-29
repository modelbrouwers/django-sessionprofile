from django.urls import path

from .views import simple_session_view

urlpatterns = [
    path("session/", simple_session_view),
]
