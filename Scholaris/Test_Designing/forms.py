from django import forms
from .models import *

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
        time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
        model = Test
        fields = ('time','duration')





