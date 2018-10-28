from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Student



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


def _register(request, form):
    if form.is_valid():
        new_user = form.save()
        new_student = Student(student=new_user)
        new_user.save()
        new_student.save()
        return redirect('index')

def user_register(request):
    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        _register(request, form)
    else:
        form = UserRegistrationForm()

    context = {
        'form':form,
    }
    return render(request, 'register.html', context)



