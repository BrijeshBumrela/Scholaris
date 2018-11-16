from django.urls import path, re_path
from . import views

app_name = 'forum'

urlpatterns = [

    re_path('(?P<id>\d+)/post_edit/$',views.post_edit, name="post_edit"),
    path('', views.post_list, name="forum-post-list"),
    re_path('^question/(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.question, name="forum-question"),
    path('post_create/', views.post_create, name="post_create"),
    path('like/', views.upvote_post, name="upvote_post"),

]