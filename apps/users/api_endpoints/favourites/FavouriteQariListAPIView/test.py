from django.urls import reverse
from rest_framework.test import APITestCase

from apps.quran.models import Qari
from apps.users.models import User


class FavouriteQariListViewTestCase(APITestCase):
    def setUp(self):
        self.user = self.setup_user()
        self.client.force_authenticate(user=self.user)
        self.qari = Qari.objects.create(full_name="test", image="test", juz_count=1, order=1)

    def setup_user(self):
        return User.objects.create_user(
            username="test",
            email="dilbarov@gmail.com",
            password="test",
        )

    def test_favourite_qari_list(self):
        add_url = reverse("users:AddRemoveFavouriteQari")
        self.client.post(add_url, {"qari": self.qari.id})
        url = reverse("users:FavouriteQariList")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
