from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CreateNewUser(UserCreationForm):
    email=forms.EmailField(required=True,label="",
    widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username=forms.CharField(required=True,label="",
    widget=forms.TextInput(attrs={'placeholder':'username'}))
    password1=forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder':'password'})
    )
    password2=forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder':'password'})
    )
    class Meta:
        model=User
        fields=('email','username','password1','password2')