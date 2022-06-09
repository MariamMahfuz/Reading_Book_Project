from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import *

class ProfileForm(ModelForm):
    class Meta:
        model = Writer
        fields = ['user','writer_name','book_title']

class UserForm(ModelForm):
    class Meta:
        model=User_list
        fields=['name','address','photo','message']