from rest_framework.test import APITestCase
from rest_framework import status
from tweets_api.models import User, Tweet


class TweetAPITest(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create(nome="TestUser", senha="TestPassword")

    def test_create_tweet(self):
        data = {
            "owner": self.usuario.id,
            "post": "This is a new tweet"
        }
        response = self.client.post('/api/tweets/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tweet.objects.count(), 1)
        self.assertEqual(Tweet.objects.get().post, "This is a new tweet")

    def test_get_tweet_list(self):
        Tweet.objects.create(owner=self.usuario, post="First tweet")
        response = self.client.get('/api/tweets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
