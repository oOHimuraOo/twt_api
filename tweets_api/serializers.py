from rest_framework import serializers
from .models import User, Tweet


class UserSerializer(serializers.ModelSerializer):
    tweets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'nome', 'senha', 'profile', 'logged_in', 'tweets']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class TweetSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.nome', read_only=True)

    class Meta:
        model = Tweet
        fields = ['id', 'owner', 'owner_name', 'image', 'post', 'data_postagem', 'hora_postagem']

