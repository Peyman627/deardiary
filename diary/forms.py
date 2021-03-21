from django import forms

from .models import Diary, DiaryImage


class DiaryForm(forms.ModelForm):
    """form for creating diary model"""
    class Meta:
        model = Diary
        fields = ('title', 'content', 'date', 'mood')


class DiaryImageForm(forms.ModelForm):
    """form for creating diaryimage model"""
    class Meta:
        model = DiaryImage
        fields = ('diary', 'image')
