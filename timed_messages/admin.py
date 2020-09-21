from django.contrib import admin

from timed_messages.models import LessonTimedMessage, DailyLessonTimedMessage

timed_message_models = [LessonTimedMessage, DailyLessonTimedMessage]
admin.site.register(timed_message_models)
