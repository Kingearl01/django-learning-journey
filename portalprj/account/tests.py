from django.test import TestCase
from django.contrib.auth import  get_user_model
# Create your tests here.
class UserManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(student_id="200048402", password="foo")
        self.assertEqual(user.student_id, "200048402")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(student_id="")
        with self.assertRaises(ValueError):
            User.objects.create_user(student_id="", password='foo')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user= User.objects.create_superuser(student_id="super", password='foo')
        self.assertEqual(admin_user.student_id, "super")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(student_id="super1", password='foo', is_superuser=True)