from multiprocessing import context
from multiprocessing.dummy import current_process
from urllib.request import Request
from django.shortcuts import render,HttpResponseRedirect
from App_Login.forms import *
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse,reverse_lazy
from App_Login.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method=='POST':
        form=CreateNewUser(data=request.POST)
        if form.is_valid():
            user=form.save()
            registered=True
            # user_profile=UserProfile(user=user)
            # user_profile.save()
            return HttpResponseRedirect(reverse('App_Login:login'))
    context={
        'title':'Signup',
        'form':form
    }

    return render(request,'App_Login/signup.html',context)

def login_user(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('User:user_list'))

    context={
        'title':login,
        'form':form
    }
    return render(request,'APP_Login/login.html',context)


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))