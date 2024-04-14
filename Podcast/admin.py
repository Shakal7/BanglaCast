from django.contrib import admin
from .models import Episode, Playlist, Premium, Subscription
from .models import Creator

# Register your models here.

admin.site.register([Episode, Playlist, Premium, Subscription,Creator])