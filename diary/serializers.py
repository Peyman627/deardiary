from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Diary, DiaryImage


class UserSerializer(serializers.HyperlinkedModelSerializer):
    diaries = serializers.HyperlinkedRelatedField(view_name='diary-detail',
                                                  many=True,
                                                  queryset=Diary.objects.all())

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'diaries']


class DiarySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Diary
        fields = ('url', 'id', 'owner', 'title', 'content', 'date', 'mood',
                  'images')


class DiaryImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiaryImage
        fields = ('diary', 'image')
