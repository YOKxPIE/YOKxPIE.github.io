from django.shortcuts import render

# Create your views here.

from .models import Course

def index(request):
    return render(request, "courses/index.html", {
        "courses": Course.objects.all()
    })


def course(request, c_code):
    course = Course.objects.get(pk=c_code)
    return render(request, "courses/course.html", {
        "course": course
    })