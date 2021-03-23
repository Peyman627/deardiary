from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Diary
from .serializers import DiarySerializer


@api_view(['GET', 'POST'])
def diary_list(request, format=None):
    """
    list all diary enteries
    """
    if request.method == 'GET':
        diary_enteries = Diary.objects.all()
        serializer = DiarySerializer(diary_enteries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DiarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def diary_detail(request, pk, format=None):
    """
    retrieve, update or delete a diary entery
    """
    try:
        diary_entery = Diary.objects.get(pk=pk)
    except Diary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DiarySerializer(diary_entery)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DiarySerializer(diary_entery, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        diary_entery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
