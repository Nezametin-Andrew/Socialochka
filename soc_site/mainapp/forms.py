from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.db.models import fields
from .models import CustomUser
from mainapp import models


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
    

class RegistrationUserForm(UserCreationForm):
    
    username = forms.CharField(
        label="Логин :", widget=forms.TextInput(attrs={"class": "form-control", "id": "username"})
        )
    first_name = forms.CharField(
        label="Имя :", widget=forms.TextInput(attrs={"class": "form-control", "id": "first_name"})
        )
    last_name = forms.CharField(
        label="Фамилия :", widget=forms.TextInput(attrs={"class": "form-control", "id": "last_name"})
        )
    email = forms.CharField(
        label="E-mail :", widget=forms.EmailInput(attrs={"class": "form-control", "id": "email"})
        )
    password1 = forms.CharField(
        label="Пароль :", widget=forms.PasswordInput(attrs={"class": "form-control", "id": "password1"})
        )
    password2 = forms.CharField(
        label="Повторите пароль :", widget=forms.PasswordInput(attrs={"class": "form-control", "id": "password2"})
        )

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



class LoginUserForm(AuthenticationForm):

    username = forms.CharField(
        label="Логин :", widget=forms.TextInput(attrs={"class": "form-control", "id": "username"})
        )
    password1 = forms.CharField(
        label="Пароль :", widget=forms.PasswordInput(attrs={"class": "form-control", "id": "password1"})
        )

    class Meta:
        model = CustomUser
        fields = ('username', 'password1')
