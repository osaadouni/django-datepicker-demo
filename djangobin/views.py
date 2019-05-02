import datetime
from django.shortcuts import HttpResponse, render_to_response, render
from django import template
from django.conf import settings


# Create your views here.
def index(request):
    return HttpResponse('<p>Hello Django</p>')

def old_today_is(request):
    now = datetime.datetime.now()
    t = template.Template('<html><body>Current date and time: {{ now }}</body></html>')
    c = template.Context({'now': now})
    html = t.render(c)
    return HttpResponse(html)

def old_2today_is(request):
    now = datetime.datetime.now()
    t = template.loader.get_template('djangobin/datetime.html')
    html = t.render({'now': now})
    return HttpResponse(html)

def today_is(request):
    now = datetime.datetime.now()
    #return render_to_response('djangobin/datetime.html', {'now': now})
    return render(request, 'djangobin/datetime.html', {'now': now, 'base_dir': settings.BASE_DIR})


def profile(request, username):
    print("request.path: {}".format(request.path))
    return HttpResponse("<p>Profile page of user #{}</p>".format(username))

def book_category(request, category='sci-fi'):
    return HttpResponse('<p>Books in {} category</p>'.format(category))

def extra_args(request, arg1=None, arg2=None):
    return HttpResponse('<p>arg1: {} <br> arg2: {} </p>'.format(arg1, arg2))