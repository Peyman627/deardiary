from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('api-auth', include('rest_framework.urls')),
    path('diary/', views.DiaryList.as_view(), name='diary-list'),
    path('diary/<int:pk>', views.DiaryDetail.as_view(), name='diary-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
