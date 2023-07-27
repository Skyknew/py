from django.shortcuts import render, redirect

# Create your views here.

from . forms import CreateUSerForm, LoginForm, UpdateUserForm, UpdateProfileForm

from . models import Profile

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User



def index(request):

    return render(request, 'test1/index.html')


# for register
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



#for login
def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():
    
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")
            
    context = {'form': form }


    return render(request, 'test1/my-login.html', context=context)



#for user-logout
def user_logout(request):
    
    auth.logout(request)

    return redirect("")



#for dashboard
@login_required(login_url='my-login')
def dashboard(request):

    profile_pic = Profile.objects.get(user=request.user)

    context = {'profilePic': profile_pic}


    return render(request, 'test1/dashboard.html', context=context)


#for profile_management
@login_required(login_url='my-login')
def profile_management(request):

    user_form = UpdateUserForm(instance=request.user)

    profile = Profile.objects.get(user=request.user)

    profile_form = UpdateProfileForm(instance=profile)



    if request.method == 'POST':

        user_form = UpdateUserForm(request.POST, instance=request.user)

        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile )

        if user_form.is_valid():

            user_form.save()

            return redirect("dashboard")
        

        if profile_form.is_valid():
            
            profile_form.save()

            return redirect("dashboard")
        
    
    context = {'user_form': user_form, 'profile_form':profile_form }

    return render(request, 'test1/profile-management.html', context=context)


#for delete-account
@login_required(login_url='my-login')
def delete_account(request):

    if request.method == 'POST':

        deleteUser = User.objects.get(username=request.user)

        deleteUser.delete()

        return redirect("")
    
    return render(request, 'test1/delete-account.html')