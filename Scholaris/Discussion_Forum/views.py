from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from .models import Post
from .forms import PostCreateForm


# Create your views here.
def post_list(request):
    posts = Post.published.all()
    query = request.GET.get('q')
    print(query)
    context = {
        'posts':posts,
    }

    return render(request, 'Discussion_Forum/post_view.html', context)

def question(request, id, slug):
    #user = User.objects.get(id=id)
    post = get_object_or_404(Post, id=id, slug=slug)
    is_upvoted = False
    if post.upvotes.filter(id=request.user.id).exists():
        is_upvoted = True
    context = {
        'post': post,
        'is_upvoted': is_upvoted,
        'total_upvotes': post.total_upvotes(),
    }
    return render(request, "Discussion_Forum/question_view.html", context)

def upvote_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    #is_upvoted = False
    if post.upvotes.filter(id=request.user.id).exists():
        post.upvotes.remove(request.user)
        is_upvoted = False
    else:
        post.upvotes.add(request.user)
        is_upvoted = True

    return HttpResponseRedirect(post.get_absolute_url())

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

class PostsView(ListView):
    model = Post
    paginate_by = 5
    context_object_name = 'posts'
    template_name = 'Discussion_Forum/post_view.html'

