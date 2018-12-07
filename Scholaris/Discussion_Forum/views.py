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
import copy
from Result_Analysis.models import Course,Teacher


# Create your views here.
def post_list(request):
    post_list = Post.published.all().order_by('-updated')
    query = request.GET.get('q')
    if query:
        post_list = Post.published.filter(
            Q(title__icontains=query)|
            Q(author__username=query)|
            Q(body__icontains=query)
        )

    Tag = request.POST.getlist('check')

    if Tag:

        p1 = []
        for tag in Tag:
            p1.extend(Post.published.filter(Q(tag__icontains=tag)))
        post_list = copy.deepcopy(p1)

    tags = []
    for post in post_list:
        tag = post.tag
        tag = tag.split("  ")

        tags.append(tag)


    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    post = zip(posts, tags)
    context = {
        'post': post,
        'posts': posts,
        'courses': Course.objects.all(),
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

    teacher_present = True
    teacher_not_present = False
    is_teacher = []

    is_comment_upvoted = []
    total_comment_upvotes = []
    for comment in comments:

        try:
            comment.user.teacher
            is_teacher.append(teacher_present)
        except:
            is_teacher.append(teacher_not_present)


        if comment.upvotes.filter(id=request.user.id).exists():
            is_comment_upvoted.append(True)
        else:
            is_comment_upvoted.append(False)

        total_comment_upvotes.append(comment.total_comment_upvotes())

    up = zip(comments,total_comment_upvotes,is_comment_upvoted,is_teacher)


    context = {

        'post': post,
        'is_upvoted': is_upvoted,
        'total_upvotes': post.total_upvotes(),
        'comment_form': comment_form,
        'comments':comments,
        'up': up,
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

@login_required()
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.author:
        raise Http404
    post.delete()
    return redirect('forum:forum-post-list')

@login_required()
def updown_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    if comment.upvotes.filter(id=request.user.id).exists():
        comment.upvotes.remove(request.user)
    else:
        comment.upvotes.add(request.user)

    return HttpResponseRedirect(comment.post.get_absolute_url())

