from django.urls import reverse
from rest_framework.test import APITestCase

from apps.books.models import Narratives
from apps.quran.models import Qari
from apps.users.models import User


class FavouriteNarrativeCreateViewTestCase(APITestCase):
    def setUp(self):
        self.user = self.setup_user()
        self.client.force_authenticate(user=self.user)
        self.qari = Qari.objects.create(full_name="test", image="test", juz_count=1)
        self.narrative = Narratives.objects.create(title="Test Narrative", image="image.png", qari=self.qari)

    def setup_user(self):
        return User.objects.create_user(
            username="test",
            email="dilbarov@gmail.com",
            password="test",
        )

    def test_add_favourite_narrative(self):
        url = reverse("users:AddRemoveFavouriteNarrative")
        response = self.client.post(url, {"narrative": self.narrative.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["is_favourite"], True)
