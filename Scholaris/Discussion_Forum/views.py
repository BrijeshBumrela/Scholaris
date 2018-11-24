from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from .models import *
from .forms import *
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
def post_list(request):
    posts = Post.published.all().order_by('-updated')
    query = request.GET.get('q')
    if query:
        posts = Post.published.filter(
            Q(title__icontains=query)|
            Q(author__username=query)|
            Q(body__icontains=query)
        )
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 5)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)

    context = {
        'posts':posts,
        'numbers': numbers,
    }

    return render(request, 'Discussion_Forum/post_view.html', context)

def question(request, id, slug):
    # user = User.objects.get(id=id)
    post = get_object_or_404(Post, id=id, slug=slug)
    comments = Comment.objects.filter(post=post).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(post=post, user=request.user, content=content, )
            comment.save()
            #return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm

    is_upvoted = False
    if post.upvotes.filter(id=request.user.id).exists():
        is_upvoted = True

    comment_id = 0
    is_comment_upvoted = False
    total_comment_upvotes = [0]
    for comment in comments:

        if comment.upvotes.filter(id=request.user.id).exists():
            comment_id = comment.id
            is_comment_upvoted = True
        else:
            comment_id = False

        total_comment_upvotes.append(comment.total_comment_upvotes())


    context = {

        'post': post,
        'is_upvoted': is_upvoted,
        'total_upvotes': post.total_upvotes(),
        'comments': comments,
        'comment_id' : comment_id,
        'is_comment_upvoted': is_comment_upvoted,
        'total_comment_upvotes': total_comment_upvotes,
        'comment_form': comment_form,

    }
    if request.is_ajax():
        html = render_to_string('Discussion_Forum/comments.html', context, request=request)
        return JsonResponse({'form': html})


    return render(request, "Discussion_Forum/question_view.html", context)




def upvote_post(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))

    #is_upvoted = False
    if post.upvotes.filter(id=request.user.id).exists():
        post.upvotes.remove(request.user)
        is_upvoted = False
    else:
        post.upvotes.add(request.user)
        is_upvoted = True

    context = {
        'post': post,
        'is_upvoted': is_upvoted,
        'total_upvotes': post.total_upvotes(),
    }

    if request.is_ajax():
        html = render_to_string('Discussion_Forum/upvotepost_section.html', context, request=request)
        return JsonResponse({'form': html})

    return HttpResponseRedirect(post.get_absolute_url())

def post_create(request):

    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostCreateForm()

    context = {
        'form': form,
    }
    return render(request, 'Discussion_Forum/post_create.html', context)

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if post.author != request.user:
        raise Http404()
    if request.method == "POST":
        form = PostEditForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostEditForm(instance=post)
    context = {
        'form': form,
        'post': post,
        }
    return render(request, 'Discussion_Forum/post_edit.html', context)

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.author:
        raise Http404
    post.delete()

    url: str = 'http://127.0.0.1:8000/forum'
    return redirect(url)

@login_required()
def updown_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    print(comment)
    if comment.upvotes.filter(id=request.user.id).exists():
        comment.upvotes.remove(request.user)
        is_comment_upvoted = False
    else:
        comment.upvotes.add(request.user)
        is_comment_upvoted = False

    attr = comment.post.id
    attr2 = comment.post.slug
    
    url: str = 'http://127.0.0.1:8000/forum/question/' + str(attr) + '/' + str(attr2)

    return HttpResponseRedirect(url)


class PostsView(ListView):
    model = Post
    paginate_by = 5
    context_object_name = 'posts'
    template_name = 'Discussion_Forum/post_view.html'

