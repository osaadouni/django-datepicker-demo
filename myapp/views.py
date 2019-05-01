from django.shortcuts import render, HttpResponse
from django.http import (
    HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound,
    HttpResponseBadRequest, HttpResponseForbidden, HttpResponseServerError
)

from .forms import ToDoForm

# Create your views here.
def show_demo(request):
    form = ToDoForm()
    return render(request, 'myapp/my_template.html', {'form': form})


def handle_post(request):
    post_id = 1
    return HttpResponse("received argument: #{}".format(post_id))

def handle_blog(request, slug):
    return HttpResponse("received argument: #{}".format(slug))

def handle_archive(request, year, month, day):
    return HttpResponse("received argument: #{}-{}-{}".format(year, month, day))

def handle_user(request, username):
    return HttpResponse("received argument: #{}".format(username))

def book_category(request, category='sci-fi'):
    return HttpResponse('<p>Books in {} category</p>'.format(category))

def extra_args(request, arg1, arg2, foo):
    return HttpResponse('<p>arg1: {} <br> arg2: {}<br> foo: {} </p>'.format(arg1, arg2, foo))


def custom_response_plain(request):
    return HttpResponse('<p>Custom Response</p>', content_type='text/plain')

def custom_response_json(request):
    import json
    data = {'name': 'john', 'email': 'john.smith@example.com', 'age': 25}
    return HttpResponse(json.dumps(data), content_type='application/json')

def custom_response_404(request):
    return HttpResponse('<h1>HTTP 404 Page Not Found</h1>', status=404)

def custom_response_302(request):
    res = HttpResponse(status=302)
    res['location'] = 'http://example.com'
    return res

def custom_response(request):
    res = HttpResponse('some data')
    res['content-disposition'] = 'attachment; filename=file.txt'
    return res


def tem_redirect(request):
    return HttpResponseRedirect('http://example.com')

def perm_redirect(request):
    return HttpResponsePermanentRedirect('http://example.com')

def not_found(request):
    return HttpResponseNotFound('Not Found')

def forbidden(request):
    return HttpResponseForbidden('Request Forbidden - 403')

def bad_request(request):
    return HttpResponseBadRequest('Bad Request - 400')

def server_error(request):
    return HttpResponseServerError('Internal Server Error - 500')

