from django.urls import reverse
from rest_framework.test import APITestCase

from apps.books.models import Narratives, NarrativesAudio
from apps.quran.models import Qari
from apps.users.models import User


class FavouriteQariNarrativeListViewTestCase(APITestCase):
    def setUp(self):
        self.user = self.setup_user()
        self.client.force_authenticate(user=self.user)
        self.qari = Qari.objects.create(full_name="test", image="test", juz_count=1)
        self.narrative = Narratives.objects.create(title="Test Narrative", image="image.png", qari=self.qari)
        self.narrative_audio = NarrativesAudio.objects.create(
            narrative=self.narrative, title="Test Audio 2", audio="audio2.mp3", order=2
        )

    def setup_user(self):
        return User.objects.create_user(
            username="test",
            email="dilbarov@gmail.com",
            password="test",
        )

    def test_favourite_qari_narrative_list(self):
        url = reverse("users:AddRemoveFavouriteQari")
        response = self.client.post(url, {"qari": self.qari.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["is_favourite"], True)

        url = reverse("users:FavouriteQariNarrative")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)
