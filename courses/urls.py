from django.urls import path

from . import views

app_name="courses"
urlpatterns = [
    # ทำตามอาจารย์
    path('', views.index, name="index"),

    # ทดลอง
    # path('registration/', views.registration, name="registration"), # ถ้ารันน่าจะerrorเพราะยังไม่defในviews.py
    # path('courses/', views.courses, name="courses"), # ถ้ารันน่าจะerrorเพราะยังไม่defในviews.py

]