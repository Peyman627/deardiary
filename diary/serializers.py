# from django.contrib.auth.models import User, Group
from rest_framework import serializers

# from .models import Diary, DiaryImage
from .models import Diary

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'groups')

# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('id', 'name')


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ('id', 'title', 'content', 'date', 'mood')
