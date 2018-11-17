from django.shortcuts import render
from .forms import QuestionForm, TestCreateForm
from Test_Designing.models import Test,QuestionSet,Question
from Result_Analysis.models import Teacher,Student
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.http import HttpResponse

import random

def index(request):
    return render(request,'Test_Designing/exam.html')


def design(request):
    test_form = TestCreateForm()
    question_formset = formset_factory(QuestionForm)
    question_formset_post = question_formset(request.POST or None)


    if request.method == 'POST':

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

def exam(request):
    #posts = User.objects.all()
    testid = request.POST['exam-name']
    posts = Question.objects.filter(question__question_list__id=testid)
    if posts.count() is 0:
        return HttpResponse('exam not found!')
    else:
        test = list(posts)
        random.shuffle(test)
        context = {
            'posts': test,
        }
        return render(request,'Test_Designing/test.html',context)
    #return HttpResponse('exam')


def result(request):
    testid = 1
    posts = Question.objects.filter(question__question_list__id=testid)
    correct = 0
    for p in posts:
        ans = request.POST['qs-{}'.format(p.id)]
        true_ans = p.answer
        if ans is true_ans:
            correct +=1

    return render(request,'Test_Designing/result.html',{'score':correct})


def exam_form(request):
    return render(request,'Test_Designing/quiz-form.html')