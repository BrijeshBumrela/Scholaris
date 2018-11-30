from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import authenticate, login, update_session_auth_hash
from .models import Student, Teacher, Course, Task
from django.http import HttpResponse
from Test_Designing.models import StudentResult, Test
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required, user_passes_test
from Discussion_Forum.models import Post


'''             Utility Functions            '''

def get_question():
    return Post.published.all().order_by('-updated')[:5]


def post_count(user):
    posts = Post.objects.filter(author=user)
    return len(posts)

'''                 """"""""""               '''

def index(request):
    try:
        if request.user.teacher or request.user.student:
            print('Hi There')
            return redirect('result:dashboard')
    except:
        print('hiiiiiii')
        return render(request, 'Result_Analysis/home.html')


@login_required()
def dashboard(request):
    user = get_object_or_404(User, pk=request.user.id)
    posts = get_question()
    countPost = post_count(request.user)
    tasks = user.task_set.all()

    context = {
        'posts': posts,
        'post_count': countPost,
        'tasks': tasks
    }
    return render(request, 'Result_Analysis/dashboard1.html', context)


def student_register(request):
    form = TeacherRegistrationForm(None)
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
            return redirect('result:dashboard')
    else:
        form = TeacherRegistrationForm()
        form1 = StudentRegistrationForm()

    context = {
        'form': form,
        'form1': form1
    }
    return render(request, 'Result_Analysis/register.html', context)


def register(request):
    form = TeacherRegistrationForm()
    form1 = StudentRegistrationForm()
    context = {
        'form': form,
        'form1': form1
    }
    return render(request, 'Result_Analysis/register.html', context)

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
            return redirect('result:choose_course_teacher')
    else:
        form = TeacherRegistrationForm()
        form1 = StudentRegistrationForm()

    context = {
        'form1': form1,
        'form': form
    }
    return render(request, 'Result_Analysis/register.html', context)

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

        return redirect('result:dashboard')
    course_list = Course.objects.all()
    context = {
        'course_list': course_list
    }
    return render(request, "Result_Analysis/course_set.html", context)

def student_list_teacher(request):
    teacherInstance = get_object_or_404(Teacher, pk=request.user.teacher.id)
    students = teacherInstance.followers.all()
    print(students)
    context = {
        'students': students,
        'count': len(students)
    }
    return render(request, "Result_Analysis/stu.html", context)


'''        Profile for student        '''

def profile(request):
    if request.method == 'POST':
        u_form= UserUpdateForm(request.POST,instance=request.user or None)
        p_form= ProfileUpdateForm(request.POST,request.FILES,instance=request.user.student or None)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('result:profile')
    else:
        u_form= UserUpdateForm(instance=request.user)
        p_form= ProfileUpdateForm(instance=request.user.student)
    context ={
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request, 'Result_Analysis/profile.html', context)

'''       Profile for teacher         '''

def teacher_profile(request):
    if request.method == 'POST':
        u1_form = UserUpdateForm(request.POST, instance=request.user)
        p1_form = TeacherProUpdateForm(request.POST, request.FILES, instance=request.user.teacher)

        if u1_form.is_valid() and p1_form.is_valid():
            u1_form.save()
            p1_form.save()
            return redirect('result:profile2')
    else:
        u1_form = UserUpdateForm(instance=request.user)
        p1_form = TeacherProUpdateForm(instance=request.user.teacher)
    context = {
        'u1_form': u1_form,
        'p1_form': p1_form,
    }
    return render(request, 'Result_Analysis/profile.html', context)


def change_password(request):
    if request.method== 'POST':
        change_form = passwordchange(data=request.POST,user=request.user)
        if change_form.is_valid():
            change_form.save()
            update_session_auth_hash(request,change_form.user)
            if request.user.teacher:
                return redirect('result:profile2')
            else:
                return redirect('result:profile1')
    else:
        change_form=passwordchange(user=request.user)
    context ={
        'change_form':change_form,
    }
    return render(request, 'Result_Analysis/updatepassword.html', context)



def results(request):
    x = Student.objects.filter(pk=request.user.student.id)
    y= StudentResult.objects.filter(student__id=request.user.student.id)
    marks_list_all=[]
    list2=[]
    names_courses=[]
    test_marks=[]
    total=[]
    for a in x:
        no_courses=a.course.count()
    for i in x:
        for j in range(0,no_courses):
            list2.append(i.course.values('name')[j])
    for k in list2:
        names_courses.append(k['name'])
    for i in y:
        marks_list_all.append(i.marks)
    if marks_list_all==[]:
        high=0
    else:
        high=max(marks_list_all)
    if request.method == 'POST':
        subject=request.POST['select_course']
        course_name= StudentResult.objects.filter(test__teacher__course__name=subject,student__id=request.user.student.id)
        for tests in course_name:
            test_marks.append(tests.marks)
            total.append(tests.test.total_marks)
        no_tests=len(test_marks)
        if no_tests==0:
            percentage=0
        else:
            percentage=(sum(test_marks)/sum(total))*100
            percentage=round(percentage,2)
        context = {'students':x,'results':y,'high':high,'courses':names_courses,'test_marks':test_marks,'percentage':percentage,'no_courses':no_courses,'course_name':course_name,}
        return render(request,'Result_Analysis/results.html',context)
    else:
        context = {'students':x,'results':y,'high':high,'courses':names_courses,'no_courses':no_courses,}
        return render(request,'Result_Analysis/results.html',context)

@login_required()
def add_task(request):
    if request.method == 'POST':
        text = request.POST['text']

    Task.objects.create(author=request.user, text=text)

    return HttpResponse('')



