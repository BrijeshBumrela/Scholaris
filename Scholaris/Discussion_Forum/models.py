
from django.db import models
from django.urls import reverse
#from Result_Analysis.models import Student,Teacher
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title   = models.CharField(max_length=150)
    slug    = models.SlugField(max_length=150)
    author  = models.ForeignKey(User, related_name='forum_posts', on_delete=models.CASCADE,)
    body    = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status  = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return  self.title

    def get_absolute_url(self):
        return reverse("forum:forum-question", args=[self.id, self.slug])
