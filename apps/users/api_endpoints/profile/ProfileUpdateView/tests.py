from django.urls import reverse
from rest_framework.test import APITestCase

from apps.users.models import User


class ProfileUpdateViewTest(APITestCase):
    def setUp(self):
        self.user = self.setup_user()
        self.client.force_authenticate(user=self.user)

    def setup_user(self):
        return User.objects.create_user(
            username="test",
            email="dilbarov@gmail.com",
            password="test",
        )

    def test_update_profile(self):
        data = {
            "first_name": "new_name",
            "last_name": "new_surname",
        }
        response = self.client.patch(reverse("users:ProfileUpdate"), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["first_name"], "new_name")
        self.assertEqual(response.data["last_name"], "new_surname")
