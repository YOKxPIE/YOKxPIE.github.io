from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    c_code = models.CharField(max_length=5)
    c_name = models.CharField(max_length=150, null = True)
    semester = models.IntegerField()
    a_year = models.IntegerField()
    count_stu = models.IntegerField(default=0)
    max_stu = models.PositiveIntegerField(default=3)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.c_code} {self.semester}/{self.a_year}"

    def is_seat_available(self):
        return self.count_stu < self.max_stu


class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=100, null = True)
    Last_name = models.CharField(max_length=100, null = True)
    email = models.CharField(max_length=200, null = True)
    student_id = models.CharField(max_length=10, null = True)

    def __str__(self):
        return f"{self.student_id}: {self.First_name} {self.Last_name}"


class Enroll(models.Model):
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f"{self.student} enroll {self.course}"