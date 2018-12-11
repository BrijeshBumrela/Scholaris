from django.test import TestCase
import datetime
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from Result_Analysis.models import Student, Teacher
from Test_Designing.models import Test, QuestionSet, Question
from django.contrib.auth.models import User
from Discussion_Forum.models import *

# class HomePageViewTest(TestCase):
#
#     def test_url_exist_at_desired_location(self):
#         login = self.client.login(username='rogerhihi', password='federer12345')
#         response = self.client.get('/')
#
#         self.assertEqual(response.status_code, 200)


#
# class ExamResultTest(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         user = User.objects.create(username='roger',email='roger@gmail.com',password='federer@20')
#         user.save()
#         teacher = Teacher.objects.create(teacher=user)
#         teacher.save()
#         test = Test.objects.create(name='ASE Quiz',
#                                    description='ASE Quiz on gitHub',
#                                    teacher=teacher,
#                                    time=datetime.date.today(),
#                                    duration=5,
#                                    total_marks=10)
#
#     def exam_check_if_logged_in(self):
#         login = self.client.login(username='roger', password='federer@20')
#         response = self.client.get(reverse(''))


class ListAllTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='rogerfederer',email='roger@gmail.com',password='roger1234')
        teacher = Teacher.objects.create(teacher=user)
        Test.objects.create(name = 'ASE QUIZ',
                                    description = 'ASE Quiz on git',
                                    teacher = teacher,
                                    time = datetime.date.today(),
                                    duration = 5,
                                    total_marks = 15
                                  )

        student = User.objects.create(username='student1',email='student@gmail.com',password='student1234')
        Student.objects.create(student=student)


    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('exam:list_all_test'))
        self.assertRedirects(response, '/login/?next=/test/list_all_test/')


    # def test_redirect_to_error_page_if_teacher(self):
    #     login = self.client.login(username='rogerfederer',password='roger1234')
    #     response = self.client.get(reverse('exam:list_all_test'))
    #     self.assertRedirects(response, '/test/error/?next=/test/list_all_test/')


    def redirect_to_list_if_student(self):
        self.client.login(username='student1', password='student1234')
        response = self.client.get(reverse('exam:list_all_test'))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(str(response.context['user']), 'student1')

        self.assertTemplateUsed(response, 'Test_Designing/test_list.html')


class PostlistViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create(username='roger', email='roger@gmail.com', password='federer@20')

        number_of_posts = 14

        for post_id in range(number_of_posts):
            Post.objects.create(title='mypost{post_id}',
                                slug='mypost{post_id}',
                                author=user1,
                                body='for_testing{post_id}',
                                tag='ASE',
                                status='Published')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/forum/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('forum:forum-post-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('forum:forum-post-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Discussion_Forum/post_view.html')











