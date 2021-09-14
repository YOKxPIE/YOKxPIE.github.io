from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

# Create your views here.

from .models import *


#login users ไมได้อาจเพราะสร้างappแยกแต่เข้าผ่าน/users
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    else:
        return render(request, "courses/index.html", {
            "courses": Course.objects.all()
        })
    

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
        else:
            messages.warning(request, "Invalid credential.")
            return render(request, "users/login.html", {
                "messages": messages.get_messages(request)
            })
    return render(request, "users/login.html")
    
def logout_view(request):
    logout(request)
    
    return HttpResponseRedirect(reverse("users:login"))


