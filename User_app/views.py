from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
def user_list(request):
    users=User_list.objects.all()
    context={
        'users':users,
    }
    return render(request,'User/user.html',context)

def user_Profile(request,primarykey):
    user_details=User_list.objects.get(pk=primarykey)   
    writers=Writer.objects.all()
    for i in writers:
        if i.user.id == primarykey:
            writer_list=i
            print(writer_list)
    context={
        'user_details':user_details,
        'writer_list':writer_list
    }
    return render(request,'User/profile.html',context)

@login_required
def Edit_User(request,primarykey):
    user_details=User_list.objects.get(pk=primarykey)   
    edit_user_form =  UserForm(instance=user_details)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user_details)
        if form.is_valid():
            form.save()
            
    context={
        'edit_user_form':edit_user_form,
    }
    return render(request,'User/edit_user.html',context)

@login_required
def Add_User(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User has been listed")
            return redirect('/')
   
    context={
        'form':form
    }
    return render(request,'User/add_user.html',context)

@login_required
def Delete_profile(request, primarykey):
    user_details=User_list.objects.get(pk=primarykey).delete()
    context = {
        'user_details' : user_details
    }
    return redirect('/',context)

