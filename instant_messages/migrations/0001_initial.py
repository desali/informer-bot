# Generated by Django 3.1.1 on 2020-09-17 18:55

import datetime

import django.db.models.deletion
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('tmessages', '0001_initial'),
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstantMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 9, 17, 18, 55, 24, 71867, tzinfo=utc))),
                ('lesson',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instant_messages',
                                   to='lessons.lesson')),
                ('message', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tmessages.message')),
            ],
            options={
                'db_table': 'messages_instant_message',
            },
        ),
    ]
