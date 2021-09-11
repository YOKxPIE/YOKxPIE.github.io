from django.db import models

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
        return f"This course is {self.c_code}"

    