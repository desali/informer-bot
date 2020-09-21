from django.db import models

from core.models import Hour, Minute
from projects.models import Project
from tmessages.models import Message


class Lesson(models.Model):
    STATUS = (
        (1, 'Created'),
        (2, 'Active'),
        (3, 'Passed'),
        (4, 'Deleted')
    )

    title = models.CharField(max_length=200)
    date = models.DateField()
    message = models.OneToOneField(Message, on_delete=models.CASCADE, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='lessons')
    hour = models.ForeignKey(Hour, on_delete=models.DO_NOTHING)
    minute = models.ForeignKey(Minute, on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.title
