import datetime
from django.test import TestCase

from Test_Designing.forms import TestCreateForm, QuestionForm
from Result_Analysis.models import Teacher
from django.contrib.auth.models import User

class ExamFormTest(TestCase):

    name = 'ASE Quiz 1'
    description = 'ASE Quiz based on gitHub'
    time = datetime.date.today()
    duration = 1

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='teacher1', email='tea@gmail.com', password='tea12345#')
        Teacher.objects.create(teacher=user)

    def setUp(self):
        pass


    def test_exam_set_time_is_in_past(self):
        time = datetime.date.today() - datetime.timedelta(days=1)
        form = TestCreateForm(data={'name': self.name, 'description': self.description, 'time': time, 'duration': 5})
        self.assertFalse(form.is_valid())

    def test_exam_duration_is_negative(self):
        self.duration = -5
        form = TestCreateForm(data={'name': self.name, 'description': self.description, 'time': self.time, 'duration': self.duration})
        self.assertFalse(form.is_valid())


class QuestionFormTest(TestCase):

    option1 = 'option1'
    option2 = 'option2'
    option3 = 'option3'
    option4 = 'option4'

    text = 'This is option text'
    mark = 2



    def test_mark_is_positive(self):
        self.mark = -5
        form = QuestionForm(data={'option1':self.option1,
                                  'option2':self.option2,
                                  'option3':self.option3,
                                  'option4':self.option4,
                                  'text':self.text,
                                  'mark':self.mark,
                                  })

        self.assertFalse(form.is_valid())






