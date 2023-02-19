from django.test import TestCase
from authentication.models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            email="cs.ttrx@gmail.com", user_name="csttrx", password="coull1515fdf"
        )
        User.objects.create_superuser(
            "coul@gmail.com", user_name="cscoul", password="godejeroien583"
        )

    def test_user_name_label(self):
        user = User.objects.get(id=1)
        user_name_label = user._meta.get_field("user_name").verbose_name
        self.assertEqual(user_name_label, "user name")

    def test_user_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field("user_name").max_length
        self.assertEqual(max_length, 50)

    def test_user_is_active_admin_superuser(self):
        user = User.objects.get(id=1)
        superuser = User.objects.get(id=2)
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_superuser)
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_admin)
        self.assertTrue(superuser.is_superuser)

    def test_user_name(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.get_short_name(), "c")
