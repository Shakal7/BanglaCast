from django.shortcuts import render
from .models import *


# Create your views here.

def episode(request):
    episode = Episode.objects.all()
    context = {
        'episode': episode,
    }
    return render(request, template_name='PodCast/Episode.html', context=context)
