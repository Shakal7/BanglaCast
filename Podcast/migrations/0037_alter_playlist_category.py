# Generated by Django 5.0.3 on 2025-04-21 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Podcast', '0036_playlist_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='category',
            field=models.CharField(choices=[('education', 'Education'), ('business', 'Business'), ('story', 'Story'), ('Live', 'Live'), ('Sports', 'Sports'), ('Politics', 'Politics')], max_length=100),
        ),
    ]
