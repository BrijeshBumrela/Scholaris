from django.urls import path, include
from . import views

app_name = 'exam'

urlpatterns = [
    path('', views.index, name='index'),
    path('design/',views.design, name='design'),
    path('exam-main/',views.exam, name="exam-main"),
    path('result/<int:id>/', views.result, name='result'),
    path('error/', views.exam_error, name='error'),
    path('list_all_test/', views.list_all_test, name='list_all_test'),
    path('my_test/', views.my_test, name='my_test'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('test_detail/<int:id>/', views.testdetail, name='testdetail'),
    path('edit_test/<int:id>/', views.edit_test, name='edit_test'),
    path('edit_question/<int:id>/', views.edit_question, name='edit_question')
]
