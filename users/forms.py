from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model=User
        #when we save the form it makes changes to the Users database
        fields=['username','email','password1','password2']
