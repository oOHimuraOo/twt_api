from django.test import TestCase
from tweets_api.models import User, Tweet


class TweetModelTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create(
            nome="TestUser",
            senha="TestPassword"
        )
        self.tweet = Tweet.objects.create(
            owner=self.usuario,
            post="This is a test tweet"
        )

    def test_tweet_creation(self):
        self.assertEqual(self.tweet.post, "This is a test tweet")
        self.assertEqual(self.tweet.owner, self.usuario)
        self.assertTrue(isinstance(self.tweet, Tweet))
        self.assertEqual(str(self.tweet), "Tweet by TestUser")
