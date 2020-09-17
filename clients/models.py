from django.core.validators import RegexValidator
from django.db import models

from projects.models import Project


class Client(models.Model):
    STATUS = (
        (1, 'Active'),
        (2, 'Deleted')
    )

    chat_id = models.IntegerField(unique=True)
    status = models.IntegerField(choices=STATUS, default=1)

    phone_regex = RegexValidator(regex=r'^(7)([0-9]{10})$',
                                 message="Phone number must be entered in the format: '77077070077'. Up to 11 digits "
                                         "allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=11)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='clients')

    def __str__(self):
        return str(self.chat_id)
