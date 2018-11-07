from django.db import models
from Result_Analysis.models import Teacher

class Test(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    exam_time = models.DateTimeField()
    exam_duration = models.IntegerField(default=0)
    total_marks = models.IntegerField()



class QuestionSet(models.Model):
    question_list = models.OneToOneField(Test, on_delete=models.CASCADE)

class Question(models.Model):
    question = models.ForeignKey(QuestionSet, on_delete=models.CASCADE)
    text = models.TextField()
    option1 = models.CharField(max_length=200,
                               verbose_name='option1',
                               blank=False)
    option2 = models.CharField(max_length=200,
                               verbose_name='option2',
                               blank=False)
    option3 = models.CharField(max_length=200,
                               verbose_name='option3',
                               blank=False)
    option4 = models.CharField(max_length=200,
                               verbose_name='option4',
                               blank=False)

    OPTIONS = (
        ('1','option1'),
        ('2','option2'),
        ('3','option3'),
        ('4','option4'),
    )

    answer = models.CharField(max_length=200, choices=OPTIONS)
    mark = models.IntegerField()

    def __str__(self):
        return self.text

# @receiver(pre_save, sender=Question)
# def pre_save_connection(sender, **kwargs):
#     kwargs['instance'].question =


