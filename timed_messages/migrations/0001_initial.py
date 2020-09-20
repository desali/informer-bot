# Generated by Django 3.1.1 on 2020-09-20 12:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tmessages', '0001_initial'),
        ('daily_lessons', '0001_initial'),
        ('core', '0001_initial'),
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimedMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField(choices=[(1, 'Created'), (2, 'Active'), (3, 'Sent')], default=1)),
                ('daily_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='timed_messages', to='daily_lessons.dailylesson')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='timed_messages', to='lessons.lesson')),
                ('message', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tmessages.message')),
                ('timing', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.timing')),
            ],
            options={
                'db_table': 'timed_messages_timed_message',
            },
        ),
    ]
