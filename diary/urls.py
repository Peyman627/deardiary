from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('diary/', views.DiaryList.as_view(), name='diary-list'),
    path('diary/<int:pk>', views.DiaryDetail.as_view(), name='diary-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
