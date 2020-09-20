# Generated by Django 3.1.1 on 2020-09-20 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tmessages', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('status', models.IntegerField(choices=[(1, 'Created'), (2, 'Active'), (3, 'Passed'), (4, 'Deleted')], default=1)),
                ('message', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tmessages.message')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='projects.project')),
            ],
        ),
    ]
