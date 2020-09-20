from django.db import models

from projects.models import Project


class Message(models.Model):
    text = models.CharField(max_length=2000)
    url = models.CharField(max_length=300, null=True, blank=True)
    media = models.ImageField(upload_to='', null=True, blank=True, max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return str(self.id)


class WelcomeMessage(models.Model):
    message = models.OneToOneField(Message, on_delete=models.DO_NOTHING)
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='welcome_message')

    def __str__(self):
        return str(self.id)


class ConfirmMessage(models.Model):
    message = models.OneToOneField(Message, on_delete=models.DO_NOTHING)
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='confirm_message')

    def __str__(self):
        return str(self.id)
