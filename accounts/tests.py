# posts/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import CustomUser


class UserTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="test_passwd",
        )

    def test_custom_user_model(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@email.com")
