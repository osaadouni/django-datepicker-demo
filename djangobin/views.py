import datetime
from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('<p>Hello Django</p>')


def today_is(request):
    now = datetime.datetime.now()
    html = '<html><body>Current date and time: {0}</body></html>'.format(now)
    return HttpResponse(html)


def profile(request, username):
    print("request.path: {}".format(request.path))
    return HttpResponse("<p>Profile page of user #{}</p>".format(username))