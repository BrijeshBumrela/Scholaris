from django.urls import path, include
from . import views

app_name = 'exam'

urlpatterns = [
    path('', views.index, name='index'),
    path('design/',views.design, name='design'),
    path('exam-main/',views.exam,name="exam-main"),
    path('result/',views.result,name="exam-result"),
    path('exam-form/',views.exam_form,name="exam-form"),
]