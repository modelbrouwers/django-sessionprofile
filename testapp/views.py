from django.http import HttpResponse


def simple_session_view(request):
    request.session['foo'] = 'bar'
    return HttpResponse('ok')
