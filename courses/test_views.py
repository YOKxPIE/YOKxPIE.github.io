from django.test import TestCase, Client
from .models import Course, Student, Enroll
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from django.urls import reverse

from django.shortcuts import resolve_url

class ViewTestCase(TestCase):

    def setUp(self):
        self.group = Group(name="student")
        self.group.save()
        self.group = Group(name="admin")
        self.group.save()

        self.user_ad = User.objects.create_user(username="ad", email="ad@test.com", password="testad")
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        group_ad = Group.objects.get(name="admin")
        self.user_ad.groups.add(group_ad)


        group_s = Group.objects.get(name="student")
        self.user.groups.add(group_s)
        self.student = Student.objects.create(user=self.user, First_name="userFirstname", Last_name="userLastname", email="user@example.com", student_id="6210000000")


    def test_index_view_stu(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('courses:index'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/index.html', 'courses/layout.html')

    def test_index_view_ad(self):
        self.c = Client()
        self.c.login(username='ad', password='testad')
        response = self.c.get(reverse('courses:index'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/indexadmin.html', 'courses/layout.html')


    def test_indexadmin_view_stu(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('courses:indexadmin'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/index.html', 'courses/layout.html')


    def test_indexadmin_view_ad(self):
        self.c = Client()
        self.c.login(username='ad', password='testad')
        response = self.c.get(reverse('courses:indexadmin'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/indexadmin.html', 'courses/layout.html')


    def test_courses_view_stu(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('courses:courses'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/courses.html', 'courses/layout.html')


    def test_courses_view_ad(self):
        self.c = Client()
        self.c.login(username='ad', password='testad')
        response = self.c.get(reverse('courses:courses'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/indexadmin.html', 'courses/layout.html')


    def test_registration_view_stu(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('courses:registration'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/registration.html', 'courses/layout.html')


    def test_registration_view_stu_can_delete_course(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        course1 = Course.objects.create(c_code="TU00", c_name="AA", semester="0", a_year="2500", count_stu="1", max_stu="2", status=True)
        course2 = Course.objects.create(c_code="TU01", c_name="BB", semester="0", a_year="2500", count_stu="1", max_stu="2", status=True)
        enroll = Enroll.objects.create(student=self.student, course=course1)
        Enroll.objects.create(student=self.student, course=course2)

        response = self.c.post(reverse('courses:delete_course', args=(enroll.id,)), follow=True)
        enroll_all = Enroll.objects.all()
        for e in enroll_all:
            self.assertEqual(e.course, course2)

        course1_af_withdraw = Course.objects.filter(id=course1.id)
        for c in course1_af_withdraw:
            self.assertEqual(c.count_stu, 0)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/registration.html', 'courses/layout.html')


    def test_registration_view_ad(self):
        self.c = Client()
        self.c.login(username='ad', password='testad')
        response = self.c.get(reverse('courses:registration'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/indexadmin.html', 'courses/layout.html')


    def test_profile_view_stu(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('courses:profile'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/profile.html', 'courses/layout.html')


    def test_profile_view_ad(self):
        self.c = Client()
        self.c.login(username='ad', password='testad')
        response = self.c.get(reverse('courses:profile'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/indexadmin.html', 'courses/layout.html')


    def test_admincourses_view_stu(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('courses:admincourses'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/index.html', 'courses/layout.html')


    def test_admincourses_view_ad(self):
        self.c = Client()
        self.c.login(username='ad', password='testad')
        response = self.c.get(reverse('courses:admincourses'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/admincourses.html', 'courses/layout.html')


    def test_unauthenticated_view_stu(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('courses:login'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/index.html', 'courses/layout.html')


    def test_unauthenticated_view_ad(self):
        self.c = Client()
        self.c.login(username='ad', password='testad')
        response = self.c.get(reverse('courses:login'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/indexadmin.html', 'courses/layout.html')


    def test_unauthenticated_view_unauthenticated(self):
        self.c = Client()
        response = self.c.get(reverse('courses:login'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/login.html')


    def test_course_view_stu(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        course = Course.objects.create(c_code="CN000", c_name="TEST", semester=1, a_year=2564)
        response = self.c.get(reverse('courses:acourse', args=(course.id,)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/index.html', 'courses/layout.html')


    def test_course_view_ad(self):
        self.c = Client()
        self.c.login(username='ad', password='testad')
        course = Course.objects.create(c_code="CN000", c_name="TEST", semester=1, a_year=2564)
        Enroll.objects.create(student=self.student, course=course)
        response = self.c.get(reverse('courses:acourse', args=(course.id,)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/course.html', 'courses/layout.html')


    def test_logout_view_stu(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('courses:logout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/login.html')


    def test_logout_view_ad(self):
        self.c = Client()
        self.c.login(username='ad', password='testad')
        response = self.c.get(reverse('courses:logout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/login.html')


    def test_enrollCourse_view_stu_enroll(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        course = Course.objects.create(c_code="CN000", c_name="TEST", semester=1, a_year=2564)
        self.assertEqual(Enroll.objects.all().count(), 0)
        response = self.c.post(reverse('courses:enroll_course', args=(course.id,)), follow=True)
        self.assertEqual(Enroll.objects.all().count(), 1)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/registration.html', 'courses/layout.html')
        course = Course.objects.get(id=course.id)
        self.assertEqual(course.count_stu, 1)


    def test_enrollCourse_view_stu_can_not_enroll(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        course1 = Course.objects.create(c_code="TU00", c_name="AA", semester="0", a_year="2500", count_stu="0", max_stu="2", status=True)

        response = self.c.get(reverse('courses:enroll_course', args=(course1.id,)), follow=True)
        enroll = Enroll.objects.all()
        course = Course.objects.filter(id=course1.id)
        for c in course:
            self.assertEqual(c.count_stu, 0)

        self.assertEqual(enroll.count(), 0)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/courses.html', 'courses/layout.html')


    def test_enrollCourse_view_ad(self):
        self.c = Client()
        self.c.login(username='ad', password='testad')
        course = Course.objects.create(c_code="CN000", c_name="TEST", semester=1, a_year=2564)
        response = self.c.get(reverse('courses:enroll_course', args=(course.id,)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/indexadmin.html', 'courses/layout.html')


    def test_login_view_ad_succ(self):
        self.c = Client()
        response = self.c.post(reverse('courses:login'), {'username': 'ad', 'password': 'testad'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/indexadmin.html', 'courses/layout.html')


    def test_login_view_stu_succ(self):
        self.c = Client()
        response = self.c.post(reverse('courses:login'), {'username': "test", 'password': "test"}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/index.html', 'courses/layout.html')


    def test_login_view_fail(self):
        self.c = Client()
        response = self.c.post(reverse('courses:login'), {'username': "test", 'password': "test1"}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/login.html')


    def test_index_context_view_stu1(self):
        self.c = Client()
        user_2 = User.objects.create_user(username="test2", email="test2@test.com", password="test2")
        Student.objects.create(user=user_2, First_name="user2Firstname", Last_name="user2Lastname", email="user2@example.com", student_id="6210000001")
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('courses:index'), follow=True)
        self.assertEqual(response.context['student'], self.student)


    def test_index_context_view_stu2(self):
        self.c = Client()
        self.user = User.objects.create_user(username="test2", email="test2@test.com", password="test2")
        group_s = Group.objects.get(name="student")
        self.student = Student.objects.create(user=self.user, First_name="user2Firstname", Last_name="user2Lastname", email="user2@example.com", student_id="6210000001")
        self.user.groups.add(group_s)
        self.c.login(username='test2', password='test2')
        response = self.c.get(reverse('courses:index'))
        self.assertEqual(response.context['student'], self.student)


    def test_courses_context(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        Course.objects.create(c_code="TU00" ,c_name="AA" ,semester=0 ,a_year=2500 ,status=True)
        Course.objects.create(c_code="TU01" ,c_name="BB" ,semester=0 ,a_year=2500 ,status=True)
        response = self.c.get(reverse('courses:courses'))
        self.assertEqual(list(response.context['courses']), list(Course.objects.all()))


    def test_registration_context(self):
        self.c = Client()
        self.c.login(username='test', password='test')
        course1 = Course.objects.create(c_code="TU01" ,c_name="AA" ,semester="0" ,a_year="2500" ,count_stu="0" ,max_stu="2" ,status=True)
        course2 = Course.objects.create(c_code="TU00" ,c_name="AA" ,semester="0" ,a_year="2500" ,count_stu="0" ,max_stu="2" ,status=True)
        Enroll.objects.create(student=self.student, course=course1)
        Enroll.objects.create(student=self.student, course=course2)
        response = self.c.get(reverse('courses:registration'))
        self.assertEqual(list(response.context['courses']), list(self.student.enroll_set.all()))
        self.assertEqual(response.context['courses'].count(), self.student.enroll_set.all().count())


    def test_admincourses_context(self):
        self.c = Client()
        self.c.login(username='ad', password='testad')
        Course.objects.create(c_code="TU01" ,c_name="AA" ,semester="0" ,a_year="2500" ,count_stu="0" ,max_stu="2" ,status=True)
        Course.objects.create(c_code="TU00" ,c_name="AA" ,semester="0" ,a_year="2500" ,count_stu="0" ,max_stu="2" ,status=True)
        response = self.c.get(reverse('courses:admincourses'))
        self.assertEqual(list(response.context['courses']), list(Course.objects.all()))


    def test_course_context(self):
        self.c = Client()
        self.c.login(username='ad', password='testad')

        course1 = Course.objects.create(c_code="TU00" ,c_name="AA" ,semester="0" ,a_year="2500" ,count_stu="0" ,max_stu="2" ,status=True)
        stu1 = Student.objects.create(First_name="userFirstname1", Last_name="userLastname1", email="user1@example.com", student_id="6210000009")
        stu2 = Student.objects.create(First_name="userFirstname2", Last_name="userLastname2", email="user2@example.com", student_id="6210000001")
        Enroll.objects.create(student=stu1, course=course1)
        Enroll.objects.create(student=stu2, course=course1)

        response = self.c.get(reverse('courses:acourse'  ,args=(course1.id,)))
        enroll = Enroll.objects.filter(course=course1)
        list_students_in_course = []
        for stu in enroll:
    	    list_students_in_course.append(stu.student)

        self.assertEqual(response.context['course'], course1)
        self.assertEqual(list(response.context['students']) ,list_students_in_course)


