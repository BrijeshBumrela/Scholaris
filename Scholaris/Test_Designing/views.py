from django.shortcuts import render
from django.urls import reverse
from .forms import QuestionForm
from .models import Question, QuestionSet, Test
from django.forms import formset_factory,

def index(request):
    return render(request,'Test_Designing/exam.html')


def design(request):
    formset = QuestionFormset(request.POST or None)

    if request.method == 'POST':
        formset = QuestionFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                text = form.cleaned_data.get('text')
                option1 = form.cleaned_data.get('option1')
                option2 = form.cleaned_data.get('option2')
                option3 = form.cleaned_data.get('option3')
                option4 = form.cleaned_data.get('option4')

                new_question = Question(option1=option1,option2=option2,option3=option3,option4=option4)

