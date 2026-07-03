from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.http import HttpResponse, JsonResponse

def home(request):
    return HttpResponse("سلام مهدی بنازم بهت")
def http_test(request):
    return HttpResponse('<h1> thi is a test </h1>')
def json_test(request):
    return JsonResponse({'name':'mehdi'})
def index_view(request):
    return HttpResponse('<h1>Home page</h1>')
def about_view(request):
    return HttpResponse('<h1>About page</h1>')
def contact_view(request):
    return HttpResponse('<h1>contact page</h1>')
