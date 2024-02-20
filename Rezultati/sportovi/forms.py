from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = ['naziv']


class TimForm(forms.ModelForm):
    class Meta:
        model = Tim
        fields = ['naziv', 'sport']


class NatjecanjeForm(forms.ModelForm):
    class Meta:
        model = Natjecanje
        fields = ['naziv', 'sport', 'tim']


class RezultatUtakmiceForm(forms.ModelForm):
    class Meta:
        model = RezultatUtakmice
        fields = ['natjecanje', 'domacin', 'gost', 'rezultat_domacin', 'rezultat_gost']