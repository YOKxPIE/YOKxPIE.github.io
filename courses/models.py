from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    # course code ex.CN331
    c_code = models.CharField(max_length=5)
    # course name
    c_name = models.CharField(max_length=150)
    semester = models.IntegerField()
    # academic year
    a_year = models.IntegerField()
    # count student who enroll this course
    count_stu = models.IntegerField(default=0)
    # the maximum number of students
    max_stu = models.IntegerField()
    # Is this course open?  default = yes
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.c_code} {self.semester}/{self.a_year}"


class Student(models.Model):
    name = models.CharField(max_length=200)
    course = models.ManyToManyField(Course ,blank=True ,related_name="students")

    def __str__(self):
        return f"{self.id} : {self.name}"


class enroll(models.Model):
    #t_code = models.ForeignKey(Course, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    #t_semester = models.ForeignKey(Course, on_delete=models.CASCADE)
    #t_year = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} {self.students}: {self.course}"
