from django.urls import path, re_path
from . import views

app_name = 'forum'

urlpatterns = [

    re_path('(?P<id>\d+)/post_edit/$',views.post_edit, name="post_edit"),
    re_path('(?P<id>\d+)/post_delete/$', views.post_delete, name="post_delete"),
    path('', views.post_list, name="forum-post-list"),
    path('question/<int:id>/<str:slug>/', views.question, name="forum-question"),
    path('post_create/', views.post_create, name="post_create"),
    path('like/', views.upvote_post, name="upvote_post"),
    path('upvote/<int:id>/',views.upvote_comment, name="upvote_comment"),
    path('downvote/<int:id>/',views.downvote_comment, name="downvote_comment"),

]