# Generated by Django 3.1.1 on 2020-09-21 20:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instant_messages', '0004_auto_20200921_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instantmessage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 21, 20, 24, 10, 327326)),
        ),
    ]
