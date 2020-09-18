from django.db import models
from django.utils import timezone

from lessons.models import Lesson
from tmessages.models import Message


class InstantMessage(models.Model):
    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='instant_messages')

    def __str__(self):
        return str(self.message)

    class Meta:
        db_table = "instant_messages_instant_message"
