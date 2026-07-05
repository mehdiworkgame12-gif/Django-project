from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

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