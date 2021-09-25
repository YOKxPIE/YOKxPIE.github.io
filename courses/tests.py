from django.test import TestCase, Client

# Create your tests here.
from .models import Course, Student, Enroll

from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password



#test Models
class TestCase(TestCase):

    def setUp(self):

        course = Course.objects.create(c_code="CN000", c_name="TEST", semester=1, a_year=2564)
        course_f = Course.objects.create(c_code="CN001", c_name="TEST_full", semester=1, a_year=2564, count_stu=3)

        password = make_password('user123456')
        user = User.objects.create(username="user", password=password, email="user@example.com")

        student = Student.objects.create(user=user, First_name="userFirstname", Last_name="userLastname", email="user@example.com", student_id="6210000000")

        Enroll.objects.create(student=student, course=course)

        Group.objects.create(name="admin")
        Group.objects.create(name="student")

        group_s = Group.objects.get(name="student")
        user.groups.add(group_s)


    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)

    def test_course_exists(self):
        course_count = Course.objects.all().count()
        self.assertEqual(course_count, 2)
        self.assertNotEqual(course_count, 0)

    def test_student_exists(self):
        stu_count = Student.objects.all().count()
        self.assertEqual(stu_count, 1)
        self.assertNotEqual(stu_count, 0)

    def test_enroll_exists(self):
        enroll_count = Enroll.objects.all().count()
        self.assertEqual(enroll_count, 1)
        self.assertNotEqual(enroll_count, 0)

    def test_str_course(self):
        course = Course.objects.first()
        self.assertEqual(str(course), course.c_code +" "+ str(course.semester) +"/"+ str(course.a_year))

    def test_str_student(self):
        stu = Student.objects.first()
        self.assertEqual(str(stu), stu.student_id +": "+ stu.First_name +" "+ stu.Last_name)

    def test_str_enroll(self):
        enroll = Enroll.objects.first()
        self.assertEqual(str(enroll), str(enroll.student) +" enroll "+ str(enroll.course))

    def test_is_seat_available(self):
        course = Course.objects.first()
        self.assertTrue(course.is_seat_available())

    def test_is_seat_full(self):
        course = Course.objects.get(c_code="CN001")
        self.assertFalse(course.is_seat_available())