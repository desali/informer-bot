from django.db import models

from core.models import Hour, Minute
from projects.models import Project
from tmessages.models import Message


class DailyLesson(models.Model):
    STATUS = (
        (1, 'Created'),
        (2, 'Active'),
        (3, 'Deleted')
    )

    title = models.CharField(max_length=200)
    day = models.IntegerField()
    message = models.OneToOneField(Message, on_delete=models.CASCADE, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='daily_lessons')
    hour = models.ForeignKey(Hour, on_delete=models.DO_NOTHING)
    minute = models.ForeignKey(Minute, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "daily_lessons_daily_lesson"
