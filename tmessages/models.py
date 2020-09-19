from django.db import models


class Message(models.Model):
    text = models.CharField(max_length=2000)
    url = models.CharField(max_length=300, null=True, blank=True)
    media = models.ImageField(upload_to='assets/media/', null=True, blank=True, max_length=255)

    def __str__(self):
        return str(self.id)
