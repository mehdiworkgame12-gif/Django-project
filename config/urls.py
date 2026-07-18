from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap

from blog import views
from blog.views import http_test, json_test
from blog.sitemaps import StaticViewSitemap


sitemaps = {
    "static": StaticViewSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),

    # sitemap
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='sitemap'
    ),

    # صفحات
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('test/', views.test, name='test'),
    path('single/', views.blog_single, name='single'),

    # تست‌ها
    path('https-test/', http_test),
    path('json-test/', json_test),
]