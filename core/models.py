from django.db import models


class Timing(models.Model):
    title = models.CharField(max_length=200)
    minutes = models.IntegerField()

    def __str__(self):
        return self.title


class Hour(models.Model):
    title = models.CharField(max_length=200)
    hour = models.IntegerField()

    def __str__(self):
        return self.title


class Minute(models.Model):
    title = models.CharField(max_length=200)
    minute = models.IntegerField()

    def __str__(self):
        return self.title
