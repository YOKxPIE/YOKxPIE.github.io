from django.db import models
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
<<<<<<< HEAD
        return f"This course is {self.c_code}"

#class Take(models.Model):
    #t_code = models.ForeignKey(Course, on_delete=models.CASCADE)
    #t_semester = models.ForeignKey(Course, on_delete=models.CASCADE)
    #t_year = models.ForeignKey(Course, on_delete=models.CASCADE)
    #students = models.ManyToManyField(User, blank=True)
    
    #def __str__(self):
        #return f"{self.id} {self.students}: {self.t_code} {self.t_semester} {self.t_year}"
=======
        return f"{self.c_code} {self.semester}/{self.a_year}"


>>>>>>> 4b112a4187b032ba2a9f9b027915ce2aeb8d7b15
