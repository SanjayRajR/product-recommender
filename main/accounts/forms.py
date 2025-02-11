from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
        email = forms.EmailField()
        first_name = forms.CharField(label = "First Name", max_length=100)
        last_name = forms.CharField(label = "Last Name", max_length=100)
        class Meta:
            model = User
            fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
            