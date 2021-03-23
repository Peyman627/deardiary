from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('diary/', views.diary_list, name='diary-list'),
    path('diary/<int:pk>', views.diary_detail, name='diary-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)