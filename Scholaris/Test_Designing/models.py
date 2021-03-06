from django.db import models
from Result_Analysis.models import Teacher, Student


class Test(models.Model):
    name = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=250,null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    time = models.DateTimeField()
    duration = models.IntegerField(default=0)
    total_marks = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class QuestionSet(models.Model):
    question_list = models.OneToOneField(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_list.name

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
    mark = models.IntegerField(default=1)

    def __str__(self):
        return self.text


class StudentResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.DO_NOTHING)
    correct_ans = models.IntegerField(default=0)
    wrong_ans = models.IntegerField(default=0)
    marks = models.IntegerField(default=0)

    def  __str__(self):
        return self.student.student.username + ' - ' + self.test.name

# @receiver(pre_save, sender=Question)
# def pre_save_connection(sender, **kwargs):
#     kwargs['instance'].question =


