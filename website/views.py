from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages
from .forms import signup

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def login_user(request):
    #if the user logged in 
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        # the authentication
        user = authenticate(request,username = name,password=password )
        if user is not None:
            login(request,user)
            messages.success(request,"you've logged in " )
            return redirect('home')
        else:
            messages.success(request, "there was an error logging in")   
            return redirect('login')

    else:
        return render(request, 'login.html',{} )

def logout_user(request):
   logout(request)
   messages.success(request,"You Have Been Loged Out . . . ")
   return render(request, 'logout.html',{} )

def register(request):
    if request.method == 'POST':
        form = signup(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,"you've been registered ... welcome " )
            return redirect('home')
        else:
            return redirect('register')

    else:
        form=signup()
        return render(request, 'register.html',{'form':form} )