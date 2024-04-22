from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Episode(models.Model):
    Title = models.CharField(max_length=200)
    Artist = models.CharField(max_length=200, blank=True, null=True)
    Type = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    audio_files = models.FileField(upload_to='images',  blank=True, null=True)


    def __str__(self):
        return self.Title


class Creator(models.Model):
    Title = models.CharField(max_length=200)
    # Duration = models.PositiveIntegerField()
    Like = models.IntegerField(blank=True, null=True)
    Share = models.IntegerField(blank=True, null=True)
    Download = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.Title


class Playlist(models.Model):
    l_title = models.CharField(max_length=200)
    # Type_choice = (
    #     ('Story', 'Story'),
    #     ('Business', 'Business'),
    #     ('Sports', 'Sports'),
    #     ('Education', 'Education'),
    # )
    Type = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.l_title


# class Audio(models.Model):
#     title = models.TextField()
#     artist = models.TextField()
#     image = models.ImageField()
#     audio_file = models.FileField(blank=True, null=True)
#     lyrics = models.TextField(blank=True, null=True)
#     duration = models.CharField(max_length=20)
#     # paginate_by = 2

# def __str__(self):
#     return self.title


class Player(models.Model):
    volume = models.FloatField(default=0.5)  # Volume level, default to 0.5
    current_audio_index = models.PositiveIntegerField(blank=True,
                                                      null=True)  # Index of the currently playing audio, can be blank initially
    is_playing = models.BooleanField(default=False)


class Premium(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    Type = models.CharField(max_length=200, blank=True, null=True)
    Price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.Type


class Audio(models.Model):
    title = models.TextField(max_length=200)
    image = models.ImageField()
    audio_file = models.FileField(blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=20)
    paginate_by = 2

    def __str__(self):
        return self.title
