from django.contrib import admin
from django.urls import path
from blog import views
from blog.views import http_test, json_test
from django.http import HttpResponse , JsonResponse
urlpatterns = [
    path('admin/', admin.site.urls),

    # صفحه اصلی
    path('', views.home, name='home'),

    # تست‌ها
    path('https-test/', http_test),
    path('json-test/', json_test),

    # صفحات HTML
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]
