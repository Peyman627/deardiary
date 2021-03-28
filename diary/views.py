from rest_framework import generics

from .models import Diary
from .serializers import DiarySerializer


class DiaryList(generics.ListCreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer


class DiaryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
