from django.db import models

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

    def __str__(self):
        return self.title
