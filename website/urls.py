from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from website.views import http_test,json_test
def home(request):
    return HttpResponse("سلام 👋 این اولین صفحه من است")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]

from django.contrib import admin
from django.urls import path
from blog import views
from blog.views import http_test,json_test
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('https-test',http_test),
    path('json-test',json_test),
    path('contact',contact_view),
    path('about',about_view),
    path('index', index_view),
   
]
    
