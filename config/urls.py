from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("سلام 👋 این اولین صفحه من است")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]

from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]