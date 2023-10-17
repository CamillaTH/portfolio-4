from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from portfolio4.models import Post, Comment

class LikePostViewTest(TestCase):
    '''Like post tests'''
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

    def test_like_post_unauthenticated_user(self):
        # Logout the user
        self.client.logout()

        # Get the CSRF token
        response = self.client.get(reverse('like_post', kwargs={'slug': self.post.slug}))
        csrf_token = response.cookies['csrftoken'].value if 'csrftoken' in response.cookies else ''

        # Send a POST request to like the post (unauthenticated user)
        response = self.client.post(
            reverse('like_post', kwargs={'slug': self.post.slug}),
            HTTP_X_CSRFTOKEN=csrf_token
        )

        # Check that the response is a redirect to the login page
        self.assertEqual(response.status_code, 302)

        # Check that the post is not liked
        self.assertFalse(self.post.likes.filter(id=self.user.id).exists())

class LikeCommentViewTest(TestCase):
    '''Like comment tests'''
    def setUp(self):
        # Create a user, a post, and a comment
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.post = Post.objects.create(
            author=self.user,
            heading='Test Post',
            content='Test content',
            slug='test-post'
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='Test comment content',
            slug='test-comment'
        )

    def test_like_comment_authenticated_user(self):
        # Log in the user
        self.client.login(username='testuser', password='password123')

        # Send a POST request to like the comment
        response = self.client.post(reverse('like_comment', kwargs={'slug': self.comment.slug}))

        # Check that the response is a redirect
        self.assertEqual(response.status_code, 302)

        # Check that the comment is liked by the user
        self.assertTrue(self.comment.likes.filter(id=self.user.id).exists())

    def test_like_comment_unauthenticated_user(self):
        # Logout the user
        self.client.logout()

        response = self.client.get(reverse('like_comment', kwargs={'slug': self.post.slug}))
        csrf_token = response.cookies['csrftoken'].value if 'csrftoken' in response.cookies else ''

        # Send a POST request to like the post (unauthenticated user)
        response = self.client.post(
            reverse('like_comment', kwargs={'slug': self.post.slug}),
            HTTP_X_CSRFTOKEN=csrf_token
        )

        # Check that the response is a redirect to the login page
        self.assertEqual(response.status_code, 302)

        # Check that the post is not liked
        self.assertFalse(self.post.likes.filter(id=self.user.id).exists())

class CreatePostViewTest(TestCase):
    '''test for create post'''

    def test_create_post_view_uses_correct_template(self):
        response = self.client.get(reverse('create_post')) 
        self.assertTemplateUsed(response, 'create_post.html')

    #Todo create more tests for create post