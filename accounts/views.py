from django.shortcuts import render

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        msg='user is already logged in'
    else:
        msg=None
    return render(request,'accounts/login.html', {'msg': msg})

def logout_view(request):
    return render(request,'accounts/logout.html')

def singup_view(request):
    return render(request,'accounts/singup.html')