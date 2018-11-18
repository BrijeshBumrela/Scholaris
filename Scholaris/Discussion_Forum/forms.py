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
    class Meta:
        model = Comment
        fields = ('content',)

