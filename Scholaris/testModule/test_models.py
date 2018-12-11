from django.test import TestCase
from Test_Designing.models import Test
from django.contrib.auth.models import User
from Result_Analysis.models import Teacher
from Discussion_Forum.models import *

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
    def setUpTestData(cls):
        user1 = User.objects.create(username='roger', email='roger@gmail.com', password='federer@20')
        User.objects.create(username='roger1', email='roger1@gmail.com', password='federer@120')


        Post.objects.create(title='mypost',slug='mypost', author=user1, body='for_testing', tag='ASE', status='Published')
        Post.objects.create(title='my post', author=user1, body='for_testing', tag='ASE', status='Published')


    def setUp(self):
        pass

    def test_first_name_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 150)

    def test_check_slug(self):
        post = Post.objects.get(id=2)
        self.assertEquals(post.slug, 'my-post')

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        slug = post.slug
        slug = str(slug)
        self.assertEquals(post.get_absolute_url(), '/forum/question/1/'+slug+'/')

    def test_totalupvotes(self):
        post = Post.objects.get(id=1)
        self.assertEquals(post.total_upvotes(), 0)



