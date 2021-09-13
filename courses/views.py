from django.shortcuts import render

# Create your views here.

from .models import Course

def index(request): #เดี๋ยวเปลี่ยน
    context = {"courses": Course.objects.all()}
    return render(request, "courses/index.html", context)


def course(request, c_code):
    course = Course.objects.get(pk=c_code)
    return render(request, "courses/course.html", {
        "course": course
    })

# ทดลอง
def registration(request):
    # context = {}
    return render(request, "courses/registration.html")#, context)


def courses(request):
    context = {"courses": Course.objects.all()}
    return render(request, "courses/courses.html", context)
