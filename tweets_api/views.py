from rest_framework import viewsets
from .models import User, Tweet
from .serializers import UserSerializer, TweetSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all().order_by('-id')
    serializer_class = TweetSerializer
