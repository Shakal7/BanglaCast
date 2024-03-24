from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Episode(models.Model):
    Title = models.CharField(max_length=200)
    # Duration = models.PositiveIntegerField()
    Like = models.IntegerField(blank=True, null=True)
    Share = models.IntegerField(blank=True, null=True)
    Download = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.Title


class Playlist(models.Model):
    l_title = models.CharField(max_length=200)
    Type_choice = (
        ('Story', 'Story'),
        ('Business', 'Business'),
        ('Sports', 'Sports'),
        ('Education', 'Education'),
    )
    Type = models.CharField(max_length=100, choices=Type_choice, blank=True, null=True)

    def __str__(self):
        return self.l_title


# class Player(models.Model):
#     Volume = models.FloatField()
#     Current_Audio_Index = models.ImageField(blank=True, null=True)


class Premium(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    Type = models.CharField(max_length=200, blank=True, null=True)
    Price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.Type


class Subscription(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    Sub_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __int__(self):
        return self.user_name
