from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="tester1",
            email="test123@email.com",
            password="pass123",
        )

        cls.post = Post.objects.create(
            author = cls.user,
            title = "Post Title",
            body = "This is content.",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "tester1")
        self.assertEqual(self.post.title, "Post Title")
        self.assertEqual(self.post.body, "This is content.")
        self.assertEqual(str(self.post), "Post Title")