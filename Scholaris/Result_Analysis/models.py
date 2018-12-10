from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return "{}".format(self.name)

class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='profile_pics',default='black2.PNG',blank='True')
    total_votes = models.IntegerField(default=0)
    course = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return "{}".format(self.student.username)


class Teacher(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='profile_pics',default='black2.PNG',blank='True')
    followers = models.ManyToManyField(Student)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.teacher.username)

class OTP_Verify(models.Model):
    name=models.CharField(max_length=50)
    otp=models.IntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.name)

class Task(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text