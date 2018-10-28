from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'} , name='logout'),
    path('register/', views.register, name='register'),
    path('student_register/', views.student_register, name='student_register'),
    path('teacher_register/', views.teacher_register, name='teacher_register')
]
