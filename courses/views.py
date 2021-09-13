from django.shortcuts import render, redirect

# Create your views here.

from .models import *

def index(request): #เดี๋ยวเปลี่ยน
    context = {"courses": Course.objects.all()}
    return render(request, "courses/index.html", context)


def course(request, pk_test):
    course = Course.objects.get(id=pk_test)
    return render(request, "courses/course.html", {"course": course})


def registration(request, student_id):
    my_course = Course.objects.get(id=student_id)
    mycourse_count = my_course.count() # เด็กลงไปกี่วิชา
    context = {"course": my_course, "mycourse_count": mycourse_count}
    return render(request, "courses/registration.html", context)


def courses(request):
    context = {"courses": Course.objects.all()}
    return render(request, "courses/courses.html", context)


def admincourses(request):
    context = {"courses": Course.objects.all()}
    return render(request, "courses/admincourses.html", context)

