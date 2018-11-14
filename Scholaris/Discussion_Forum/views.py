from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from datetime import datetime
from .models import Post
from .forms import PostCreateForm


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

def post_create(request):

    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PostCreateForm()

    context = {
        'form': form,
    }
    return render(request, 'Discussion_Forum/post_create.html', context)