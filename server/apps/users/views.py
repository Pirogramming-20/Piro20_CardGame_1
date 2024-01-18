from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

#def signup(request):
#    pass

#def logout(request):
#    pass

def login(request):
    return render(request, 'users/naver_login.html')

def naver_login_callback(request):
    return render(request, 'users/naver_callback.html')   