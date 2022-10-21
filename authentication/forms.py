from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from authentication.models import User

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form_input', 'placeholder':"Email"}))
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form_input', 'placeholder':"User name"}))

    class Meta:
        model = User
        fields = ['email', 'user_name']

class LoginForm(forms.Form):
    #username = forms.CharField(label='Email / Username')
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form_input' , 'placeholder':"Email"}))
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={'class':'form_input password' , 'placeholder':'Password'}))