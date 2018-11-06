from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm, TeacherRegistrationForm
from django.contrib.auth import authenticate,login
from .models import Student, Teacher, Course



def index(request):
    return render(request, 'landing.html')

def dashboard(request):
    return render(request, 'Result_Analysis/dashboard.html')


def student_register(request):
    form = TeacherRegistrationForm(request.POST or None)
    form1 = StudentRegistrationForm(request.POST or None)

    if request.method == 'POST':

        if form1.is_valid():
            new_user = form1.save()
            new_student = Student(student=new_user)
            new_user.save()
            new_student.save()
            username = form1.cleaned_data.get('username')
            raw_password = form1.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('result:course_list')
    else:
        form = TeacherRegistrationForm()
        form1 = StudentRegistrationForm()

    context = {
        'form': form,
        'form1': form1
    }
    return render(request, 'registration/register.html', context)


def register(request):
    form = TeacherRegistrationForm()
    form1 = StudentRegistrationForm()
    context = {
        'form': form,
        'form1': form1
    }
    return render(request, 'registration/register.html', context)

def teacher_register(request):
    form = TeacherRegistrationForm(request.POST or None)
    form1 = StudentRegistrationForm()
    if request.method == 'POST':

        if form.is_valid():
            new_user = form.save()
            new_teacher = Teacher(teacher=new_user)
            new_user.save()
            new_teacher.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('result:course_list')
    else:
        form = TeacherRegistrationForm()
        form1 = StudentRegistrationForm()

    context = {
        'form1': form1,
        'form': form
    }
    return render(request, 'registration/register.html', context)


def course_list(request):
    teacher_list = Teacher.objects.all()
    context = {
        'teacher_list':teacher_list
    }
    return render(request, 'Result_Analysis/course_list.html', context)