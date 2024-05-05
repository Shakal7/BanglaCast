from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register([Episode, Premium, Audio, Profile, Channel, Playlist])
