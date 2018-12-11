from django.test import TestCase
from Test_Designing.models import Test
from django.contrib.auth.models import User
from Result_Analysis.models import Teacher
from Discussion_Forum.models import Post,Comment

class ExamTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='roger',email='roger@gmail.com',password='federer@20')
        teacher = Teacher.objects.create(teacher=user)


    def setUp(self):
        pass

    def test_teacher_instance_name(self):
        get_teacher = Teacher.objects.get(id=1)
        expected_name = "{0}".format(get_teacher.teacher.username)
        self.assertEqual(expected_name, str(get_teacher))

class ForumTestClass(TestCase):

    @classmethod
    def setupTestData(cls):
        user = User.objects.create(username='roger', email='roger@gmail.com', password='federer@20')
        post1 = Post.objects.create(title='mypost', author='user', body='for_testing', tag='ASE')

    def setUp(self):
        pass

    def test_first_name_max_length(self):
        post: Post = Post.objects.get(id=2)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 150)



