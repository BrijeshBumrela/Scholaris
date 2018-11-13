from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from datetime import datetime
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }

    return render(request, 'Discussion_Forum/post_view.html', context)

def question(request, id, slug):
    #user = User.objects.get(id=id)
    post = get_object_or_404(Post, id=id, slug=slug)
    context = {
        'post': post,
    }
    return render(request, "Discussion_Forum/question_view.html", context)