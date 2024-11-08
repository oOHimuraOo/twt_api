from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TweetViewSet

router = DefaultRouter()
router.register(r'api/usuarios', UserViewSet, basename='usuario')
router.register(r'api/tweets', TweetViewSet, basename='tweet')

urlpatterns = [
    path('', include(router.urls)),
]
