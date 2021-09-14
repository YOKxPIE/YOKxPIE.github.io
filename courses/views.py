from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import *


#login users ไมได้อาจเพราะสร้างappแยกแต่เข้าผ่าน/usersได้
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    else:
        return render(request, "index.html", {
            "courses": Course.objects.all()
        })

def course(request):
    return render(re)



