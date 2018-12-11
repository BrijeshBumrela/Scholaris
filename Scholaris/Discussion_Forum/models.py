from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils import timezone

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")

class Post(models.Model):

    objects = models.Manager() # Default Manager
    published = PublishedManager() # Custom Model Manager

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title   = models.CharField(max_length=150)
    slug    = models.SlugField(max_length=150)
    author  = models.ForeignKey(User, related_name='forum_posts', on_delete=models.CASCADE,)
    body    = models.TextField()
    tag     = models.CharField(max_length=150)
    upvotes = models.ManyToManyField(User, related_name='upvotes', blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status  = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return  self.title

    def total_upvotes(self):
        return self.upvotes.count()

    def get_absolute_url(self):
        return reverse("forum:forum-question", args=[self.id, self.slug])

@receiver(pre_save, sender=Post)
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug

class Comment(models.Model):
    post      = models.ForeignKey(Post, on_delete=models.CASCADE)
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    content   = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    upvotes   = models.ManyToManyField(User, related_name='comment_upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='comment_downvotes', blank=True)

    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))

    def total_comment_upvotes(self):
        return self.upvotes.count()

    def total_comment_downvotes(self):
        return self.downvotes.count()




