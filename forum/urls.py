from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.fhome, name="forum-homepage"),
	path('question/', views.question, name="forum-question"),
]