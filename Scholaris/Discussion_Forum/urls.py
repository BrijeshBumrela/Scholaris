from django.urls import path, re_path
from . import views

app_name = 'forum'

urlpatterns = [

    path('', views.post_list, name="forum-post-list"),
    re_path('^question/(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.question, name="forum-question"),
    path('post_create/', views.post_create, name="post_create"),
]