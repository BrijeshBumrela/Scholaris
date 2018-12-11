from django.shortcuts import render, get_object_or_404, redirect
from .forms import QuestionForm, TestCreateForm
from Test_Designing.models import Test,QuestionSet,Question,StudentResult
from Result_Analysis.models import Teacher,Student
from django.contrib import messages
from django.forms import formset_factory
from django.http import HttpResponse
import random
from django.contrib.auth.decorators import user_passes_test, login_required
import datetime
from django.utils import timezone

'''  Utility Functions   '''

def check_teacher(user):
    try:
        Teacher.objects.get(teacher=user)
        return True
    except:
        return False

def check_student(user):
    try:
        Student.objects.get(student=user)
        return True
    except:
        return False

'''        end          '''



def index(request):
    return render(request,'Test_Designing/exam.html')


def exam_error(request):
    return render(request, 'Test_Designing/exam/exam_error.html')


@login_required(login_url='result:login')
@user_passes_test(check_teacher, login_url='/test/error')
def design(request):
    test_form = TestCreateForm()
    question_formset = formset_factory(QuestionForm)
    question_formset_post = question_formset(request.POST or None)


    if request.method == 'POST':

        total_marks = 0

        test_form = TestCreateForm(request.POST)
        question_formset_post = question_formset(request.POST)

        if test_form.is_valid() and question_formset_post.is_valid():

            teacher = Teacher.objects.get(teacher=request.user)

            testList = test_form.save(commit=False)
            testList.teacher = teacher
            testList.save()


            questionList = QuestionSet.objects.create(question_list=testList)


            for question in question_formset_post:

                questionInstance = question.save(commit=False)
                questionInstance.question = questionList
                questionInstance.save()

                total_marks = total_marks + questionInstance.mark

            testList.total_marks = total_marks
            testList.save()
            messages.success(request, 'Test Created Successfully')
            return redirect('result:dashboard')



        else:
            context = {
                'test_form':test_form,
                'question_formset':question_formset_post
            }
            return render(request, 'Test_Designing/exam_set.html', context)



    context = {
        'test_form': test_form,
        'question_formset': question_formset
    }
    return render(request, 'Test_Designing/exam_set.html', context)

#exam_taking views starts here

@login_required(login_url='result:login')
@user_passes_test(check_student, login_url='/test/error')
def exam_form(request):
    return render(request,'Test_Designing/quiz-form.html')


@login_required(login_url='result:login')
@user_passes_test(check_student, login_url='/test/error')
def exam(request):
    testid = request.POST['exam-name']
    posts = Question.objects.filter(question__question_list__id=testid)
    get_test = get_object_or_404(Test, id=testid)
    timer = get_test.duration

    expiry_time = get_test.time + datetime.timedelta(minutes=get_test.duration)
    r = expiry_time - timezone.now()
    print(r)
    print(r.seconds)
    if posts.count() is 0:
        return HttpResponse('exam not found!')
    else:
        test = list(posts)
        random.shuffle(test)
        context = {
            'posts': test,
            'no_of_qs':posts.count(),
            'timer': int(r.seconds),
        }
        return render(request,'Test_Designing/t.html',context)
    #return HttpResponse('exam')

@login_required(login_url='result:login')
@user_passes_test(check_student, login_url='/test/error')
def result(request, id):
    test = Test.objects.get(id=id)
    student = Student.objects.get(student=request.user)

    questions = test.questionset.question_set.all()

    correct = 0
    marks = 0
    total_marks = test.total_marks
    for question in questions:
        try:

            ans = request.POST['qs-{}'.format(question.id)]
            if ans == question.answer:
                correct += 1
                marks += question.mark
        except:
            pass


    print(correct)
    print(marks)

    wrong = len(questions) - correct
    StudentResult.objects.create(student=student, test=test, correct_ans=correct, wrong_ans=wrong, marks=marks)

    context = {
        'total_marks':total_marks,
        'marks':marks,
        'correct_ans':correct,
        'wrong_ans':wrong,
    }
    return render(request,'Test_Designing/result.html', context)



#exam-taking views ends here

@login_required(login_url='result:login')
@user_passes_test(check_student, login_url='/test/error')
def list_all_test(request):
    teacher_list = Teacher.objects.filter(followers=request.user.student)
    test_list = []
    for teacher in teacher_list:
        test_list.extend(teacher.test_set.all())

    #test_list = []
    '''
    tl = []
    oneday = datetime.timedelta(days=1)
    for t in list(test_list):

        diff = t.time.date() - datetime.date.today()
        if(diff < oneday ):
            tl.append(t)

        if (t.date.date() > datetime.date.today()):
            tl.append(t)
    #test_list=tl
    '''
    context = {
        'test_list':test_list
    }
    return render(request, 'Test_Designing/test_list.html', context)


def detail(request, id):
    get_test = get_object_or_404(Test, id=id)
    question_list = get_test.questionset.question_set.all()

    student = Student.objects.get(student=request.user)

    timer = get_test.duration

    expiry_time = get_test.time + datetime.timedelta(minutes=get_test.duration)
    r = expiry_time - timezone.now()


    if (get_test.studentresult_set.filter(student=student).exists()):
        return HttpResponse("You Can't Bruh !")

    if question_list.count() is 0:
        return HttpResponse('exam not found!')

    else:
        test = list(question_list)
        random.shuffle(test)
        context = {
            'posts':test,
            'test':get_test,
            'no_of_qs': question_list.count(),
            'timer': r.seconds,
            'expiry_time': expiry_time
        }

    return render(request, 'Test_Designing/t.html', context)


def testdetail(request, id):
    get_test = get_object_or_404(Test, id=id)
    entry_token = False
    expiry_token= False
    expiry_time = get_test.time + datetime.timedelta(minutes=get_test.duration)
    r =expiry_time - timezone.now()
    if get_test.time < timezone.now():
        entry_token = True
    if expiry_time < timezone.now():
        expiry_token = True

    context = {
        'test':get_test,
        'timer': int(r.seconds),
        'time':get_test.time,
        'marks':get_test.total_marks,
        'entry_token':entry_token,
        'expiry_token':expiry_token,
        'expiry_time':expiry_time,
    }
    return render(request, 'Test_Designing/test_description.html', context)

@login_required()
@user_passes_test(check_teacher, login_url='/test/error')
def my_test(request):
    teacher = get_object_or_404(Teacher, id=request.user.teacher.id)

    test_list = teacher.test_set.all()
    is_done = []

    for test in test_list:
        if test.time < timezone.now():
            is_done.append(True)
        else:
            is_done.append(False)


    test_list_done = zip(test_list, is_done)

    context = {
        'test_list': test_list_done
    }

    return render(request, 'Test_Designing/my_test.html', context)


@login_required()
@user_passes_test(check_teacher, login_url='/test/error')
def edit_test(request, id):
    test = get_object_or_404(Test, id=id)
    question_list = test.questionset.question_set.all()


    context = {
        'q_list': question_list
    }

    # return render(request, 'Test_Designing/edit_test.html', context)

    # return render(request, 'Test_Designing/test_description.html', context)
    return render(request, 'Test_Designing/exam_edit.html', context)

@login_required()
@user_passes_test(check_teacher, login_url='/test/error')
def edit_question(request, id):
    instance = get_object_or_404(Question, id=id)
    print(instance)
    if request.method == 'POST':
        form = QuestionForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()


            return redirect('result:dashboard')

    print('no there')
    form = QuestionForm()
    context = {
        'form':form,
        'instance':instance
    }
    return render(request, 'Test_Designing/question_edit.html', context)

