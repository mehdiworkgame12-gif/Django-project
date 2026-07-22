from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from blog import views
from blog.views import http_test, json_test
from blog.sitemaps import StaticViewSitemap
import debug_toolbar
from blog.feeds import LatestPostsFeed

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
    path('robots.txt',include('robots.urls')),
    path('__debug__/',include(debug_toolbar.urls)),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path("summernote/", include("django_summernote.urls")),
    path('captcha/', include('captcha.urls')),
    path('rss/feed/', LatestPostsFeed(),name='post_feeds'),

]