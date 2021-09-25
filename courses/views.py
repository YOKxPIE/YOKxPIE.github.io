from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

from .decorators import *
from django.db.models import F
from .models import *

@login_required(login_url='courses:login')
@student_only
def index(request):
	student = request.user.student
	context = {"student": student}
	return render(request, "courses/index.html", context)


@login_required(login_url='courses:login')
@admin_only
def indexadmin(request):
	return render(request, "courses/indexadmin.html")


@login_required(login_url='courses:login')
@admin_only
def course(request, pk_test):
    course = Course.objects.get(id=pk_test)
    enroll = Enroll.objects.filter(course=course)
    list_of_ids = []
    for stu in enroll:
    	list_of_ids.append(stu.student.student_id)
    students = Student.objects.filter(student_id__in=list_of_ids)


    context = {"course": course, "students": students}
    return render(request, "courses/course.html", context)


@login_required(login_url='courses:login')
@student_only
def registration(request):
    my_course = request.user.student.enroll_set.all()
    all_course = Course.objects.all()

    mycourse_count = my_course.count()
    context = {"courses": my_course, "mycourse_count": mycourse_count, "all_c": all_course}
    return render(request, "courses/registration.html", context)


@login_required(login_url='courses:login')
@student_only
def courses(request):
    my_course = request.user.student.enroll_set.all()
    list_of_ids = []
    for en_c in my_course:
        list_of_ids.append(en_c.course.c_code)
    courses = Course.objects.exclude(c_code__in=list_of_ids)

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


@login_required(login_url='courses:login')
@student_only
def deleteCourse(request, pk):
	enroll = Enroll.objects.get(id=pk)
	name_course = enroll.course
	id_course = name_course.id
	if request.method == "POST":
		Course.objects.filter(id=id_course).update(count_stu=F('count_stu') - 1)
		enroll.delete()
		return redirect('courses:registration')




@login_required(login_url='courses:login')
@student_only
def enrollCourse(request ,pk):
	course = Course.objects.get(id=pk)
	student = Student.objects.get(user=request.user)
	if request.method == 'POST':
	    enroll = Enroll.objects.create(student=student, course=course)
	    Course.objects.filter(id=pk).update(count_stu=F('count_stu') + 1)
	    return redirect('courses:registration')

	return redirect('courses:courses')

@login_required(login_url='courses:login')
@student_only
def profile(request):
	student =  request.user.student

	context = {"student":student}
	return render(request, "courses/profile.html" ,context)