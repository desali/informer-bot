# Generated by Django 3.1.1 on 2020-09-17 18:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('timed_messages', '0002_auto_20200918_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timedmessage',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
