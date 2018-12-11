from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='api_post_list'),
    path('posts/<int:id>/', views.post_detail, name='api_post_detail'),
    path('result/', views.result, name='api_result'),
]
