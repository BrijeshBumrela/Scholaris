from django import forms
from .models import *
from django.utils import timezone

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['option1','option2','option3','option4','text','answer','mark']
        widgets = {
            'option1': forms.TextInput(attrs={'required':True}),
            'option2': forms.TextInput(attrs={'required':True}),
            'option3': forms.TextInput(attrs={'required':True}),
            'option4': forms.TextInput(attrs={'required':True}),
            'text': forms.Textarea(attrs={'required':True}),
            'answer':forms.Select(attrs={'required':True}),
            'mark': forms.TextInput(attrs={'required':True})
        }


class TestCreateForm(forms.ModelForm):
    class Meta:
        model = Test
        exclude = ('teacher','total_marks',)


    def clean(self):
        cleaned_data = super().clean()

        exam_date = cleaned_data.get('time')
        if exam_date < timezone.now():
            self.add_error('time', 'Selected Time from past')

        exam_duration = cleaned_data.get('duration')
        if exam_duration < 0:
            self.add_error('duration', 'Time can not be negative')



