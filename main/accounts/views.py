from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(response):
    return render(response, "home/index.html")


def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        
        user=auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.danger(request,'Invalid Credentials')
            return redirect('login')
    else:
        if request.user.is_authenticated == True:
            return redirect('index')
        return render(request,'accounts/login.html')


def register(response):
    if response.method=="POST":
        form = RegisterForm(response.POST)
        first_name=response.POST['first_name']
        last_name=response.POST['last_name']
        username=response.POST['email']
        password1=response.POST['password1']
        password2=response.POST['password2']
        email=response.POST['email']
        if User.objects.filter(email=email).exists():
                  messages.danger(response,'Email Already Exists')
                  return redirect('register')
        elif password1!=password2:  
                messages.danger(response,'Passwords do not match')
                return redirect('register')
        elif form.is_valid():
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.success(response,'Account created Successfully')
                print(messages)
                return redirect("login")
    else:
        if response.user.is_authenticated == True:
            return redirect('index')
        form = RegisterForm()
        return render(response, "accounts/register.html", {"form":form})


def logout(request):
    auth.logout(request)
    return redirect("login")    

@login_required
def user_selection(response):
    return redirect("info")  