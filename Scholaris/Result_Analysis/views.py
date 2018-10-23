from django.shortcuts import render
from .forms import UserLoginForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def index(request):
    return render(request, 'base.html')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    HttpResponse("User is not active")
            else:
                HttpResponse("User Not Found")
    else:
        form = UserLoginForm()

    context = {
        'form':form
    }

    return render(request, 'login.html', context)