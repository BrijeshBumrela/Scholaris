from django.urls import path, include

from django.contrib.auth import views as auth_views
from . import views


app_name = 'result'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': 'result:index'} , name='logout'),
    path('register/', views.register, name='register'),
    path('student_register/', views.student_register, name='student_register'),
    path('teacher_register/', views.teacher_register, name='teacher_register'),
    path('choose_course_teacher/', views.choose_course_teacher, name='choose_course_teacher'),
    path('set_course_teacher/', views.set_course_teacher, name='set_course_teacher'),
    path('list_all_students/', views.list_all_students, name='list_all_students'),
    path('follow/', views.follow, name='follow'),
    path('list_all_teachers_to_follow/', views.list_all_teachers_to_follow, name='list_all_teachers_to_follow')
]
