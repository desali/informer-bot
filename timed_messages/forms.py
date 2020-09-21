from django.forms import ModelForm

from timed_messages.models import LessonTimedMessage, DailyLessonTimedMessage


class LessonTimedMessageCreateForm(ModelForm):
    class Meta:
        model = LessonTimedMessage
        fields = ['lesson', 'message', 'timing']


class DailyLessonTimedMessageCreateForm(ModelForm):
    class Meta:
        model = DailyLessonTimedMessage
        fields = ['daily_lesson', 'message', 'timing']
