from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    password1 = forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':"form-control"}))
    password2 = forms.CharField(label="confirm password",widget=forms.PasswordInput(attrs={'class':"form-control"}))

    class Meta:
        model = User
        fields =['username']

class LogInForm(AuthenticationForm):
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model =User
        fiedls=['username','password']