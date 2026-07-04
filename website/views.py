from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def http_test(request):
    return HttpResponse('<h1>this is a test</h1>')

def json_test(request):
    return JsonResponse({'name': 'mehdi'})

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return HttpResponse('<h1>About page</h1>')

def contact_view(request):
    return HttpResponse('<h1>contact page</h1>')
def contact_view(request):
    return render(request,'contact.html')
