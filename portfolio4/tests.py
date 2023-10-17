from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from portfolio4.models import Post

class LikePostViewTest(TestCase):
    def setUp(self):
        # Create a user and a post
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.post = Post.objects.create(
            author=self.user,
            heading='Test Post',
            content='Test content',
            slug='test-post'
        )

    def test_like_post_authenticated_user(self):
        # Log in the user
        self.client.login(username='testuser', password='password123')

        # Send a POST request to like the post
        response = self.client.post(reverse('like_post', kwargs={'slug': self.post.slug}))

        # Check that the response is a redirect
        self.assertEqual(response.status_code, 302)

        # Check that the post is liked by the user
        self.assertTrue(self.post.likes.filter(id=self.user.id).exists())