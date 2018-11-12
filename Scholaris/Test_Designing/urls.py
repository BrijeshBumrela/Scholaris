from django.urls import path, include
from . import views

app_name = 'exam'

urlpatterns = [
    path('', views.index, name='index'),
    path('design/',views.design, name='design'),
    path('error/', views.exam_error, name='error'),
    path('list_all_test/', views.list_all_test, name='list_all_test')

]