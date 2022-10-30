from django.http import HttpRequest
from django.http.response import HttpResponseBase

from sessionprofile.backends import get_backend


class SessionProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.store = get_backend()()

    def __call__(self, request: HttpRequest) -> HttpResponseBase:
        response = self.get_response(request)
        if hasattr(request, "session"):
            self.store.save_session(request)
        return response
