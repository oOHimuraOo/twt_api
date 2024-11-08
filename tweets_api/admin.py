from django.contrib import admin
from .models import User, Tweet


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'logged_in')


@admin.register(Tweet)
class TweetModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'post', 'image')
