from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from .decorators import unauthenticated_user, allowed_users, admin_only
from .models import *

@login_required(login_url='courses:login')
@allowed_users(allowed_roles=['student', 'admin']) # ล็อคให้คนบทบาทstudentเท่านั้น
def index(request): #เดี๋ยวเปลี่ยน
    context = {"courses": Course.objects.all()}
    return render(request, "courses/index.html", context)


@login_required(login_url='courses:login')
@admin_only
def course(request, pk_test):
    course = Course.objects.get(id=pk_test)
    return render(request, "courses/course.html", {"course": course})


@login_required(login_url='courses:login')
@allowed_users(allowed_roles=['student'])  #กำลังลอง
def registration(request): # , student_id
    my_course = request.user.student.enroll_set.all()
    all_course = Course.objects.all()
    # print(my_course)
    # for 
    mycourse_count = my_course.count() # เด็กลงไปกี่วิชา
    context = {"courses": my_course, "mycourse_count": mycourse_count, "all_c": all_course}
    return render(request, "courses/registration.html", context)


@login_required(login_url='courses:login')
def courses(request):
    context = {"courses": Course.objects.all()}
    return render(request, "courses/courses.html", context)


@login_required(login_url='courses:login')
@admin_only
def admincourses(request):
    context = {"courses": Course.objects.all()}
    return render(request, "courses/admincourses.html", context)


@unauthenticated_user
def loginPage(request):
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('courses:index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'courses/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('courses:login')