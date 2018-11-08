from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm, TeacherRegistrationForm
from django.contrib.auth import authenticate,login
from .models import Student, Teacher, Course
from django.http import HttpResponse



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


def choose_course(request):
    course_list = Course.objects.all()
    context = {
        'course_list':course_list
    }
    return render(request, 'Result_Analysis/course_list.html', context)

def set_course_teacher(request):
    if request.method == "POST":

        selected_course = request.POST.get('course')
        print(selected_course + ' jafhhjkasdhflksahfkljsahfdlkjsahdflkjhasldkfjhsakljdfhjsalkfhlfsdalk')
        get_course = Course.objects.get(name=selected_course)
        return HttpResponse('Done')
    else:
        print('Not freaking running')
        return HttpResponse('Not done')


def course(request):
    if request.method == 'POST':
        selected_courses = request.POST.getlist('course')
        student = Student.objects.get(student=request.user)

        for course in Course.objects.all:
            if course in selected_courses:
                student.course.add(get_course)
            else:
                student.course.remove(course)
        student.save()

        return redirect('result:dashboard')
    course_list = Course.objects.all()
    context = {
        'course_list': course_list
    }
    return render(request, "Result_Analysis/course_set.html", context)