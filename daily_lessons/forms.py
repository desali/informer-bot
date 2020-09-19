from django import forms
from django.forms import ModelForm

from daily_lessons.models import DailyLesson
from lessons.models import Lesson


class DailyLessonCreateForm(ModelForm):
    class Meta:
        model = DailyLesson
        fields = ['title', 'day', 'hour', 'project']


class DailyLessonEditForm(ModelForm):
    class Meta:
        model = DailyLesson
        fields = ['title', 'hour']
