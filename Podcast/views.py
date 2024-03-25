from django.shortcuts import render
from .models import *


# Create your views here.

def Podcast(request):
    podcast = Podcast.objects.all()
    context = {
        'Podcast': podcast,
    }
    return render(request, template_name='PodCast/Episode.html', context=context)
