from django.test import TestCase
try:
    from django.core.urlresolvers import reverse
except ImportError:  # django < 1.10
    from django.urls import reverse
from django.test import Client
from django_forum_app.models import Category, Forum, Topic, Post
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:  # django < 1.5
    from django.contrib.auth.models import User


class BasicTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        cat = Category.objects.create(order=1, title="General")
        forum = Forum.objects.create(title="The Beatles", slug="the-beatles", category=cat, creator=user)
        topic = Topic.objects.create(title="Which is the first album's name?", forums=forum, creator=user)
        Post.objects.create(title="My opinion", creator=user, topic=topic, body="I think is Please Please Me")

    def test_forum_index(self):
        c = Client()
        url = reverse('forum-index')
        response = c.get(url)
        self.assertEqual(response.status_code, 200)