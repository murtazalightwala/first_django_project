from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *


# Create your views here.

def index(request):
    return render(request,'home.html')

def log_in(request):
    user = authenticate(request,username = request.POST.get('username'),password = request.POST.get('password'))
    if user:
        login(request, user)
        return landing(request, user)
    else:
        return index(request)

def landing(request, user):
    
    u = False

    try:
        u = Staff.objects.get(user = user)
        return redirect('staff/')
    except:
      pass
    try:
        u = Teacher.objects.get(user = user)
        return redirect('teacher/')
    except:
      pass
    try:
        u = Student.objects.get(user = user)
        return redirect('student/')
    except:
      pass
    
    
    return render(request,'landing.html',{'user':u})

def log_out(request):
    logout(request)
    return index(request)

