from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'diary', views.DiaryViewSet, basename='diary')
router.register(r'users', views.UserViewSet)
router.register(r'diaryimage', views.DiaryImageViewSet)

urlpatterns = [
    path('api-auth', include('rest_framework.urls')),
    path('', include(router.urls)),
]
