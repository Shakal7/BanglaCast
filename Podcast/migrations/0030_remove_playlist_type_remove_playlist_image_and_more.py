# Generated by Django 5.0.3 on 2025-04-19 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Podcast', '0029_profile_is_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='Type',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='image',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='l_title',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='lists',
        ),
        migrations.AddField(
            model_name='playlist',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playlist',
            name='name',
            field=models.CharField(default='General', max_length=100),
        ),
    ]
