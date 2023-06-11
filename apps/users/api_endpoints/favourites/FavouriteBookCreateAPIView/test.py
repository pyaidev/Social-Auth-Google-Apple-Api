from django.urls import reverse
from rest_framework.test import APITestCase

from apps.books.models import Book
from apps.users.models import User


class FavouriteBookCreateViewTestCase(APITestCase):
    def setUp(self):
        self.user = self.setup_user()
        self.client.force_authenticate(user=self.user)
        self.book = Book.objects.create(
            title="Test Book", author="Test Author", description="Test Description", image="image.png", file="file.pdf"
        )
        self.url = reverse("users:AddRemoveFavouriteBook")

    def setup_user(self):
        return User.objects.create_user(
            username="test",
            email="dilbarov@gmail.com",
            password="test",
        )

    def test_add_favourite_book(self):
        response = self.client.post(self.url, {"book": self.book.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["is_favourite"], True)
