from django.urls import path, include

from django.contrib.auth import views as auth_views
from . import views


app_name = 'result'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'next_page': 'result:index'} , name='logout'),
    path('register/', views.register, name='register'),
    path('student_register/', views.student_register, name='student_register'),
    path('teacher_register/', views.teacher_register, name='teacher_register'),
    path('choose_course/', views.choose_course, name='choose_course'),
    path('course/',views.course, name='course'),
    path('set_course_teacher/', views.set_course_teacher, name='set_course_teacher'),
    path('student_list_teacher/', views.student_list_teacher, name='student_list_teacher')
]
