from django.contrib.auth.forms import UserCreationForm
from .models import User, Name
from django.forms import ModelForm
from django import forms

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class NameForm(ModelForm):

    class Meta:
        model = Name
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'email', 'bio']




