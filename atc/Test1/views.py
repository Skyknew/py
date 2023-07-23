from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'index.html')

def register(request):

    return render(request, 'register.html')

def dashboard(request):

    return render(request, 'dashboard.html')

def my_login(request):

    return render(request, 'my-login.html')

def profile_management(request):

    return render(request, 'profile-management.html')