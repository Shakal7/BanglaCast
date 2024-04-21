from django.contrib import admin
from .models import Episode, Playlist, Premium, Audio
from .models import Creator

# Register your models here.

admin.site.register([Episode, Playlist, Premium, Audio, Creator])