from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets

from .models import Diary, DiaryImage
from .serializers import DiaryImageSerializer, DiarySerializer, UserSerializer
from .permissions import IsOwner


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DiaryViewSet(viewsets.ModelViewSet):
    serializer_class = DiarySerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        This view should return a list of all the
        diary enteries by the user
        """
        user = self.request.user
        return Diary.objects.filter(owner=user)


class DiaryImageViewSet(viewsets.ModelViewSet):
    queryset = DiaryImage.objects.all()
    serializer_class = DiaryImageSerializer
    permission_classes = [permissions.IsAuthenticated]
