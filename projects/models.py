from django.db import models

from tmessages.models import Message


class Project(models.Model):
    title = models.CharField(max_length=200)
    key = models.CharField(max_length=200)
    welcome_message = models.OneToOneField(Message, on_delete=models.CASCADE, related_name='welcome_message')
    confirm_message = models.OneToOneField(Message, on_delete=models.CASCADE, related_name='confirm_message')

    def __str__(self):
        return self.title
