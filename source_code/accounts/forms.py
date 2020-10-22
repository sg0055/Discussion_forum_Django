from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from django.forms import ModelForm


class signupForm(UserCreationForm):
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'input'}))
	password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={'class': 'input'}))

	class Meta:
		model = User
		fields = ['username', 'email']
		widgets = {
            'username': forms.TextInput(attrs={'class': 'input', 'autofocus': True}),
            'email': forms.EmailInput(attrs={'class': 'input', 'required': True})
		}

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		exclude = ['user']
		widgets = {
            'Full_Name': forms.TextInput(attrs={'class': 'input','required': True}),
            'Phone': forms.TextInput(attrs={'class': 'input', 'required': True}),
			'profile_pic': forms.FileInput(attrs={'class': 'file', 'required': True})
		}