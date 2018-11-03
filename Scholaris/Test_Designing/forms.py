from django import forms
from django.forms import formset_factory
from .models import Contact

# class QuestionForm(forms.ModelForm):
#
#     class Meta:
#         model = Question
#
#     text = forms.TextInput()
#     option1 = forms.CharField(max_length=200, required=True)
#     option2 = forms.CharField(max_length=200, required=True)
#     option3 = forms.CharField(max_length=200, required=True)
#     option4 = forms.CharField(max_length=200, required=True)
#
#     CHOICES = [('option1'),('option2'),('option3'),('option4'),]
#
#     answer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=True)
#
#
#
#
#

class ContactForm(forms.ModelForm):

    class Meta:
        model=Contact
        fields=['contact_name','contact_group','phone','email',]
        widgets = {
            'contact_name': forms.TextInput(attrs={'required': True}),
            'phone': forms.TextInput(attrs={'required': True}),
            'Email': forms.EmailInput(attrs={'required': True}),

        }