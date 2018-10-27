from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate,login, logout
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

    return render(request, 'register.html', context)




def user_logout(request):
    logout(request)
    return redirect('index')


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            print('is it going here?')
            new_user = form.save()
            new_user.save()
            return redirect('index')
    else:
        form = UserRegistrationForm()

    context = {
        'form':form,
    }
    return render(request, 'register.html', context)



