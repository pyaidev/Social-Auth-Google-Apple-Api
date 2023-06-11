from django.urls import reverse
from rest_framework.test import APITestCase

from apps.books.models import AudioBook
from apps.users.models import User


class FavouriteAudioBookCreateViewTestCase(APITestCase):
    def setUp(self):
        self.user = self.setup_user()
        self.client.force_authenticate(user=self.user)
        self.audio_book = AudioBook.objects.create(
            title="Test Audio Book", author="Test Author", description="Test Description", image="image.png"
        )
        self.url = reverse("users:AddRemoveFavouriteAudioBook")

    def setup_user(self):
        return User.objects.create_user(
            username="test",
            email="dilbarov@gmail.com",
            password="test",
        )

    def test_add_favourite_audio_book(self):
        response = self.client.post(self.url, {"audiobook": self.audio_book.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["is_favourite"], True)
