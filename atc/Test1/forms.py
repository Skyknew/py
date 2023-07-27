
#user registration

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#user Login

from django.contrib.auth.forms import AuthenticationForm

from django.forms.widgets import PasswordInput, TextInput

from django import forms


class CreateUSerForm(UserCreationForm):

    class Meta:

        model = User
        fields = {'username', 'email', 'password1', 'password2' }


#Login Users

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

    
#Profile-Management Update

class UpdateUserForm(forms.ModelForm):

    password = None

    class Meta:

        model = User

        fields = ['username', 'email']
        exclude = ['password1', 'password2']