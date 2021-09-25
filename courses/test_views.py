from django.test import TestCase, Client
from .models import Course, Student, Enroll
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from django.urls import reverse

class ViewTestCase(TestCase):

    # def setUp(self):

    #     course = Course.objects.create(c_code="CN000", c_name="TEST", semester=1, a_year=2564)
    #     course_f = Course.objects.create(c_code="CN001", c_name="TEST_full", semester=1, a_year=2564, count_stu=3)

    #     password = make_password('user123456')
    #     user = User.objects.create(username="user", password=password, email="user@example.com")

    #     student = Student.objects.create(user=user, First_name="userFirstname", Last_name="userLastname", email="user@example.com", student_id="6210000000")

    #     Enroll.objects.create(student=student, course=course)



    def test_index_view_stu(self):
        c = Client()
        self.group = Group(name="student")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        group_s = Group.objects.get(name="student")
        self.student = Student.objects.create(user=self.user, First_name="userFirstname", Last_name="userLastname", email="user@example.com", student_id="6210000000")
        self.user.groups.add(group_s)
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('courses:index'))
        self.assertEqual(response.status_code, 200) #ไปถูกที่=200

    def test_index_view_ad(self):
        c = Client()
        self.group = Group(name="admin")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="ad", email="ad@test.com", password="testad")
        group_ad = Group.objects.get(name="admin")
        self.user.groups.add(group_ad)
        self.c.login(username='ad', password='testad')
        response = self.c.get(reverse('courses:index'))
        self.assertEqual(response.status_code, 302) #โดนย้ายปลายทางที่มีpageรองรับ302



    def test_indexadmin_view_stu(self):
        c = Client()
        self.group = Group(name="student")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        group_s = Group.objects.get(name="student")
        self.student = Student.objects.create(user=self.user, First_name="userFirstname", Last_name="userLastname", email="user@example.com", student_id="6210000000")
        self.user.groups.add(group_s)
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('courses:indexadmin'))
        self.assertEqual(response.status_code, 302) #โดนย้ายปลายทางที่มีpageรองรับ302

    def test_indexadmin_view_ad(self):
        c = Client()
        self.group = Group(name="admin")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="ad", email="ad@test.com", password="testad")
        group_ad = Group.objects.get(name="admin")
        self.user.groups.add(group_ad)
        self.c.login(username='ad', password='testad')
        response = self.c.get(reverse('courses:indexadmin'))
        self.assertEqual(response.status_code, 200) #ไปถูกที่=200



    def test_courses_view_stu(self):
        c = Client()
        self.group = Group(name="student")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        group_s = Group.objects.get(name="student")
        self.student = Student.objects.create(user=self.user, First_name="userFirstname", Last_name="userLastname", email="user@example.com", student_id="6210000000")
        self.user.groups.add(group_s)
        self.c.login(username='test', password='test')
        course = Course.objects.create(c_code="CN000", c_name="TEST", semester=1, a_year=2564)
        self.enroll = Enroll.objects.create(student=self.student, course=course)
        response = self.c.get(reverse('courses:courses'))
        self.assertEqual(response.status_code, 200) #ไปถูกที่=200

    def test_courses_view_ad(self):
        c = Client()
        self.group = Group(name="admin")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="ad", email="ad@test.com", password="testad")
        group_ad = Group.objects.get(name="admin")
        self.user.groups.add(group_ad)
        self.c.login(username='ad', password='testad')
        response = self.c.get(reverse('courses:courses'))
        self.assertEqual(response.status_code, 302) #โดนย้ายปลายทางที่มีpageรองรับ302



    def test_registration_view_stu(self):
        c = Client()
        self.group = Group(name="student")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        group_s = Group.objects.get(name="student")
        self.student = Student.objects.create(user=self.user, First_name="userFirstname", Last_name="userLastname", email="user@example.com", student_id="6210000000")
        self.user.groups.add(group_s)
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('courses:registration'))
        self.assertEqual(response.status_code, 200) #ไปถูกที่=200

    def test_registration_view_ad(self):
        c = Client()
        self.group = Group(name="admin")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="ad", email="ad@test.com", password="testad")
        group_ad = Group.objects.get(name="admin")
        self.user.groups.add(group_ad)
        self.c.login(username='ad', password='testad')
        response = self.c.get(reverse('courses:registration'))
        self.assertEqual(response.status_code, 302) #โดนย้ายปลายทางที่มีpageรองรับ302



    def test_profile_view_stu(self):
        c = Client()
        self.group = Group(name="student")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        group_s = Group.objects.get(name="student")
        self.student = Student.objects.create(user=self.user, First_name="userFirstname", Last_name="userLastname", email="user@example.com", student_id="6210000000")
        self.user.groups.add(group_s)
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('courses:profile'))
        self.assertEqual(response.status_code, 200) #ไปถูกที่=200

    def test_profile_view_ad(self):
        c = Client()
        self.group = Group(name="admin")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="ad", email="ad@test.com", password="testad")
        group_ad = Group.objects.get(name="admin")
        self.user.groups.add(group_ad)
        self.c.login(username='ad', password='testad')
        response = self.c.get(reverse('courses:profile'))
        self.assertEqual(response.status_code, 302) #โดนย้ายปลายทางที่มีpageรองรับ302



    def test_admincourses_view_stu(self):
        c = Client()
        self.group = Group(name="student")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        group_s = Group.objects.get(name="student")
        self.student = Student.objects.create(user=self.user, First_name="userFirstname", Last_name="userLastname", email="user@example.com", student_id="6210000000")
        self.user.groups.add(group_s)
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('courses:admincourses'))
        self.assertEqual(response.status_code, 302) #โดนย้ายปลายทางที่มีpageรองรับ302

    def test_admincourses_view_ad(self):
        c = Client()
        self.group = Group(name="admin")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="ad", email="ad@test.com", password="testad")
        group_ad = Group.objects.get(name="admin")
        self.user.groups.add(group_ad)
        self.c.login(username='ad', password='testad')
        response = self.c.get(reverse('courses:admincourses'))
        self.assertEqual(response.status_code, 200) #ไปถูกที่=200



    def test_unauthenticated_view_stu(self):
        c = Client()
        self.group = Group(name="student")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        group_s = Group.objects.get(name="student")
        self.student = Student.objects.create(user=self.user, First_name="userFirstname", Last_name="userLastname", email="user@example.com", student_id="6210000000")
        self.user.groups.add(group_s)
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('courses:login'))
        self.assertEqual(response.status_code, 302) #โดนย้ายปลายทางที่มีpageรองรับ302

    def test_unauthenticated_view_ad(self):
        c = Client()
        self.group = Group(name="admin")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="ad", email="ad@test.com", password="testad")
        group_ad = Group.objects.get(name="admin")
        self.user.groups.add(group_ad)
        self.c.login(username='ad', password='testad')
        response = self.c.get(reverse('courses:login'))
        self.assertEqual(response.status_code, 302) #โดนย้ายปลายทางที่มีpageรองรับ302

    def test_unauthenticated_view_unauthenticated(self):
        c = Client()
        self.c = Client()
        response = self.c.get(reverse('courses:login'))
        self.assertEqual(response.status_code, 200) #ไปถูกที่=200



    def test_course_view_stu(self):
        c = Client()
        self.group = Group(name="student")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        group_s = Group.objects.get(name="student")
        self.student = Student.objects.create(user=self.user, First_name="userFirstname", Last_name="userLastname", email="user@example.com", student_id="6210000000")
        self.user.groups.add(group_s)
        self.c.login(username='test', password='test')
        course = Course.objects.create(c_code="CN000", c_name="TEST", semester=1, a_year=2564)
        response = self.c.get(reverse('courses:acourse', args=(course.id,)))
        self.assertEqual(response.status_code, 302) #โดนย้ายปลายทางที่มีpageรองรับ302

    def test_course_view_ad(self):
        c = Client()
        self.group = Group(name="admin")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="ad", email="ad@test.com", password="testad")
        group_ad = Group.objects.get(name="admin")
        self.user.groups.add(group_ad)
        self.c.login(username='ad', password='testad')
        user = User.objects.create_user(username="test", email="test@test.com", password="test")
        stu = Student.objects.create(user=user, First_name="userFirstname", Last_name="userLastname", email="user@example.com", student_id="6210000000")
        course = Course.objects.create(c_code="CN000", c_name="TEST", semester=1, a_year=2564)
        Enroll.objects.create(student=stu, course=course)
        response = self.c.get(reverse('courses:acourse', args=(course.id,)))
        self.assertEqual(response.status_code, 200) #ไปถูกที่=200



    def test_logout_view_stu(self):
        c = Client()
        self.group = Group(name="student")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        group_s = Group.objects.get(name="student")
        self.student = Student.objects.create(user=self.user, First_name="userFirstname", Last_name="userLastname", email="user@example.com", student_id="6210000000")
        self.user.groups.add(group_s)
        self.c.login(username='test', password='test')
        response = self.c.get(reverse('courses:logout'))
        self.assertEqual(response.status_code, 302) #โดนย้ายปลายทางที่มีpageรองรับ302

    def test_logout_view_ad(self):
        c = Client()
        self.group = Group(name="admin")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="ad", email="ad@test.com", password="testad")
        group_ad = Group.objects.get(name="admin")
        self.user.groups.add(group_ad)
        self.c.login(username='ad', password='testad')
        response = self.c.get(reverse('courses:logout'))
        self.assertEqual(response.status_code, 302) #โดนย้ายปลายทางที่มีpageรองรับ302



    def test_enrollCourse_view_stu_enroll(self):
        c = Client()
        self.group = Group(name="student")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        group_s = Group.objects.get(name="student")
        self.student = Student.objects.create(user=self.user, First_name="userFirstname", Last_name="userLastname", email="user@example.com", student_id="6210000000")
        self.user.groups.add(group_s)
        self.c.login(username='test', password='test')
        course = Course.objects.create(c_code="CN000", c_name="TEST", semester=1, a_year=2564)
        self.assertEqual(Enroll.objects.all().count(), 0) #studentก่อนกดปุ่มenroll
        response = self.c.post(reverse('courses:enroll_course', args=(course.id,)))
        self.assertEqual(Enroll.objects.all().count(), 1) #studentกดปุ่มenroll มีobject enrollเกิดมาอันนึง
        self.assertEqual(response.status_code, 302) #โดนย้ายปลายทางที่มีpageรองรับ302 โดนredirect('courses:registration')

    def test_enrollCourse_view_stu(self):
        c = Client()
        self.group = Group(name="student")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        group_s = Group.objects.get(name="student")
        self.student = Student.objects.create(user=self.user, First_name="userFirstname", Last_name="userLastname", email="user@example.com", student_id="6210000000")
        self.user.groups.add(group_s)
        self.c.login(username='test', password='test')
        course = Course.objects.create(c_code="CN000", c_name="TEST", semester=1, a_year=2564)
        response = self.c.get(reverse('courses:enroll_course', args=(course.id,)))
        self.assertEqual(Enroll.objects.all().count(), 0) #studentไม่กดปุ่มenroll ไม่มีobject enrollเกิดขึ้น
        self.assertEqual(response.status_code, 302) #โดนย้ายปลายทางที่มีpageรองรับ302 โดนredirect('courses:registration')

    def test_enrollCourse_view_ad(self):
        c = Client()
        self.group = Group(name="admin")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="ad", email="ad@test.com", password="testad")
        group_ad = Group.objects.get(name="admin")
        self.user.groups.add(group_ad)
        self.c.login(username='ad', password='testad')
        course = Course.objects.create(c_code="CN000", c_name="TEST", semester=1, a_year=2564)
        response = self.c.get(reverse('courses:enroll_course', args=(course.id,)))
        self.assertEqual(response.status_code, 302) #โดนย้ายปลายทางที่มีpageรองรับ302 โดน redirect('courses:indexadmin')


