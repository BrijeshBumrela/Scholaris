
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)


    def __str__(self):
        return "{}".format(self.student.username)


class Teacher(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)


    def __str__(self):
        return '{}'.format(self.teacher.username)


