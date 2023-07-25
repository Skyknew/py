from django.shortcuts import render, redirect

# Create your views here.

from . forms import CreateUSerForm

from . models import Profile

def index(request):

    return render(request, 'test1/index.html')



def register(request):

    form = CreateUSerForm()

    if request.method == 'POST':

        form = CreateUSerForm(request.POST)

        if form.is_valid():

            current_user = form.save(commit=False)


            form.save()

            profile = Profile.objects.create(user=current_user)


            return redirect("my-login")
        

    context = { 'form': form }


    return render(request, 'test1/register.html', context=context)







def dashboard(request):

    return render(request, 'test1/dashboard.html')

def my_login(request):

    return render(request, 'test1/my-login.html')

def profile_management(request):

    return render(request, 'test1/profile-management.html')