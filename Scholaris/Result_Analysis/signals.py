from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Student , Teacher

@receiver(post_save,sender=User)
def create_profile1(sender,instance,created,**kwargs):
	if created:
		Student.objects.create(user=instance)
@receiver(post_save,sender=User)
def save_profile1(sender,instance,**kwargs):
		instance.Student.save()

@receiver(post_save,sender=User)
def create_profile2(sender,instance,created,**kwargs):
	if created:
		Teacher.objects.create(user=instance)
@receiver(post_save,sender=User)
def save_profile2(sender,instance,**kwargs):
		instance.Teacher.save()