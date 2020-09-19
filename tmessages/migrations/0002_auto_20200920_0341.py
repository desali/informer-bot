# Generated by Django 3.1.1 on 2020-09-19 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmessages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='media',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='assets/media/'),
        ),
        migrations.AlterField(
            model_name='message',
            name='url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
