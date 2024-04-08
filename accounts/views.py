from django.shortcuts import render, redirect
from django.http import HttpResponse
#from.forms import UserRegisterForm , UserLoginForm
from.forms import *
from.models import profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
# Create your views here.
def user_register(request):
    #return render(request,'accounts/register.html')
    if request.method == 'POST' :
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            data= form.cleaned_data
            User.objects.create_user(username=data['user_name'], email=data['email'],first_name=data['first_name'],last_name=data['last_name'], password=data['password_2'])
            messages.success(request, 'با موفقیت ثبت نام شدید','info')
            messages.success(request, 'وارد شوید','dark')
            return redirect('accounts:user_login')
    else:
        form = UserRegisterForm()
    context ={'form' : form}
    return render(request, 'accounts/register.html', context)


def user_login(request):
    if request.method == 'POST' :
        form= UserLoginForm(request.POST)
        if form.is_valid():
            data= form.cleaned_data
            try:
                User=authenticate(request, username=User.objects.get(email=data['user']), password=data['password'])
            except:
                User=authenticate(request, username=data['user'], password=data['password'])

            if User is not None :
                login(request, User)
                messages.success(request, 'با موفقیت وارد شدید' ,'primary')
                return redirect('home:home')
            else:
                messages.success(request, 'کاربری یا پسورد اشتباه است' ,'danger') 
            
    else:
        form = UserLoginForm()
    
    return render (request, 'accounts/login.html' , {'form':form})


def user_logout(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید','dark')
    return redirect('home:home')
#return redirect('accounts:user_register')

def user_profile(request):
    # user = User.objects.get(pk=request.user.id)
    profile = profile.objects.filter(profile__user=request.user)
    #print(request.user.id)
    return render (request,'accounts/profile.html' , {'profile',profile})