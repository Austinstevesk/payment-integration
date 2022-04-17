from pyexpat import model
from django import forms
from django.contrib.auth.forms import  UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'full_name', 'account_name', 'password1', 'password2')
        