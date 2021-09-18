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
def index(request):
	student = request.user.student
	context = {"student": student}
	return render(request, "courses/index.html", context)
	
	



@login_required(login_url='courses:login')
@admin_only
def course(request, pk_test):
    course = Course.objects.get(id=pk_test)
    students = Student.objects.all()

    context = {"course": course, "students": students}
    return render(request, "courses/course.html", context)


@login_required(login_url='courses:login')
@allowed_users(allowed_roles=['student'])
def registration(request): # , student_id
    my_course = request.user.student.enroll_set.all()
    all_course = Course.objects.all()
    # print(my_course)
    # for
    mycourse_count = my_course.count() # เด็กลงไปกี่วิชา
    context = {"courses": my_course, "mycourse_count": mycourse_count, "all_c": all_course}
    return render(request, "courses/registration.html", context)


@login_required(login_url='courses:login')   #กำลังลอง
@allowed_users(allowed_roles=['student'])
def courses(request):
    my_course = request.user.student.enroll_set.all()
    list_of_ids = []
    for en_c in my_course:
        list_of_ids.append(en_c.course.c_code)
    courses = Course.objects.exclude(c_code__in=list_of_ids)
    # print(list_of_ids)
    print(my_course)
    # print(courses)

    context = {"courses": courses}
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


@login_required(login_url='courses:login')   #กำลังลอง
@allowed_users(allowed_roles=['student'])
def deleteCourse(request, pk):
	enroll = Enroll.objects.get(id=pk)
	if request.method == "POST":
		enroll.delete()
		return redirect('courses:registration')

	return redirect('courses:registration')


@login_required(login_url='courses:login')
@allowed_users(allowed_roles=['student'])
def enrollCourse(request ,pk):
	course = Course.objects.get(id=pk)
	student = Student.objects.get(user=request.user)
	if request.method == 'POST':
	    enroll = Enroll.objects.create(student=student, course=course)
	    return redirect('courses:registration')

	return redirect('courses:courses')

@login_required(login_url='courses:login')
@allowed_users(allowed_roles=['student'])
def profile(request):
	student =  request.user.student

	context = {"student":student}
	return render(request, "courses/profile.html" ,context)