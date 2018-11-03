from django.urls import path, include
from . import views

app_name = 'exam'

urlpatterns = [
    path('', views.index, name='index'),
    path('design/',views.design, name='design'),

]