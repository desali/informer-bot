from django.db import models
from django.utils import timezone

from core.models import Timing
from lessons.models import Lesson
from tmessages.models import Message


class TimedMessage(models.Model):
    STATUS = (
        (1, 'Created'),
        (2, 'Active'),
        (3, 'Sent'),
    )

    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    timing = models.ForeignKey(Timing, on_delete=models.DO_NOTHING)
    status = models.IntegerField(choices=STATUS, default=1)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='timed_messages')

    def __str__(self):
        return str(self.message)

    class Meta:
        db_table = "timed_messages_timed_message"
