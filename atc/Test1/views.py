from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'test1/index.html')

def register(request):

    return render(request, 'test1/register.html')

def dashboard(request):

    return render(request, 'test1/dashboard.html')

def my_login(request):

    return render(request, 'test1/my-login.html')

def profile_management(request):

    return render(request, 'test1/profile-management.html')