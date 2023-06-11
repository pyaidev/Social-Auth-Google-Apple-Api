from django.urls import reverse
from rest_framework.test import APITestCase

from apps.books.models import Book
from apps.users.models import User


class FavouriteBookListViewTestCase(APITestCase):
    def setUp(self):
        self.user = self.setup_user()
        self.client.force_authenticate(user=self.user)
        self.book = Book.objects.create(
            title="Test Book", author="Test Author", description="Test Description", image="image.png", file="file.pdf"
        )

    def setup_user(self):
        return User.objects.create_user(
            username="test",
            email="dilbarov@gmail.com",
            password="test",
        )

    def test_favourite_book_list(self):
        add_url = reverse("users:AddRemoveFavouriteBook")
        self.client.post(add_url, {"book": self.book.id})

        get_url = reverse("users:FavouriteBookList")
        response = self.client.get(get_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["results"][0]["id"], self.book.id)
        self.assertEqual(response.data["results"][0]["title"], self.book.title)
        self.assertEqual(response.data["results"][0]["image"], "http://testserver/media/image.png")
