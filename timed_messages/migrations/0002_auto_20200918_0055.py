# Generated by Django 3.1.1 on 2020-09-17 18:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('timed_messages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timedmessage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 17, 18, 55, 30, 169826, tzinfo=utc)),
        ),
    ]
