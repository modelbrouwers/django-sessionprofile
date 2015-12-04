from django.http import HttpResponse
from django.views.generic import View


class SimpleSessionView(View):

    def get(self, request, *args, **kwargs):
        self.request.session['foo'] = 'bar'
        return HttpResponse('ok')
