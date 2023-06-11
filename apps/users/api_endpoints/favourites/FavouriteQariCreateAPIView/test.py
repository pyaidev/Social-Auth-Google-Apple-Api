from django.urls import reverse
from rest_framework.test import APITestCase

from apps.quran.models import Qari
from apps.users.models import User


class FavouriteQariCreateViewTestCase(APITestCase):
    def setUp(self):
        self.user = self.setup_user()
        self.client.force_authenticate(user=self.user)
        self.qari = Qari.objects.create(full_name="test", image="test", juz_count=1)

    def setup_user(self):
        return User.objects.create_user(
            username="test",
            email="dilbarov@gmail.com",
            password="test",
        )

    def test_add_favourite_qari(self):
        url = reverse("users:AddRemoveFavouriteQari")
        response = self.client.post(url, {"qari": self.qari.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["is_favourite"], True)
