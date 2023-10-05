# from django.contrib import messages, auth
# from django.contrib.auth.models import User
# from django.http import HttpResponseRedirect
# from django.shortcuts import render, redirect
# from django.urls import reverse
#
#
# def base(request):
#
#     return render(request, "base.html")
# def login(request):
#     if request.method=='POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('/')
#         else:
#             messages.info(request,"invalid credentials")
#             return redirect('login')
#     return render(request,"login.html")
# def register(request):
#     if request.method=='POST':
#         username = request.POST['username']
#         # first_name = request.POST['first_name']
#         # last_name = request.POST['last_name']
#         # email = request.POST['email']
#         password = request.POST['password']
#         cpassword=request.POST['password1']
#         if password==cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,"username taken")
#                 return render(request,'register.html')
#             # elif User.objects.filter(email=email).exists():
#             #     messages.info(request,"email taken")
#             #     return redirect('register')
#             else:
#                 user = User.objects.create_user(username=username,password=password)
#                 user.save()
#                 print("user created")
#                 return render(request,'login.html')
#                 # return HttpResponseRedirect(reverse('login'))
#         else:
#             messages.info(request,"password not matching")
#             return render(request,'register.html')
#     return render(request, "register.html")
# # def logout(request):
# #     auth.logout(request)
# #     return redirect('/')
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect




from django.shortcuts import render

# Create your views here.
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

from django.shortcuts import render
# app_name = 'bankapp'
from django import forms
# Create your views here.
def base(request):
    return render(request, 'base.html')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                print('user created')
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')

    return render(request,"register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('newpage')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def new(request):
    return render(request,'new.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def newpage(request):

    return render(request,'newpage.html')

def msg(request):
    return render(request, 'msg.html')
