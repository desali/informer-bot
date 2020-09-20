# Generated by Django 3.1.1 on 2020-09-20 12:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tmessages', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstantMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('message', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tmessages.message')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instant_messages', to='projects.project')),
            ],
            options={
                'db_table': 'instant_messages_instant_message',
            },
        ),
    ]
