from django.shortcuts import render, redirect, get_object_or_404
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

def choose_course_teacher(request):
    course_list = Course.objects.all()
    context = {
        'course_list': course_list
    }
    return render(request, 'Result_Analysis/choose_course_teacher.html', context)

def list_all_students(request):
    std2 = Student.objects.all()
    stud_list = []
    for stud in std2:
        stud_list.append(stud.student.username)
    context = {
        'all_students': stud_list
    }
    print(stud_list)
    return render(request, 'Result_Analysis/list_all_students.html', context)

def list_all_teachers_to_follow(request):
    teachers = Teacher.objects.all()
    context = {
        'all_teachers': teachers
    }
    return render(request, 'Result_Analysis/follow.html', context)


def set_course_teacher(request):
    if request.method == "POST":

        selected_course = request.POST.get('course')
        print(selected_course + ' jafhhjkasdhflksahfkljsahfdlkjsahdflkjhasldkfjhsakljdfhjsalkfhlfsdalk')
        get_course = Course.objects.get(name=selected_course)
        teacher = get_object_or_404(Teacher, pk=request.user.teacher.id)
        teacher.course = get_course
        teacher.save()
        return HttpResponse('Done')
    else:
        print('Not freaking running')
        return HttpResponse('Not done')

def follow(request):
    if request.method == 'POST':
        selected_teacher = request.POST.getlist('teacher')
        student = Student.objects.get(student=request.user)
        for teacher in Teacher.objects.all():
            if teacher.teacher.username in selected_teacher:
                teacher.followers.add(student)
            else:
                teacher.followers.remove(student)
            teacher.save()
        return HttpResponse('Done')

    return HttpResponse('Nothing Found')
