from django.urls import reverse
from rest_framework.test import APITestCase

from apps.books.models import AudioBook
from apps.users.models import FavouriteAudioBook, User


class FavouriteAudioBookListViewTestCase(APITestCase):
    def setUp(self):
        self.user = self.setup_user()
        self.client.force_authenticate(user=self.user)
        self.audio_book = AudioBook.objects.create(
            title="Test Audio Book", author="Test Author", description="Test Description", image="image.png"
        )
        self.favourite_audio_book = FavouriteAudioBook.objects.create(user=self.user, audiobook=self.audio_book)
        self.url = reverse("users:FavouriteAudioBookList")

    def setup_user(self):
        return User.objects.create_user(
            username="test",
            email="dilbarov@gmail.com",
            password="test",
        )

    def test_get_favourite_audio_book_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["results"][0]["title"], "Test Audio Book")
        self.assertEqual(response.data["results"][0]["image"], "http://testserver/media/image.png")
