from django.urls import path

from . import views

app_name="courses"
urlpatterns = [
    path('login/', views.login, name="loginPage"),
   # path('courses/', views.course, name="courses"),
    path('', views.index, name="index")
]