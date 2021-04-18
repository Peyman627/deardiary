from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Diary


class UserSerializer(serializers.ModelSerializer):
    diaries = serializers.PrimaryKeyRelatedField(many=True,
                                                 queryset=Diary.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'diaries']


class DiarySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Diary
        fields = ('owner', 'id', 'title', 'content', 'date', 'mood', 'images')
