from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Diary, DiaryImage


class DiaryInline(admin.TabularInline):
    model = Diary


class DiaryImageInline(admin.TabularInline):
    model = DiaryImage


class DiaryAdmin(admin.ModelAdmin):
    inlines = [
        DiaryImageInline,
    ]


admin.site.register(Diary, DiaryAdmin)
