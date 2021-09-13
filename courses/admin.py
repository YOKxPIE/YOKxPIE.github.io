from django.contrib import admin

# Register your models here.

from .models import *

class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ("course",)
    
admin.site.register(Course)
admin.site.register(Student ,StudentAdmin)
admin.site.register(enroll)