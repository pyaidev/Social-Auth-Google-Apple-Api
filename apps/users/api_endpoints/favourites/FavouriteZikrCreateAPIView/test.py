from django.urls import reverse
from rest_framework.test import APITestCase

from apps.users.models import User
from apps.zikr.models import Category, Zikr


class FavouriteZikrCreateViewTestCase(APITestCase):
    def setUp(self):
        self.user = self.setup_user()
        self.client.force_authenticate(user=self.user)
        self.zikr_category = Category.objects.create(title="test", logo="test.png", order=1)
        self.zikr = Zikr.objects.create(
            title="test",
            category=self.zikr_category,
            arabic="test",
            transliteration="test",
            translation="test",
            audio="test.mp3",
            description="test",
            order=1,
        )

    def setup_user(self):
        return User.objects.create_user(
            username="test",
            email="dilbarov@gmail.com",
            password="test",
        )

    def test_add_favourite_zikr(self):
        url = reverse("users:AddRemoveFavouriteZikr")
        response = self.client.post(url, {"zikr": self.zikr.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["is_favourite"], True)
