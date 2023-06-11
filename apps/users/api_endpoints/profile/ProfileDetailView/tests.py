from django.urls import reverse
from rest_framework.test import APITestCase

from apps.users.models import User


class ProfileDetailViewTestCase(APITestCase):
    def setUp(self):
        self.user = self.setup_user()
        self.client.force_authenticate(user=self.user)

    def setup_user(self):
        return User.objects.create_user(
            username="test",
            email="dilbarov@gmail.com",
            password="test",
        )

    def test_get_profile_detail(self):
        response = self.client.get(reverse("users:ProfileDetail"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["email"], "dilbarov@gmail.com")
