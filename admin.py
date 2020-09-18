# pylint: disable=line-too-long

from django.contrib import admin

from .models import QuestionSet, ScheduledItem

@admin.register(QuestionSet)
class QuestionSetAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'name',)
    search_fields = ('identifier', 'name',)

@admin.register(ScheduledItem)
class ScheduledItemAdmin(admin.ModelAdmin):
    list_display = ('respondent', 'date', 'start_time', 'end_time',)
    search_fields = ('respondent',)
    list_filter = ('date', 'start_time', 'end_time', 'questions', 'respondent',)
