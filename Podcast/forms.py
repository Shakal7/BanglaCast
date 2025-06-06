from django.forms import ModelForm
from .models import *


class EpisodeForm(ModelForm):
    class Meta:
        model = Episode
        fields = ('Title', 'Artist', 'Type', 'image', 'audio_files', 'playlist', 'category', 'is_premium')


class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', 'description', 'Artist', 'Type', 'image', 'category']
