from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate,login, logout
from .models import Student, Teacher



def index(request):
    return render(request, 'landing.html')

def dashboard(request):
    return render(request, 'Result_Analysis/dashboard.html')


def student_register(request):
    form = UserRegistrationForm(request.POST or None)
    form1 = UserRegistrationForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            new_user = form.save()
            print(form)
            new_student = Student(student=new_user)
            new_user.save()
            new_student.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('result:dashboard')
    else:
        form = UserRegistrationForm()
        form1 = UserRegistrationForm()

    context = {
        'form': form,
        'form1': form1
    }
    return render(request, 'registration/register.html', context)


def register(request):
    form = UserRegistrationForm()
    form1 = UserRegistrationForm()
    context = {'form': form, 'form1': form1}
    return render(request, 'registration/register.html', context)

def teacher_register(request):
    form1 = UserRegistrationForm(request.POST or None)
    form = UserRegistrationForm()
    if request.method == 'POST':

        if form1.is_valid():
            new_user = form1.save()
            new_student = Teacher(teacher=new_user)
            new_user.save()
            new_student.save()
            username = form1.cleaned_data.get('username')
            raw_password = form1.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('result:dashboard')
    else:
        form = UserRegistrationForm()
        form1 = UserRegistrationForm()

    context = {
        'form1': form1,
        'form': form
    }
    return render(request, 'registration/register.html', context)

