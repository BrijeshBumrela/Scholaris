from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import authenticate, login, update_session_auth_hash
from .models import Student, Teacher, Course , otp_verify, Task
from django.http import HttpResponse
from Test_Designing.models import StudentResult, Test
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required, user_passes_test
from Discussion_Forum.models import Post
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
import random
from django.contrib import messages
from datetime import date

def age(born):
    today = date.today()
    try: 
        birthday = born.replace(year=today.year)
    except ValueError: # raised when birth date is February 29 and the current year is not a leap year
        birthday = born.replace(year=today.year, month=born.month+1, day=1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year
'''             Utility Functions            '''

def get_question():
    return Post.published.all().order_by('-updated')[:5]


def post_count(user):
    posts = Post.objects.filter(author=user)
    return len(posts)

'''                 """"""""""               '''

def send(email):
    global otp
    otp=random.randint(100000,999999)
    mail=EmailMessage('Email Verification','your otp is'+str(otp),to=[email])
    mail.send()
    print(otp)
    return otp


def index(request):
    try:
        if request.user.is_authenticated:
            print('Hi There')
            return redirect('result:dashboard')
    except:
        return render(request, 'Result_Analysis/home.html')


def dash_percent(result):
    marks=[]
    total=[]
    for tests in result:
        marks.append(tests.marks)
        total.append(tests.test.total_marks)
    no_tests=len(marks)
    if no_tests==0:
        percentage=0
    else:
        percentage=(sum(marks)/sum(total))*100
        percentage=round(percentage,2)
    return percentage

def dash_marks(result):
    marks=[]
    for tests in result:
        marks.append(tests.marks)
    length=len(marks)
    if length>10:
        marks=marks[length-10:]
    return marks


def dash_test(result):
    test_ids=[]
    for x in result:
        test_ids.append(x.test.id)
    length=len(test_ids)
    if length>10:
        test_ids=test_ids[length-10:]
    return test_ids


@login_required()
def dashboard(request):

    try:
        if request.user.student:
            student = get_object_or_404(Student, id=request.user.student.id)

            teachers = student.teacher_set.all()
            events = []

            for teacher in teachers:
                events.extend(teacher.test_set.all())

            dash = StudentResult.objects.filter(student__id=request.user.student.id)
            percent=dash_percent(dash)
            marks=dash_marks(dash)
            tests=dash_test(dash)

            posts = get_question()
            print(posts)
            context = {
                'posts':posts,
                'percent':percent,
                'marks':marks,
                'tests':tests,
                'events':events
            }
            return render(request, 'Result_Analysis/dashboard1.html', context)
    except:
        pass
    posts = get_question()
    countPost = post_count(request.user)



    context = {
        'posts': posts,
        'post_count': countPost,
    }
    return render(request, 'Result_Analysis/dashboard1.html', context)

def register(request):
    form = TeacherRegistrationForm()
    form1 = StudentRegistrationForm()
    context = {
        'form': form,
        'form1': form1
    }
    return render(request, 'Result_Analysis/register.html', context)

def get_this(request):
    return render(request, 'Result_Analysis/ques1.html')


def student_register(request):
    form = TeacherRegistrationForm(None)
    form1 = StudentRegistrationForm(request.POST or None)

    if request.method == 'POST':

        if form1.is_valid():
            email=form1.data['email']
            otp1=send(email)
            #new_user = form1.save(commit=False)
            firstname=form1.data['first_name']
            lastname=form1.data['last_name']
            username=form1.data['username']
            password1=form1.data['password1']
            password2=form1.data['password2']
            try:
                user=otp_verify.objects.get(name=username)
                user.otp=otp1   
                user.save()     
            except:
                user_otp=otp_verify.objects.create(name=username,otp=otp1)
                user_otp.save()
            context={
                'firstname':firstname,
                'lastname':lastname,
                'username':username,
                'email':email,
                'password1':password1,
                'password2':password2,
            }
            return render(request,'Result_Analysis/verify.html',context)
    else:
        form = TeacherRegistrationForm()
        form1 = StudentRegistrationForm()

    context = {
        'form': form,
        'form1': form1
    }
    return render(request, 'Result_Analysis/register.html', context)

def verify(request):
    if request.method=='POST':
        otp1=request.POST.get('typed_otp')
        username=request.POST.get('username')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        otp2 = otp_verify.objects.get(name=username).otp
        print(otp2)
        if otp1 == str(otp2):
            new_user=User.objects.create(username=username,email=email,first_name=firstname,last_name=lastname)
            new_user.set_password(request.POST['password1'])           
            new_student = Student(student=new_user)
            new_user.save()
            new_student.save()
            raw_password = request.POST.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('result:dashboard')
        else:
            context={
                'firstname':firstname,
                'lastname':lastname,
                'username':username,
                'email':email,
                'password1':password1,
                'password2':password2,
            }
            messages.error(request,'wrong otp')
            return render(request,'Result_Analysis/verify.html',context)
    else:
        return HttpResponse('wrong way')


def teacher_register(request):
    form = TeacherRegistrationForm(request.POST or None)
    form1 = StudentRegistrationForm()
    if request.method == 'POST':

        if form.is_valid():
            email=form.data['email']
            otp1=send(email)
            firstname=form.data['first_name']
            lastname=form.data['last_name']
            username=form.data['username']
            password1=form.data['password1']
            password2=form.data['password2']
            try:
                user=otp_verify.objects.get(name=username)
                user.otp=otp1   
                user.save()     
            except:
                user_otp=otp_verify.objects.create(name=username,otp=otp1)
                user_otp.save()
            context={
                'firstname':firstname,
                'lastname':lastname,
                'username':username,
                'email':email,
                'password1':password1,
                'password2':password2,
            }
            return render(request,'Result_Analysis/verify2.html',context)
    else:
        form = TeacherRegistrationForm()
        form1 = StudentRegistrationForm()

    context = {
        'form1': form1,
        'form': form
    }
    return render(request, 'Result_Analysis/register.html', context)

def verify2(request):
    if request.method=='POST':
        username=request.POST.get('username')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        otp1=request.POST.get('typed_otp')
        otp2 = otp_verify.objects.get(name=username).otp
        if otp1 == str(otp2):          
            raw_password=request.POST.get('password1')
            new_user1=User.objects.create(username=username,email=email,first_name=firstname,last_name=lastname)
            new_user1.set_password(request.POST['password1'])           
            new_teacher = Teacher(teacher=new_user1)
            new_user1.save()
            new_teacher.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('result:choose_course_teacher')
        else:
            context={
                'firstname':firstname,
                'lastname':lastname,
                'username':username,
                'email':email,
                'password1':password1,
                'password2':password2,
            }
            messages.error(request,'wrong otp')
            return render(request,'Result_Analysis/verify2.html',context)
    else:
        return HttpResponse('wrong way')

def forget_email(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        resetotp=send(email)
        try:
            username=User.objects.get(email=email).username
        except:
            messages.error(request,'no user exists with this email')
            return render(request,'Result_Analysis/forget_email.html')

        try:
            user=otp_verify.objects.get(name=username)
            user.otp=resetotp   
            user.save()     
        except:
            user_otp=otp_verify.objects.create(name=username,otp=resetotp)
            user_otp.save()
        return render(request,'Result_Analysis/forget_otp.html',{'email':email})
    else:
        return render(request,'Result_Analysis/forget_email.html')

def otp_verification(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        username=User.objects.get(email=email).username
        new_otp= otp_verify.objects.get(name=username).otp
        otp1=request.POST.get('otp1')
        if otp1 == str(new_otp) :
            return render(request,'Result_Analysis/forget_password.html',{'email':email})
        else:
            messages.error(request,'incorrect otp')
            return render(request,'Result_Analysis/forget_otp.html',{'email':email})
    else:
        return render(request,'Result_Analysis/forget_otp.html')
        

def reset_password(request):  
    if request.method == 'POST':
        email=request.POST.get('email')
        username=User.objects.get(email=email).username
        user=User.objects.get(username=username)
        reset1=request.POST['resetpass1']
        reset2=request.POST['resetpass2']
        if reset1!=reset2:
            messages.error(request,'passwords didnot match')
            return render(request,'Result_Analysis/forget_password.html',{'email':email}) 
        if len(reset1)<8:
            messages.error(request,'password is too short')
            return render(request,'Result_Analysis/forget_password.html',{'email':email})    
        user.set_password(reset1)
        user.save()
        return redirect('result:login')
    else:
        return render(request,'Result_Analysis/forget_password.html')

def choose_course_teacher(request):
    teacher = get_object_or_404(Teacher, id=request.user.teacher.id)
    if teacher.course:
        messages.warning(request, 'You have Already selected course!')
        return redirect('result:dashboard')

    course_list = Course.objects.all()
    context = {
        'course_list': course_list
    }
    return render(request, 'Result_Analysis/courses.html', context)

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
        'teachers': teachers
    }
    return render(request, 'Result_Analysis/tea.html', context)


def set_course_teacher(request):
    if request.method == "POST":

        selected_course = request.POST.get('course')
        print(selected_course + ' ' + 'foa;iesnoisevn')
        get_course = Course.objects.get(name=selected_course)
        teacher = get_object_or_404(Teacher, pk=request.user.teacher.id)
        teacher.course = get_course
        teacher.save()
        messages.success(request, 'Course Successfully Set')
        return redirect('result:dashboard')
    else:
        return HttpResponse('Some Error Occured')

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
        try:
            if request.user.student:
                p_form= ProfileUpdateForm(request.POST,request.FILES,instance=request.user.student or None)
        except:
            p_form = TeacherProUpdateForm(request.POST, request.FILES, instance=request.user.teacher)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('result:profile')
    else:
        u_form= UserUpdateForm(instance=request.user)
        try:
            if request.user.student:
                p_form= ProfileUpdateForm(instance=request.user.student)
        except:
            p_form = TeacherProUpdateForm(instance=request.user.teacher)

        # std=Student.objects.filter(pk=request.user.student.id)
        # for std in std:
        #     born=std.dob
        # aged=age(born)

    context ={
        'u_form':u_form,
        'p_form':p_form,
        # 'age':aged,
    }
    return render(request, 'Result_Analysis/profile.html', context)

'''       Profile for teacher         '''
def change_password(request):
    if request.method== 'POST':
        change_form = passwordchange(data=request.POST,user=request.user)
        if change_form.is_valid():
            change_form.save()
            update_session_auth_hash(request,change_form.user)
            try:
                if request.user.student:
                    return redirect('result:profile')
            except:
                return redirect('result:profile')
    else:
        change_form=passwordchange(user=request.user)
    context ={
        'change_form':change_form,
    }
    return render(request, 'Result_Analysis/updatepassword.html', context)


def course(stds):
    for std in stds:
        number=std.course.count()
    return number



def name(no_courses,stds):
    names=[]
    keys=[]
    for i in stds:
        for j in range(0,no_courses):
            keys.append(i.course.values('name')[j])
    for k in keys:
        names.append(k['name'])
    return names




def highest(result):
    marks_list=[]
    for i in result:
        marks_list.append(i.marks)
    if marks_list==[]:
        high=0
    else:
        high=max(marks_list)
    return high



def course_percentage(result):
    marks=[]
    total=[]
    for tests in result:
        marks.append(tests.marks)
        total.append(tests.test.total_marks)
    no_tests=len(marks)
    if no_tests==0:
        percentage=0
    else:
        percentage=(sum(marks)/sum(total))*100
        percentage=round(percentage,2)
    return percentage



def marks(result):
    test_marks=[]
    for tests in result:
        test_marks.append(tests.marks)
    if len(test_marks)>10:
        length=len(test_marks)-10
        test_marks=test_marks[length:]
    return test_marks


def StudentNames(result):
    names=set()
    for std in result:
        x=std.student.student.username
        names.add(x)
    return names


def topper(student,result):
    percent=[]
    for std in student:
        marks=[]
        total=[]
        for tests in result:
            if tests.student.student.username==std:
                marks.append(tests.marks)
                total.append(tests.test.total_marks)
        no_tests=len(marks)
        if no_tests==0:
            percentage=0
        else:
            percentage=(sum(marks)/sum(total))*100
            percentage=round(percentage,2)
            percent.append(percentage)
    top=max(percent)
    return top


def average(result):
    marks=[]
    total=[]
    for tests in result:
        marks.append(tests.marks)
        total.append(tests.test.total_marks)
    no_tests=len(marks)
    if no_tests==0:
        percentage=0
    else:
        percentage=(sum(marks)/sum(total))*100
        percentage=round(percentage,2)
    return percentage
def test(result):
    test_ids=[]
    str1="test"
    for x in result:
        test_ids.append(x.test.id)
    # for i in range(0,len(test_ids)):
    #     x=test_ids[i]
    #     test_ids[i]=str1+str(x)
    length=len(test_ids)
    if length>10:
        test_ids=test_ids[length-10:]
    return test_ids

def results(request):
    student = Student.objects.filter(pk=request.user.student.id)
    result= StudentResult.objects.filter(student__id=request.user.student.id)
    no_courses=course(student)
    names=name(no_courses,student)
    high=highest(result)
    if request.method=='POST':
        subject=request.POST['select_course']
        result2= StudentResult.objects.filter(test__teacher__course__name=subject,student__id=request.user.student.id)
        result3= StudentResult.objects.filter(test__teacher__course__name=subject)
        StdNames=StudentNames(result3)
        test_marks=marks(result2)
        testids=test(result2)
        percent=course_percentage(result2)
        top=topper(StdNames,result3)
        avg=average(result3)
        context = {'testids':testids,'average':avg,'top':top,'stdnames':StdNames,'students':no_courses,'results':result,'high':high,'courses':names,'test_marks':test_marks,'percentage':percent,'no_courses':no_courses,'course_name':result2,}
        return render(request,'Result_Analysis/results.html',context)
    else:
        context = {'students':no_courses,'results':result,'high':high,'courses':names,'no_courses':no_courses,}
        return render(request,'Result_Analysis/results.html',context)

@login_required()
def add_task(request):
    if request.method == 'POST':
        text = request.POST['text']

    Task.objects.create(author=request.user, text=text)

    return HttpResponse('')



