from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets

from .models import Diary, DiaryImage
from .serializers import DiaryImageSerializer, DiarySerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DiaryViewSet(viewsets.ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DiaryImageViewSet(viewsets.ModelViewSet):
    queryset = DiaryImage.objects.all()
    serializer_class = DiaryImageSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
