from django import forms

from .models import Diary


class DiaryForm(forms.ModelForm):
    """form for creating diary model"""
    class Meta:
        model = Diary
        field = ('title', 'content', 'date', 'mood', 'image')
