from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages
from .forms import signup
from .models import record 

# Create your views here.
def home(request):
    return render(request,'home.html',{})


def login_user(request):
    records = record.objects.all().order_by('id').values
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You've logged in.")
            return render(request, 'login.html', {'records':records})
        else:
            messages.error(request, "There was an error logging in.")
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {'records':records})

def logout_user(request):
   logout(request)
   messages.success(request,"You Have Been Loged Out . . . ")
   return render(request, 'home.html',{} )

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


def customer(request,pk):
    if request.user.is_authenticated:
        data =record.objects.get(id=pk)
        return render (request,'record.html',{'data':data}) 
    else:
        messages.success(request,'You Must Log In First ...')
        return render(request,'home.html',{})
    
def delete(request,pk):
    if request.user.is_authenticated:
        data =record.objects.get(id=pk)
        data.delete()
        messages.success(request,"Customer Deleted Successfully...")
        return render(request,'home.html',{})
    else:
        messages.success(request,'You Must Log In First ...')
        return render(request,'home.html',{})
