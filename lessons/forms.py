from django import forms

from admins.models import Admin
from lessons.models import Lesson


class LessonEditForm(forms.Form):
    model = Lesson
    fields = ['title', 'date']
