from django.db import models


class Message(models.Model):
    text = models.CharField(max_length=2000)
    url = models.CharField(max_length=300)
    media = models.CharField(max_length=300)

    def __str__(self):
        return str(self.id)