# ========================ตรงนี้ลองแล้วยัง fail อยู่==============================
    def test_deleteCourse_view_stu_w(self):
        c = Client()
        self.group = Group(name="student")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        group_s = Group.objects.get(name="student")
        self.student = Student.objects.create(user=self.user, First_name="userFirstname", Last_name="userLastname", email="user@example.com", student_id="6210000000")
        self.user.groups.add(group_s)
        self.c.login(username='test', password='test')
        course = Course.objects.create(c_code="CN000", c_name="TEST", semester=1, a_year=2564)
        en = Enroll.objects.create(student=self.student, course=course)
        self.assertEqual(Enroll.objects.all().count(), 1) #studentก่อนกดปุ่มwithdraw
        response = self.c.post(reverse('courses:delete_course', args=(en.id,)))
        self.assertEqual(Enroll.objects.all().count(), 0) #studentกดปุ่มwithdraw
        self.assertEqual(response.status_code, 302) #โดนย้ายปลายทางที่มีpageรองรับ302 โดนredirect('courses:registration')

    # def test_deleteCourse_view_stu(self):
    #     c = Client()
    #     self.group = Group(name="student")
    #     self.group.save()
    #     self.c = Client()
    #     self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
    #     group_s = Group.objects.get(name="student")
    #     self.student = Student.objects.create(user=self.user, First_name="userFirstname", Last_name="userLastname", email="user@example.com", student_id="6210000000")
    #     self.user.groups.add(group_s)
    #     self.c.login(username='test', password='test')
    #     course = Course.objects.create(c_code="CN000", c_name="TEST", semester=1, a_year=2564)
    #     en = Enroll.objects.create(student=self.student, course=course)
    #     self.assertEqual(Enroll.objects.all().count(), 1)
    #     response = self.c.get(reverse('courses:delete_course', args=(en.id,)))
    #     self.assertEqual(Enroll.objects.all().count(), 1) #studentไม่กดปุ่มwithdraw
    #     self.assertEqual(response.status_code, 302) #โดนย้ายปลายทางที่มีpageรองรับ302 โดนredirect('courses:registration')

    # def test_deleteCourse_view_ad(self):
    #     c = Client()
    #     self.group = Group(name="admin")
    #     self.group.save()
    #     self.c = Client()
    #     self.user = User.objects.create_user(username="ad", email="ad@test.com", password="testad")
    #     group_ad = Group.objects.get(name="admin")
    #     self.user.groups.add(group_ad)
    #     self.c.login(username='ad', password='testad')
    #     course = Course.objects.create(c_code="CN000", c_name="TEST", semester=1, a_year=2564)
    #     response = self.c.get(reverse('courses:delete_course', args=(course.id,)))
    #     self.assertEqual(response.status_code, 302) #โดนย้ายปลายทางที่มีpageรองรับ302 โดน redirect('courses:indexadmin')
