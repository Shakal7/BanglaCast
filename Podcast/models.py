from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime


# Create your models here.

class Playlist(models.Model):
    name = models.CharField(max_length=100, default='General')
    description = models.TextField(blank=True, null=True)
    Artist = models.CharField(max_length=200, blank=True, null=True)
    Type = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True, default='images/default.jpg')

    def __str__(self):
        return self.name


class Episode(models.Model):
    Title = models.CharField(max_length=200)
    Artist = models.CharField(max_length=200, blank=True, null=True)
    Type = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True, default='images/default.jpg')
    audio_files = models.FileField(upload_to='images', blank=True, null=True)
    is_premium = models.BooleanField(default=False)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='episodes', null=True, blank=True)

    def __str__(self):
        return self.Title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)
    expiry_date = models.DateTimeField(null=True, blank=True)
    is_creator = models.BooleanField(default=False)  # NEW: True if user is a creator

    def is_premium_active(self):
        """Check if the listener's premium subscription is still valid."""
        return self.is_premium and self.expiry_date and self.expiry_date > datetime.now()

    def renew_premium(self, days=30):
        """Extend premium for listeners only."""
        if not self.is_creator:  # Creators don’t need premium
            self.is_premium = True
            self.expiry_date = datetime.now() + timedelta(days=days)
            self.save()


class Creator(models.Model):
    Title = models.CharField(max_length=200)
    # Duration = models.PositiveIntegerField()
    Like = models.IntegerField(blank=True, null=True)
    Share = models.IntegerField(blank=True, null=True)
    Download = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.Title


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
    index = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


class Channel(models.Model):
    channel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    audio = models.CharField(max_length=200)
