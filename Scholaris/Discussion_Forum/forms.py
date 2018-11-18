from django import forms
from .models import *

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {
            'title',
            'body',
            'tag',
            'status'
        }

class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {
            'title',
            'body',
            'tag',
            'status'
        }

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'text', 'rows' :'4', 'cols':'50'}))
    class Meta:
        model = Comment
        fields = ('content',)

