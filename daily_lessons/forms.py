from django.forms import ModelForm

from daily_lessons.models import DailyLesson


class DailyLessonCreateForm(ModelForm):
    class Meta:
        model = DailyLesson
        fields = ['title', 'day', 'hour', 'project']


class DailyLessonEditForm(ModelForm):
    class Meta:
        model = DailyLesson
        fields = ['title', 'hour']
