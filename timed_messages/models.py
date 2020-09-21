from django.db import models

from core.models import Timing
from daily_lessons.models import DailyLesson
from lessons.models import Lesson
from tmessages.models import Message


class LessonTimedMessage(models.Model):
    STATUS = (
        (1, 'Created'),
        (2, 'Active'),
        (3, 'Sent'),
    )

    message = models.OneToOneField(Message, on_delete=models.CASCADE, related_name='lesson_timed', null=True, blank=True)
    timing = models.ForeignKey(Timing, on_delete=models.DO_NOTHING)
    status = models.IntegerField(choices=STATUS, default=1)

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='timed_messages',
                               null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "timed_messages_lesson_timed_message"


class DailyLessonTimedMessage(models.Model):
    STATUS = (
        (1, 'Created'),
        (2, 'Active'),
        (3, 'Sent'),
    )

    message = models.OneToOneField(Message, on_delete=models.CASCADE, related_name='daily_lesson_timed', null=True, blank=True)
    timing = models.ForeignKey(Timing, on_delete=models.DO_NOTHING)
    status = models.IntegerField(choices=STATUS, default=1)

    daily_lesson = models.ForeignKey(DailyLesson, on_delete=models.CASCADE, related_name='timed_messages',
                                     null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "timed_messages_daily_lesson_timed_message"
