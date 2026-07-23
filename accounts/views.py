from django.shortcuts import render

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        msg = 'user is already logged in'
    else:
        msg = None

    return render(request, 'login.html', {'msg': msg})


def logout_view(request):
    return render(request, 'login.html')


def singup_view(request):
    return render(request, 'singup.html')