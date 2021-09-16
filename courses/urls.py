from django.urls import path

from . import views

app_name="courses"
urlpatterns = [
    # ทำตามอาจารย์
    path('', views.index, name="index"),


    path('registration/', views.registration, name="registration"),
    path('courses/', views.courses, name="courses"),
    path('admincourses/', views.admincourses, name="admincourses"),
    path('course/<str:pk_test>/', views.course, name="acourse"),
    
    path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	
	
	path('delete_course/<str:pk>/', views.deleteCourse, name="delete_course"),

]