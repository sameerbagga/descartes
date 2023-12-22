from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Post


# Create your tests here.
class AuthorModelTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="John Doe", email="john@example.com")

    def test_author_str_method(self):
        self.assertEqual(str(self.author), "John Doe")


class PostModelTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="John Doe", email="john@example.com")
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            pub_date="2023-01-01",
            author=self.author,
        )

    def test_post_str_method(self):
        self.assertEqual(str(self.post), "Test Post")


class AuthorAPITestCase(APITestCase):
    def setUp(self):
        self.author_data = {"name": "Jane Doe", "email": "jane@example.com"}
        self.author = Author.objects.create(**self.author_data)
        self.author_list_url = reverse("author-list")
        self.author_detail_url = reverse("author-detail", kwargs={"pk": self.author.pk})

    def test_list_authors(self):
        response = self.client.get(self.author_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Jane Doe")

    def test_retrieve_author(self):
        response = self.client.get(self.author_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Jane Doe")

    def test_create_author(self):
        new_author_data = {"name": "New Author", "email": "newauthor@example.com"}
        response = self.client.post(
            self.author_list_url, new_author_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 2)

    def test_update_author(self):
        updated_data = {"name": "Updated Doe", "email": "updated@example.com"}
        response = self.client.put(self.author_detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Doe")

    def test_delete_author(self):
        response = self.client.delete(self.author_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.count(), 0)


class PostAPITestCase(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="John Doe", email="john@example.com")
        self.post_data = {
            "title": "Test Post",
            "content": "This is a test post.",
            "pub_date": "2023-01-01",
            "author": self.author,
        }
        self.post = Post.objects.create(**self.post_data)
        self.post_list_url = reverse("post-list")
        self.post_detail_url = reverse("post-detail", kwargs={"pk": self.post.pk})

    def test_list_posts(self):
        response = self.client.get(self.post_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Post")

    def test_retrieve_post(self):
        response = self.client.get(self.post_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Post")

    def test_create_post(self):
        new_post_data = {
            "title": "New Post",
            "content": "This is a new post.",
            "pub_date": "2023-01-02",
            "author": self.author.pk,
        }
        response = self.client.post(self.post_list_url, new_post_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_update_post(self):
        updated_data = {
            "title": "Updated Post",
            "content": "This is an updated post.",
            "pub_date": "2023-01-02",
            "author": self.author.pk,
        }
        response = self.client.put(self.post_detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Post")

    def test_delete_post(self):
        response = self.client.delete(self.post_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)
