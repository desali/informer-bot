from django import forms
from django.forms import ModelForm

from lessons.models import Lesson
from timed_messages.models import LessonTimedMessage


class LessonTimedMessageCreateForm(ModelForm):
    class Meta:
        model = LessonTimedMessage
        fields = ['lesson', 'message', 'timing']
