from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse, JsonResponse
from blog.models import Post
# صفحه اصلی
def home(request):
    return HttpResponse("سلام 👋 این اولین صفحه من است")

# تست HTML
def http_test(request):
    return HttpResponse("<h1>This is a test</h1>")

# تست JSON
def json_test(request):
    return JsonResponse({"name": "mehdi"})

# صفحه index (HTML)
def index(request):
    return render(request, 'index.html')

# صفحه contact (HTML)
def contact(request):
    return render(request, 'contact.html')

def index(request):
    return render(request, "index.html", {
        "items": ["لپ‌تاپ", "موبایل", "موس"]
    })

def blog_view(request):
    return render (request,'blog/blog-home.html')
def blog_single(request):
    return render(request,'blog/blog-single.html')
def test(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render (request,'test.html',context)

