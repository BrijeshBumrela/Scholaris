from django.db import models
from Result_Analysis.models import Teacher
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

# class Test(models.Model):
#     teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
#     exam_time = models.DateTimeField()
#
# class QuestionSet(models.Model):
#     question_list = models.OneToOneField(Test, on_delete=models.CASCADE)
#
# class Question(models.Model):
#     question = models.ForeignKey(QuestionSet, on_delete=models.CASCADE)
#     text = models.TextField()
#     option1 = models.CharField(max_length=200,
#                                verbose_name='option1')
#     option2 = models.CharField(max_length=200,
#                                verbose_name='option2')
#     option3 = models.CharField(max_length=200,
#                                verbose_name='option3')
#     option4 = models.CharField(max_length=200,
#                                verbose_name='option4')
#
#     OPTIONS = (
#         ('1','option1'),
#         ('2','option2'),
#         ('3','option3'),
#         ('4','option4'),
#     )
#
#     answer = models.CharField(max_length=200, choices=OPTIONS)
#
#     def __str__(self):
#         return self.question
#
# # @receiver(pre_save, sender=Question)
# # def pre_save_connection(sender, **kwargs):
# #     kwargs['instance'].question =
#


class Contact(models.Model):
    CONTACT_GROUP=(("PRE-SALES","PRE-SALES"),("SALES","SALES"),("SERVICE","SERVICE"))

    contact_name = models.CharField(max_length=50,blank=True,null=True)
    contact_group = models.CharField(max_length=50,choices=CONTACT_GROUP,blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(max_length=30,blank=True,null=True)
    def __str__(self):
        return self.name