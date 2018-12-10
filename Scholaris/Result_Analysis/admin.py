from django.contrib import admin
from .models import Student, Teacher, Course ,OTP_Verify, Task

# Register your models here.

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Task)
admin.site.register(OTP_Verify)