# ========================ตรงนี้ลองแล้วยัง fail อยู่==============================



    def test_login_view_stu_succ(self):
        c = Client()
        self.group = Group(name="student")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        group_s = Group.objects.get(name="student")
        self.student = Student.objects.create(user=self.user, First_name="userFirstname", Last_name="userLastname", email="user@example.com", student_id="6210000000")
        self.user.groups.add(group_s)
        response = self.c.post(reverse('courses:login'), {'username': "test", 'password': "test"})
        self.assertEqual(response.status_code, 302) #โดนย้ายปลายทางที่มีpageรองรับ302

    def test_login_view_ad_succ(self):
        c = Client()
        self.group = Group(name="admin")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="ad", email="ad@test.com", password="testad")
        group_ad = Group.objects.get(name="admin")
        self.user.groups.add(group_ad)
        response = self.c.post(reverse('courses:login'), {'username': 'ad', 'password': 'testad'})
        self.assertEqual(response.status_code, 302) #โดนย้ายปลายทางที่มีpageรองรับ302

    def test_login_view_fail(self):
        c = Client()
        self.group = Group(name="student")
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")
        group_s = Group.objects.get(name="student")
        self.student = Student.objects.create(user=self.user, First_name="userFirstname", Last_name="userLastname", email="user@example.com", student_id="6210000000")
        self.user.groups.add(group_s)
        response = self.c.post(reverse('courses:login'), {'username': "test", 'password': "test1"})
        self.assertEqual(response.status_code, 200) #login ไม่สำเร็จ(รหัสผิด) จึงอยู่หน้าเดิมให้ใส่รหัสใหม่