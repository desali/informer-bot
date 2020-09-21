from django.forms import ModelForm

from lessons.models import Lesson


class LessonCreateForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'date', 'project']


class LessonEditForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'date']
