from django.shortcuts import render, get_object_or_404
from .forms import QuestionForm, TestCreateForm
from Test_Designing.models import Test,QuestionSet,Question,StudentResult
from Result_Analysis.models import Teacher,Student
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.http import HttpResponse
import random
from django.contrib.auth.decorators import user_passes_test, login_required



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

@login_required(login_url='result:login')
@user_passes_test(check_student, login_url='/test/error')
def result(request, id):
    test = Test.objects.get(id=id)
    student = Student.objects.get(student=request.user)
    questions = test.questionset.question_set.all()

    correct = 0
    marks = 0

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
        'marks':marks,
        'correct_ans':correct,
        'wrong_ans':wrong
    }
    return render(request,'Test_Designing/result.html', context)



#exam-taking vies ends here

@login_required()
@user_passes_test(check_student, login_url='/test/error')
def list_all_test(request):
    teacher_list = Teacher.objects.filter(followers=request.user.student)
    test_list = []
    for teacher in teacher_list:
        test_list.extend(teacher.test_set.all())
    context = {
        'test_list':test_list
    }
    return render(request, 'Test_Designing/test_list.html', context)


def detail(request, id):
    get_test = get_object_or_404(Test, id=id)
    question_list = get_test.questionset.question_set.all()
    print(question_list)
    context = {
        'que_list':question_list,
        'test':get_test
    }

    return render(request, 'Test_Designing/test.html', context)
